# Claude Code

## Interactive (OAuth)

```bash
claude mcp add --transport http apiport https://apiport.ae/mcp
```

Claude opens the APIport sign-in page the first time a tool is used.

## Headless (CI, servers) — 90-day agent token

```bash
ACCESS=$(curl -s -X POST https://apiport.ae/api/v1/auth/login \
  -H 'content-type: application/json' \
  -d '{"email":"you@company.com","password":"..."}' | jq -r .data.accessToken)

TOKEN=$(curl -s -X POST https://apiport.ae/api/v1/auth/agent-token \
  -H "authorization: Bearer $ACCESS" | jq -r .data.token)

claude mcp add --transport http apiport https://apiport.ae/mcp \
  --header "Authorization: Bearer $TOKEN"
```

Then: `claude "Which devices are offline in my fleet?"`
