# APIport examples — connect your AI agent to live fleet telemetry

[APIport](https://apiport.ae) is an AI-native telematics platform by [PILOT Telematics](https://pilot-gps.com).
It exposes vehicle positions, alerts, history and reports as **MCP tools** and a **REST API**.

**30 seconds to connect:**

```bash
# 1. Sign up (creates your own workspace; you are its admin)
curl -X POST https://apiport.ae/api/v1/auth/signup \
  -H 'content-type: application/json' \
  -d '{"email":"you@company.com","password":"choose-a-long-one","name":"You","workspace":"My Fleet"}'

# 2. Add the MCP server to Claude Code — it will open the APIport sign-in page (OAuth)
claude mcp add --transport http apiport https://apiport.ae/mcp

# 3. Ask
#    "Which of my vehicles are moving right now?"
#    "Build a speed report for the last 7 days."
```

ChatGPT / Claude.ai / Cursor: add a connector with the URL **`https://apiport.ae/mcp`** — nothing else to configure.

## What the agent gets

| Tool | Returns |
|---|---|
| `list_sites` | Workspaces the token can access |
| `get_devices` | Devices with their latest observation; search by name or exact device ID |
| `get_alerts` | Unresolved alerts: speeding, geofence, offline, battery |
| `get_vehicle_history` | Telemetry coverage and service records for one device (≤ 30 days) |
| `get_report` | Mileage, trips, speed or parking report for a date range (≤ 31 days) |

All tools are **read-only**. Writes (zones, rules, devices, device commands) go through the authenticated REST API.

## Folders

- [`claude-code/`](claude-code) — one command, plus a headless token variant
- [`claude-desktop/`](claude-desktop) — `claude_desktop_config.json`
- [`cursor/`](cursor) — `.cursor/mcp.json`
- [`chatgpt/`](chatgpt) — connector setup, what the OAuth screen looks like
- [`python/`](python) — call the REST API and the MCP server from Python
- [`node/`](node) — the official MCP SDK client in 25 lines
- [`curl/`](curl) — every endpoint an agent needs, as copy-paste curl
- [`prompts/`](prompts) — prompts that map 1:1 to the tools

## Auth in one paragraph

Hosted agents (ChatGPT, Claude.ai) use **OAuth 2.1**: the host reads `https://apiport.ae/.well-known/oauth-authorization-server`, registers itself, sends you to the sign-in page, and gets a read-only token (scope `fleet:read`) that it refreshes by itself.
Scripts use a **90-day agent token**: `POST /api/v1/auth/login` → `POST /api/v1/auth/agent-token` → `Authorization: Bearer <token>`.

## Links

- MCP discovery (no auth): https://apiport.ae/mcp
- OpenAPI 3.1: https://apiport.ae/openapi.json
- LLM summary: https://apiport.ae/llms.txt
- Developer guide: https://apiport.ae/developers/
- Pricing: https://apiport.ae/pricing/ — Agent $1 / Fleet $3 per active device per month, Custom by quote
- Devices: Teltonika FMx (Codec 8/8E) → `apiport.ae:5027`; PILOT Telematics fleets sync from Settings

Questions: support@apiport.ae
