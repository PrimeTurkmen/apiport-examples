# curl — everything an agent needs

```bash
B=https://apiport.ae

# sign up (own workspace, you are its admin)
curl -s -X POST $B/api/v1/auth/signup -H 'content-type: application/json' \
  -d '{"email":"you@company.com","password":"longenough","name":"You","workspace":"My Fleet"}'

# login → short token; agent-token → 90-day token
ACCESS=$(curl -s -X POST $B/api/v1/auth/login -H 'content-type: application/json' -d '{"email":"you@company.com","password":"longenough"}' | jq -r .data.accessToken)
TOKEN=$(curl -s -X POST $B/api/v1/auth/agent-token -H "authorization: Bearer $ACCESS" | jq -r .data.token)
H="authorization: Bearer $TOKEN"

# workspaces
curl -s $B/api/v1/sites -H "$H" | jq '.data[] | {id,name}'
SITE=$(curl -s $B/api/v1/sites -H "$H" | jq -r '.data[0].id')

# register a device (Teltonika IMEI as externalId), then point the tracker at apiport.ae:5027
curl -s -X POST $B/api/v1/sites/$SITE/devices -H "$H" -H 'content-type: application/json' \
  -d '{"externalId":"352094081234567","name":"Truck 7","type":"vehicle"}'

# latest positions / alerts / zones
curl -s "$B/api/v1/sites/$SITE/positions/current" -H "$H" | jq '.data[:3]'
curl -s "$B/api/v1/sites/$SITE/alerts?state=open" -H "$H" | jq '.data[:3]'
curl -s "$B/api/v1/sites/$SITE/zones" -H "$H" | jq '.data'

# a report
curl -s -X POST $B/api/v1/sites/$SITE/reports/generate -H "$H" -H 'content-type: application/json' \
  -d '{"template":"trips","dateFrom":"2026-11-01","dateTo":"2026-11-07"}' | jq '{title,summary}'

# ask in natural language
curl -s -X POST $B/api/v1/sites/$SITE/ai/ask -H "$H" -H 'content-type: application/json' \
  -d '{"question":"Which vehicles were speeding this week?"}'

# MCP, raw JSON-RPC (what the SDK does for you)
curl -s -X POST $B/mcp -H "$H" -H 'content-type: application/json' -H 'accept: application/json, text/event-stream' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'
```
