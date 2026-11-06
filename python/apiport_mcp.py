"""Call the APIport MCP server from Python with the official `mcp` package (pip install mcp)."""
import asyncio, os
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

TOKEN = os.environ["APIPORT_AGENT_TOKEN"]  # from POST /api/v1/auth/agent-token

async def main():
    async with streamablehttp_client("https://apiport.ae/mcp", headers={"Authorization": f"Bearer {TOKEN}"}) as (r, w, _):
        async with ClientSession(r, w) as s:
            await s.initialize()
            print([t.name for t in (await s.list_tools()).tools])
            sites = await s.call_tool("list_sites", {})
            print(sites.structuredContent)
            devices = await s.call_tool("get_devices", {"search": ""})
            print(devices.structuredContent["data"]["devices"][:3])

asyncio.run(main())
