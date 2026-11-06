// npm i @modelcontextprotocol/sdk — then: APIPORT_AGENT_TOKEN=... node mcp-client.mjs
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';

const client = new Client({ name: 'my-agent', version: '1.0.0' });
await client.connect(new StreamableHTTPClientTransport(new URL('https://apiport.ae/mcp'), {
  requestInit: { headers: { Authorization: `Bearer ${process.env.APIPORT_AGENT_TOKEN}` } },
}));

const { tools } = await client.listTools();
console.log('tools:', tools.map(t => t.name));

const sites = await client.callTool({ name: 'list_sites', arguments: {} });
const siteId = sites.structuredContent.sites[0].id;

const alerts = await client.callTool({ name: 'get_alerts', arguments: { site_id: siteId } });
console.log('open alerts:', alerts.structuredContent.data.alerts.length);

const report = await client.callTool({ name: 'get_report', arguments: { site_id: siteId, template: 'mileage', dateFrom: '2026-11-01', dateTo: '2026-11-07', deviceIds: [] } });
console.log(report.structuredContent.data.title, report.structuredContent.data.summary);
await client.close();
