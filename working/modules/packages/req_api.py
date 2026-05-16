import requests
import sys
import json

try:
    if len(sys.argv) < 2:
        print("Not a good search term")
        sys.exit(1)
    results = []
    response = requests.get(
        "https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1]
    )
    data = response.json()

    for result in data["results"]:
        results.append(
            {
                "artist": result["artistName"],
                "track": result["trackName"],
                "album": result["collectionName"],
            }
        )
        print(json.dumps(results, indent=4))
except requests.RequestException as e:
    print(f"Error fetching API data: {e}")
