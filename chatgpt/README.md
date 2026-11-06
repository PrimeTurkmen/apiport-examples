# ChatGPT

1. Settings → **Connectors** → **Add** (developer mode may need to be on).
2. URL: `https://apiport.ae/mcp` — leave auth on **OAuth**; ChatGPT discovers the rest.
3. Sign in on the APIport page that opens. The page says exactly what is granted: *read-only — sites, devices, positions, alerts, trips, reports*.
4. In a chat, enable the APIport connector and ask: *"Where are my vehicles right now?"*

Revoke any time from the connector settings; the token also expires on its own.
