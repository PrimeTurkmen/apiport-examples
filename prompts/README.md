# Prompts that map to real tools

| Say | Tool the agent calls |
|---|---|
| "Which workspaces do I have?" | `list_sites` |
| "Where is truck 7 right now?" | `get_devices(search="truck 7")` |
| "Which devices are offline?" | `get_devices` + timestamps |
| "Any open alerts?" | `get_alerts` |
| "Show me the last 2 weeks for device 352094081234567" | `get_vehicle_history(deviceId, days=14)` |
| "Build a speed report for last week" | `get_report(template="speed", dateFrom, dateTo)` |
| "Mileage per vehicle this month" | `get_report(template="mileage", ...)` |
| "How long was each vehicle parked yesterday?" | `get_report(template="parking", ...)` |
| "List trips for the Dong Feng trucks on Monday" | `get_devices(search="dong feng")` → `get_report(template="trips", deviceIds=[...])` |

Tips: dates are `YYYY-MM-DD`, ranges ≤ 31 days, history ≤ 30 days. Old timestamps mean "last seen", not "live".
