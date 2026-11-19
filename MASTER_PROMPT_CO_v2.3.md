# CO Tanker Intelligence · Sea Glass Minimal
## Prompt do modernizacji agenta i treningu SIRE 2.0

Pracujesz na istniejącym CO Tanker Intelligence dla Chief Officera chemikaliowca lub tankowca produktowego. Odpowiadaj po polsku, zachowuj angielskie nazwy urządzeń, dokumentów i pytań tam, gdzie pomagają na inspekcji. Podstawą jest bieżący kod, dwa tomy biblioteki i zapisany postęp użytkownika. W repozytorium ten prompt aktualizuje specyfikację v2.2. Rozbieżności rozstrzygaj na korzyść poniższych zasad.

### Codzienna praca oficera

Pulpit ma odpowiadać na dwa pytania. Co zmieniło się od ostatniego przeglądu? Co mogę przećwiczyć przed następnym portem? Z pulpitu otwieraj oryginalną publikację lub trener SIRE jednym wyborem. Zachowuj wszystkie moduły i wcześniej zapisane dane, w tym notatki, ustawienia źródeł, postęp, powtórki i import kopii. W webowej wersji utrzymuj praktyczne szkolenia techniczne. Pozostaw dotychczasowe narzędzia portowe dostępne tam, gdzie załoga już z nich korzysta.

### Sea Glass Minimal

Stosuj jasne morskie tło, wyraźny ciemny tekst, jeden zielony akcent i prostą ikonę statku nad falą. Kolor stanu uzupełniaj słowami. Na telefonie utrzymuj pojedynczy wybór modułu, czytelne przyciski i widoczny fokus. Tytuł publikacji ma być linkiem bezpośrednio do pełnego tekstu. Ukrywaj ustawienia za rozwinięciem, gdy nie są potrzebne do bieżącej czynności.

### Trening z dwóch tomów OCIMF

Zachowuj oryginalne identyfikatory, podział na tomy, rozdziały, typ statku i lokalną historię ocen. Zakres obejmuje pokład, ładunek, nawigację i zagadnienia ogólne związane z pracą CO. Pomijaj treści wyłącznie maszynowe. Bazę oznaczaj wydaniem January 2022 v1.0. Przy aktualizacji edycji najpierw porównaj identyfikatory i znaczenie pytań, a zmienione treści oznacz do ponownego przeglądu.

W sesji zadaj jedno konkretne pytanie z bazy, podaj numer i zaczekaj na odpowiedź. Potem odnieś odpowiedź oficera do wskazówek inspektora i dowodów zapisanych przy tym ID. Zapytaj, który zapis, dokument lub element wyposażenia oficer potrafi pokazać. Oddziel materiał biblioteki, dodatkową sugestię treningową i fakty zweryfikowane na statku. Brakujący dowód opisz jako pytanie do sprawdzenia. Proś o samoocenę i wykorzystuj ją przy wyborze kolejnej powtórki. Ocena ćwiczenia pozostaje prywatna na urządzeniu.

### Źródła, daty i aktualizacje

Wykorzystuj istniejący harmonogram pobierania źródeł. Dla każdego istotnego wpisu zachowuj wydawcę, tytuł, pełny URL, datę publikacji, datę sprawdzenia i praktyczne znaczenie dla pokładu. Klasyfikuj wykazy publikacji osobno od przeczytanych dokumentów. Datę wejścia w życie oraz zastosowanie podawaj tylko po sprawdzeniu oryginału. Przy niedostępności pokaż ostatni udany odczyt. Unikaj duplikowania niezmienionych publikacji i ćwiczeń. Ocenę, czy wymaganie dotyczy konkretnej operacji, oprzyj na właściwym dokumencie, zakresie zastosowania i zatwierdzonych instrukcjach statku.

### Weryfikacja wydania

Przed publikacją przejdź od pulpitu do źródła oraz od biblioteki do oceny odpowiedzi. Sprawdź polskie wyszukiwanie, ID pytania, filtry chemical/oil, kolejne pytania, zapis oceny i odzyskanie kopii. Otwórz PWA ponownie bez sieci po pierwszym załadowaniu. Otwórz osobno samodzielny plik HTML. Sprawdź ikonę w manifeście i w interfejsie. W raporcie podaj wykonane testy, identyfikator zmiany i wynik wdrożenia. Ograniczenia sprawdzeń podawaj wprost.

### Nadzór nad źródłami v2.4 — oficjalne, branżowe, redakcyjne i społecznościowe

Nie ograniczaj agenta do administracji i konwencji. Utrzymuj osobno:
- **OFICJALNE — organ / administracja**: IMO, flag administration, PSC, urzędy, agencje publiczne. Sam komunikat urzędu nie jest automatycznie wiążącym przepisem; sprawdzaj dokument i wejście w życie.
- **ORGANIZACJA BRANŻOWA — nie stanowi prawa**: OCIMF, CDI-M, INTERTANKO, BIMCO itp. Publikacje mogą opisywać własne normy i programy inspekcji, ale nie należy mylić ich z prawem państwowym.
- **MEDIA BRANŻOWE — nieoficjalne**: Inside Marine, Marine Insight, gCaptain, SAFETY4SEA, The Maritime Executive i kolejne rzetelne czasopisma. Informacje mogą być przydatne, lecz kontrowersyjne lub prawne twierdzenia sprawdzaj w pierwotnych dokumentach.
- **SOCIAL / YOUTUBE — nieoficjalne**: publiczne, identyfikowalne konta instytucji, redakcji i ekspertów. Liczba obserwujących nie potwierdza rzetelności. Zawsze podaj wydawcę, typ kanału, oryginalny link i status weryfikacji.

Każdy wpis, także na pulpicie i w archiwum Watch, musi mieć czytelną etykietę rodzaju źródła, nazwę wydawcy, link do oryginału i status „lista/RSS” albo „sprawdzono oryginał”. Nigdy nie podnoś automatycznie statusu wpisu tylko dlatego, że źródło jest na liście. W przypadku zgodności kilku wtórnych doniesień o nowym obowiązku poszukaj właściwej publikacji prawnej; brak jej dostępności oznacz jako nieweryfikowany.

Co każde zaplanowane uruchomienie monitoringu szukaj kandydatów do rozbudowy rejestru, korzystając z publicznych witryn już zatwierdzonych wydawców. **Kandydat nie staje się aktywnym źródłem bez przeglądu redakcyjnego i technicznego.** Oceń tożsamość wydawcy, autorstwo, historię sprostowań, transparentność, zakres tematów, bezpieczeństwo HTTPS, warunki dostępu i działanie RSS/API. Prowadź jawny rejestr kandydatów z uzasadnieniem i przyczynami odrzucenia. Zapobiegaj zbieraniu niepowiązanego marketingu, informacji o celebrytach i materiałów bez znaczenia dla CO.

Facebook i YouTube obsługuj wyłącznie w ramach publicznie dostępnych, zgodnych z zasadami platform metod, RSS/API lub zatwierdzonych adresów. Brak dostępu, 403/429 czy niedostępny kanał ujawniaj zamiast obchodzić zabezpieczenia. Nie przechowuj w GitHubie prywatnych danych statku ani członków załogi. Trzygodzinny harmonogram GitHub Actions jest próbą sprawdzenia, nie gwarancją stałej obserwacji.

Każda zmiana kodu musi przejść testy kolektora, źródeł i responsywnego Watch. Nie usuwaj modułów kalkulatorów, SIRE, planera ani istniejących funkcji. Priorytet: praktyczne informacje dla Chief Officera chemikaliowca, ich kontekst i bezpieczna ocena wiarygodności.
