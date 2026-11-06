"""APIport REST in 30 lines: sign in, list sites, latest positions, a speed report."""
import os, requests

B = "https://apiport.ae"
EMAIL, PASSWORD = os.environ["APIPORT_EMAIL"], os.environ["APIPORT_PASSWORD"]

tok = requests.post(f"{B}/api/v1/auth/login", json={"email": EMAIL, "password": PASSWORD}, timeout=15).json()["data"]["accessToken"]
S = requests.Session(); S.headers["Authorization"] = f"Bearer {tok}"

sites = S.get(f"{B}/api/v1/sites", timeout=15).json()["data"]
site = sites[0]; print("workspace:", site["name"])

positions = S.get(f"{B}/api/v1/sites/{site['id']}/positions/current", timeout=15).json()["data"]
for p in positions[:5]:
    print(f"{p['name']:<24} {p['lat']:.5f},{p['lon']:.5f}  speed={p.get('speed')}  seen={p.get('lastUpdate')}")

report = S.post(f"{B}/api/v1/sites/{site['id']}/reports/generate",
                json={"template": "speed", "dateFrom": "2026-11-01", "dateTo": "2026-11-07"}, timeout=60).json()
print("report:", report.get("title"), report.get("summary"))
