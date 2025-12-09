# Błąd 2 - Co obejrzeć?
### Tytuł
Co obejrzeć nie wyświetla propozycji po zmienie kategorii

### Środowisko
- Przeglądarka 
Brave 1.84.141 (Oficjalna wersja) (64-bitowa)
Chromium: 142.0.7444.176
- Windows 11 Home, 24H2

### Opis
Na stronie jest możliwość wylosowania propozycji filmu lub serialu do obejrzenia. 
Użytkownik może określić kategorie (film lub serial) oraz gatunek produkcji.

### Kroki do odtworzenia
1. Otwórz `https://vod.film/co-obejrzec`
2. Wybierz kategorie `Filmy`
3. Wybierz gatunek `Akcja`
3. Kliknij `Losuj`
4. Wybierz kategorie `Seriale`
5. Kliknij `Losuj`


### Rezultat oczekiwany
Przy zmianie kategorii z `Filmy` na `Seriale` pole z gatunkami przyjęło wartość `Wszystkie gatunki`. 
Po naciśnięciu `Losuj` powinien wyświetlić się losowy serial spośród wszystkich gatunków. 

### Rezultat aktualny
Serial nie jest losowany. Zamiast wyniku wyszukiwania wyświetla się `Wylosuj film lub serial do obejrzenia...`. 
W zakładce network widać request do wylosowania serialu z gatunkiem akcja. Gatunek nie istnieje wsród 
seriali, wiec request zwrócił brak wyników.

### Priorytet
średni

### Uzasadnienie
Brak możliwości losowania filmów nie powoduje, że użytkownik nie może korzystać z kluczowych funkcjonalności systemu.
Użytkownik nadal może przeglądac filmy i je odtwarzać, jednak część uzytkowników moze wybrac inny serwis, aby wylosować
i obejrzeć film.
