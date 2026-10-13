# FDA Recalls API — Food, Drug & Product Recall Notices as JSON

REST API for the US Food and Drug Administration's official recall feed. Get the latest FDA recalls, market withdrawals, and safety alerts as clean JSON, filter by keyword such as a brand, ingredient, or hazard, and power food-safety alerts, compliance dashboards, and grocery or supply-chain monitoring.

👉 **[Get a free API key on RapidAPI](https://rapidapi.com/crisp-point-studio-crisp-point-studio-default/api/live-fda-product-food-recalls)**

---

## Quick Start

```bash
curl 'https://live-fda-product-food-recalls.p.rapidapi.com/api/recalls?search=salmonella' \
  -H 'X-RapidAPI-Key: YOUR_RAPIDAPI_KEY' \
  -H 'X-RapidAPI-Host: live-fda-product-food-recalls.p.rapidapi.com'
```

Full examples: [Python](examples/python/quickstart.py) · [JavaScript](examples/javascript/quickstart.js) · [curl](examples/curl.sh)

---

## Endpoint Reference

Base URL: `https://live-fda-product-food-recalls.p.rapidapi.com`

### `GET /api/recalls`

Returns the most recent FDA recall notices, newest first. The FDA feed carries the 20 most recent notices at any time, so a request without a filter returns up to 20 entries.

#### Query Parameters

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `search` | string | No | — | Case-insensitive keyword match on the recall title, e.g. `salmonella`, `listeria`, `undeclared`, or a brand name. |
| `limit` | integer | No | `50` | Maximum entries to return, 1 to 250. |

#### Response

A JSON array of recall objects, newest first.

| Field | Type | Description |
| :--- | :--- | :--- |
| `title` | string | Recall headline as published by the FDA |
| `link` | string | URL of the full recall notice on fda.gov |
| `pubDate` | string | Publication time in RFC 2822 format, US Eastern time |

#### Sample Response

`GET /api/recalls?limit=2`

```json
[
  {
    "title": "Oliva LLC Issues Allergy Alert on Undeclared Sesame in Baba Ghanouj, Spicy Baba Ghanouj, and Hummus",
    "link": "http://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts/oliva-llc-issues-allergy-alert-undeclared-sesame-baba-ghanouj-spicy-baba-ghanouj-and-hummus",
    "pubDate": "Fri, 09 Oct 2026 15:08:00 EDT"
  },
  {
    "title": "Krasnyi Oktyabr Inc. Recalls Starfish Seafood Trio Because of Possible Health Risk",
    "link": "http://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts/krasnyi-oktyabr-inc-recalls-starfish-seafood-trio-because-possible-health-risk",
    "pubDate": "Fri, 09 Oct 2026 14:41:00 EDT"
  }
]
```

---

## Pricing

All plans are billed through RapidAPI. Full details on the [pricing tab](https://rapidapi.com/crisp-point-studio-crisp-point-studio-default/api/live-fda-product-food-recalls/pricing).

| Plan | Price | Requests / month | Rate limit |
| :--- | :--- | :--- | :--- |
| Basic | Free | 100 | 1,000 per hour |
| Pro | $9.99 / month | 10,000 | — |
| Ultra | $29.99 / month | 50,000 | — |

---

## Data Source

Data comes from the official [FDA Recalls, Market Withdrawals & Safety Alerts](https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts) feed, which covers food, drugs, medical devices, cosmetics, and other FDA-regulated products.

**Refresh frequency: real-time.** Responses reflect the FDA feed as it stands at the moment of the request. Notices typically appear within minutes of the FDA publishing them.

## License

The example code in this repository is released under the [MIT License](LICENSE). The API service itself and the data it returns are governed by the RapidAPI terms of service and FDA data terms, not by this license.

---

👉 **[Subscribe on RapidAPI](https://rapidapi.com/crisp-point-studio-crisp-point-studio-default/api/live-fda-product-food-recalls)** · Built by Crisp Point Studio
