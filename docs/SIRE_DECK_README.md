# SIRE 2.0 Deck Trainer — aktualizacja programu

## Podstawa
Źródło: dwa tomy OCIMF SIRE 2.0 Question Library, version 1.0 (January 2022), przesłane przez użytkownika. Zidentyfikowano 258 niepowtarzających się pytań dotyczących pokładu, nawigacji, zarządzania, bezpieczeństwa, MARPOL, operacji ładunkowych i balastowych, cumowania i kotwiczenia, fotografii oraz działań w lodzie.

Nie publikujemy pełnych rozdziałów dokumentów; aplikacja przechowuje numer, krótki tytuł, treść pytania w skróconej postaci oraz krótkie, źródłowe fragmenty dotyczące celu, działań inspektora, oczekiwanych dowodów i potencjalnych obserwacji. Dodatkowe wskazówki treningowe są jawnie odróżnione od materiału OCIMF.

## Zakres
Dla oil i chemical tankers z wyłączeniem głównego rozdziału maszynowego (10), podrozdziałów wyłącznie LNG/LPG/IGC, DP/shuttle-specific, większości fotografii maszynowni oraz zagadnień niedotyczących pracy działu pokładowego. Pytania z zakresu ogólnego ISM, STCW, fire safety i nawigacji pozostają, nawet jeśli mają odniesienie do współpracy z innymi działami. System nie oznacza automatycznie pozycji jako mającej zastosowanie do konkretnego statku; wątpliwości rozstrzyga instrukcja, HVPQ, wyposażenie i CoF.

## UI
Dział Trening i AI rozpoczyna się od bazy SIRE, z filtrem rodzaju tankowca (domyślnie chemical), działów, wyszukiwarką ID/tematu i powtórkami. Zaznaczając stopień przygotowania użytkownik tworzy lokalny plan przeglądu po 0/2/7/14/30/60 dniach. Treść pytania nie jest testem ABCD, lecz ćwiczeniem realnego pokazania procesu / dokumentów / czynności na statku.

Wszystkie wcześniej istniejące ćwiczenia PSC, CDI, archiwalne scenariusze i AI handoff pozostają w rozwijanej sekcji. Nowa baza ma dodatkowy przycisk kopiowania szczegółowego pytania do AI z obowiązkiem weryfikacji aktualnych źródeł.

Postęp przechowuje się lokalnie (bez danych statkowych w repozytorium). Istnieje osobny eksport i integracja z eksportem/importem danych głównej aplikacji. Oba tryby — PWA i Chrome — otrzymują identyczne dane. Service worker buforuje bibliotekę dla pracy offline. Budowniczy jednostronicowego HTML osadza dane bez zewnętrznych zależności.

## Źródła i ograniczenia
- OCIMF oficjalny program: https://www.ocimf.org/programmes/sire-2-0/
- IMO chemical pollution: https://www.imo.org/en/ourwork/environment/pages/chemicalpollution-default.aspx

Ważne: baza 2022 nie jest gwarancją aktualności SIRE, nie zastępuje vessel-specific VIQ, zatwierdzonego SMS/QMS, P&A Manual, Certificate of Fitness, SDS ani instrukcji producenta. Żadna odpowiedź w ćwiczeniu nie potwierdza faktycznej zgodności statku. Pojedyncza pozycja może być warunkowa (np. COW lub SPM). Materiały IMO/OCIMF i daty obowiązywania należy weryfikować przed rzeczywistym użyciem.

## Kontrola
Automatyczne testy agent/test_sire_deck.py, node --check, budowa offline oraz kontrola ID, wymaganych pól i nieusuniętych oryginalnych funkcji. Po przejściu testów nadal potrzebna próba ręczna na Samsungu/Chrome w rzeczywistej przeglądarce.
