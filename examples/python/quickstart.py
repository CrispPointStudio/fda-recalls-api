"""FDA Recalls API quick start (Python 3, requires `pip install requests`).

Get a free key:
https://rapidapi.com/crisp-point-studio-crisp-point-studio-default/api/live-fda-product-food-recalls
"""

import requests

HOST = "live-fda-product-food-recalls.p.rapidapi.com"
API_KEY = "YOUR_RAPIDAPI_KEY"

HEADERS = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": HOST,
}


def fetch_recalls(search: str | None = None, limit: int = 50) -> list[dict]:
    """Return up to `limit` FDA recall notices (newest first), optionally filtered by keyword."""
    params: dict[str, str | int] = {"limit": limit}
    if search:
        params["search"] = search
    response = requests.get(
        f"https://{HOST}/api/recalls",
        headers=HEADERS,
        params=params,
        timeout=15,
    )
    response.raise_for_status()
    return response.json()  # bare JSON array


if __name__ == "__main__":
    recalls = fetch_recalls("salmonella", limit=10)
    print(f"Retrieved {len(recalls)} recalls.")
    for r in recalls:
        print(f"{r['pubDate']}  {r['title']}")
