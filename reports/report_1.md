# Błąd 1 - sortowanie
### Tytuł 
Przycisk `Wyczyść` nie resetuje zastosowanego sortowania

### Środowsko 
- Przegladarka 
Brave 1.84.141 (Oficjalna wersja) (64-bitowa)
Chromium: 142.0.7444.176
- Windows 11 Home, 24H2

### Opis
Na stronie jest możliwość sortowania filmów według trzech kategorii: popularność, oceny i daty produkcji. 
Każdą z kategorii można ustawić w trybie rosnącym lub malejacym. Może być zaznaczone wiele kategorii w 
jednym momencie. 
Zarządzanie sortowaniem odbywa się w modalu wyświetlanym po kliknięciu `Sortuj wg.` 
Aby wyczyscić sortowania zastosowano przycisk `Wyczyść` wyświetlany w modalu.

### Kroki do odtworzenia
1. Otwórz `https://vod.film/filmy`
2. Kliknij `Sortuj wg.`
3. Wybierz dowolne sortowanie
4. Nacisnij `Wyczyść` obok `Sortuj wg.`

### Rezultat oczekiwany
Wybrane wyszukiwanie zostanie wyczyszczone i lista filmów zostanie odświeżona. Z aktywnego URL zniknie 
parametr odpowiedzialny za sortowanie.

### Rezultat aktualny
Wybrane wyszukwanie pozostaje aktywne, nie można go usunąć, trzeba edytowac URL aby zobaczyć liste bez sortowania.

### Priorytet 
niski

### Uzasadnienie 
Brak możliwości wyczyszczenia sortowania nie powoduje, że użytkownik nie może korzystać z kluczowych 
funkcjonalności systemu.
Użytkownik nadal może przeglądac filmy i je odtwarzać. 
