# CO Tanker Intelligence v1.8

**Aplikacja:** https://koszrozmai.github.io/CO-Tanker-Intelligence/

Wersja dla Chrome (Windows) i Samsung Android PWA. Otwórz link w Chrome, a na Samsungu wybierz menu przeglądarki → **Dodaj do ekranu głównego** / **Zainstaluj aplikację**. Po pierwszym otwarciu online aplikacja przechowuje powłokę do pracy offline.

## Monitoring informacji
Workflow `.github/workflows/collect.yml` jest uruchamiany przy zmianach, ręcznie oraz według harmonogramu co trzy godziny (UTC). Publikuje `docs/data/intelligence.json`. **Wyniki kolektora to wykryte odsyłacze, a nie zatwierdzone interpretacje przepisów**. Sprawdzaj oryginalne źródło oraz datę obowiązywania. Harmonogram GitHub Actions nie jest gwarancją wykonania o określonej godzinie. Zmiany krytyczne wymagają zatwierdzenia przez oficera i zgodności z SMS, banderą, instrukcją producenta i dokumentacją statku.

## Aktualizacje i kopie danych
Dane prywatne, notatki i postęp przechowywane lokalnie w przeglądarce **nie synchronizują się między telefonem a komputerem**. W aplikacji wykonaj eksport kopii zapasowej i import na drugim urządzeniu. Nie publikuj dokumentów statkowych ani danych załogi w publicznym repozytorium. Kod źródłowy i pełen pakiet ZIP v1.8 pozostały do odrębnego przeniesienia; strona jest uruchamiana z samodzielnego pliku HTML v1.8.

**Status:** GitHub Pages wymaga aktywnego źródła `GitHub Actions` w ustawieniach Pages. Sprawdź działanie wdrożenia w zakładce Actions.

## Uproszczony interfejs v1.9
Na Samsungu jeden zwarty wybór modułu zamiast zdublowanej nawigacji. Na komputerze najważniejsze moduły są widoczne od razu, a pozostałe pod „Więcej modułów”. Dodatkowe karty na pulpicie są dostępne po rozwinięciu. **Wszystkie dotychczasowe opcje i dane pozostają dostępne.** Nowa nadrzędna reguła UI/UX znajduje się w [MASTER_PROMPT_CO_v2.2.md](MASTER_PROMPT_CO_v2.2.md).
