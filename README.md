## Opis projektu

Projekt automatyzacji testów E2E oraz API wraz z raportem z testów manualnych strony **https://vod.film/**.
W repozytorium można znaleźć zautoamtyzowaną ścieżkę pozytywną, negatywną, prosty test API oraz raporty z testów
manualnych strony. Kod został przygotowany z zachowaniem wzorca POM.

Sama strona pozwala wyszukac dany film lub serial i przekierowuje do partnerów, 
którzy posiadają produkcję w swojej ofercie.


## Instrukcja instalacji

W repozytorium znajduje się plik `requirements.txt`. Aby zainstalować zależności użyj:
`pip install -r requirements.txt`

Po instalacji zależności, aby uruchomić wszystkie testy (test api: `test_endpoint`, testy UI: `test_search_positive`,
`test_search_negative`) użyj: `pytest --tb=short`

## Wybrana biblioteka

Zdecydowałam się wybrać Selenium. Zdaję sobie sprawę, że Playwright może być uważany za lepszy wybór ze względu na 
szybkość oraz obsługę dynamicznych elementów (np. pop-up)
jendak pracuje na co dzień z użyciem Selenium i Javy, z Playwrightem nie mam doświadczenia.

## Endpoint używany przy wyszukiwaniu

`https://vod.film/search-route`

Po wyszukaniu frazy `"the pickup"` wysyłane jest zapytanie POST z body:
`{"host": "vod.film", "locale": "pl", "searchTerm": "the pickup"}`

Endpoint zwraca tablicę wyników pasujących do wyszukiwania. Każdy z znalezionych wyników zawiera: `type, title, title_with_prefix,
slug, overview, poster_path, backdrop_paths, release_date, vote_average, vote_count, popularity, tmdb_id.`

## Napotkane trudności

W `is_text_present` napotkałam trudności z zastosowaniem odpowiedniej funkcji do czekania.
Funkcja sprawdzała widoczność wyników wyszukiwania zanim te sie odświeżyły po wpisaniu frazy do wyszukiwarki.
Finalnie zastosowałam tam twarde `sleep(2)`.

## Raporty znalezionych błędów

Raporty z części manualnej znajdują się w `/reports`. Dla dwóch wybranych błędów utworzono pliki `.md`