import requests


def test_endpoint():
    API_ENDPOINT = "https://vod.film/search-route"
    text = "The pickup"
    payload = {
        "searchTerm": text,
        "locale": "pl",
        "host": "vod.film",
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 "
                      "Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json"
    }

    r = requests.post(API_ENDPOINT, json=payload, headers=headers)
    assert r.status_code == 200

    results = r.json()
    print(results["data"][0])