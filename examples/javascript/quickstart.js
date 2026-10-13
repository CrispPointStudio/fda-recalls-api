// FDA Recalls API quick start (Node 18+ or any runtime with global fetch)
// Get a free key: https://rapidapi.com/crisp-point-studio-crisp-point-studio-default/api/live-fda-product-food-recalls

const HOST = 'live-fda-product-food-recalls.p.rapidapi.com';
const API_KEY = 'YOUR_RAPIDAPI_KEY';

async function getRecalls(search, limit = 50) {
  const url = new URL(`https://${HOST}/api/recalls`);
  url.searchParams.set('limit', String(limit));
  if (search) url.searchParams.set('search', search);

  const response = await fetch(url, {
    headers: {
      'X-RapidAPI-Key': API_KEY,
      'X-RapidAPI-Host': HOST,
    },
  });
  if (!response.ok) {
    throw new Error(`HTTP ${response.status}: ${await response.text()}`);
  }
  return response.json(); // array of recall objects
}

getRecalls('salmonella', 10)
  .then((recalls) => {
    console.log(`Retrieved ${recalls.length} recalls.`);
    for (const r of recalls) {
      console.log(`${r.pubDate}  ${r.title}`);
    }
  })
  .catch((err) => console.error('Error fetching FDA recalls:', err));
