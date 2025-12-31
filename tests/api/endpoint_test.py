import pytest
import requests


@pytest.mark.api
def test_endpoint():
    api_endpoint = "https://vod.film/search-route"
    search_text = "The pickup"

    payload = {
        "searchTerm": search_text,
        "locale": "pl",
        "host": "vod.film",
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 "
                      "Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json"
    }

    try:
        r = requests.post(api_endpoint, json=payload, headers=headers)
    except requests.exceptions.RequestException as e:
        pytest.fail("Can't reach API", e)

    assert r.status_code == 200, "Expected 200, actual: {r.status_code}"

    json_data = r.json()

    assert "data" in json_data, "Missing data"
    assert isinstance(json_data["data"], list), "Expected data to be a list"
    assert len(json_data["data"]) > 0, "Empty list"

    first_movie = json_data["data"][0]
    movie_title = first_movie["title"].lower()

    assert search_text.lower() in movie_title, "Search text not found in movie title"
