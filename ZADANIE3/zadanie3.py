import requests, re, time, sys
from collections import Counter

URL = "https://pl.wikipedia.org/api/rest_v1/page/random/summary"
N = 100  # liczba losowań
HEADERS = {
    "User-Agent": "wp-edu-wiki-stats/0.1 (paulina.andrychiewicz@student.uj.edu.pl)",
    "Accept": "application/json",
}

# przygotowanie wyrażenia regularnego wyłapującego słowa (litery)
WORD_RE = re.compile(r"[^\W\d_]+", re.UNICODE)


def selekcja(text: str):
    # Zwróć listę słów wydobytych z 'text', spełniających warunki zadania:
    #  - słowa zapisane małymi literami
    #  - długość każdego słowa > 3 znaki
    #
    # Wskazówka:
    #  użyj WORD_RE.findall(text), następnie przefiltruj wynik
    #
    # Przykład:
    #  selekcja("Ala ma 3 koty i 2 psy oraz żółw")
    #     -> ["koty", "oraz", "żółw"]
    words = []
    for word in WORD_RE.findall(text):
        word_lower = word.lower()
        if len(word_lower) > 3:
            words.append(word_lower)
    return words


def ramka(text: str, width: int = 80) -> str:
    # Zwróć napis w ramce o stałej szerokości, w postaci:
    #   [        treść wyśrodkowana w polu o szerokości width-2       ]
    #
    # Jeśli text jest za długi (ma więcej znaków niż width-2),
    # obetnij go do width-3 i dodaj na końcu znak '…' (U+2026).
    #
    # Następnie wyśrodkuj (użyj str.center(...)) i doklej nawiasy
    # kwadratowe po bokach. Zwróć wynik w postaci f"[{...}]".
    #
    # Przykład:
    #   ramka("Kot", width=10)  ->  "[  Kot   ]"   (łącznie 10 znaków)
    szerokosc_tekstu = width - 2
    
    if len(text) > szerokosc_tekstu:
        text = text[:szerokosc_tekstu - 1] + "…"

    return f"[{text.center(szerokosc_tekstu)}]"    


def main():
    cnt = Counter()
    licznik_slow = 0
    pobrane = 0

    # linia statusu
    print(ramka("Start"), end="", flush=True)

    while pobrane < N:
        try:
            data = requests.get(URL, headers=HEADERS, timeout=10).json()
        except Exception:
            # timeout / brak JSON → spróbuj ponownie
            time.sleep(0.1)
            continue

        # Pobierz tytuł hasła z 'data' (klucz "title"; jeśli brak, użyj pustego łańcucha)
        # Następnie drukuj ramkę z tym tytułem:
        #  - zbuduj łańcuch: "\r" + ramka(tytul, 80)
        #  - wydrukuj print(..., end="", flush=True), by nadpisywać bieżącą linię w konsoli
        #
        # Przykład:
        #   title = data.get("title") or ""
        #   line = "\r" + ramka(title, 80)
        #   print(line, end="", flush=True)

        # Pobierz 'extract' (klucz "extract"; jeśli brak, użyj ""), przepuść przez selekcja()
        #  - wynikowa lista słów (>=4) powinna zostać doliczona do licznika:
        #       cnt.update(lista_slow)
        #  - dolicz też do licznik_slow długość tej listy
        #  - zwiększ licznik 'pobrane' (udało się przetworzyć jedną próbkę)
        #  - opcjonalnie mała przerwa: time.sleep(0.05)

        title = data['title'] if 'title' in data else ""
        linia = "\r" + ramka(title, 80)
        print(linia, end="", flush=True)

        extract = data['extract'] if 'extract' in data else ""
        lista_slow = selekcja(extract)
        cnt.update(lista_slow)
        licznik_slow += len(lista_slow)
        pobrane += 1
        time.sleep(0.05)

    print()
    print(f"Pobrano wpisów: {pobrane}")
    print(f"Słów (≥4) łącznie:  {licznik_slow}")
    print(f"Unikalnych (≥4):  {len(cnt)}\n")

    print("Top 15 słów (≥4):")
    # tu wypisz w pętli, korzystając np. z most_common(15)

    for word, count in cnt.most_common(15):
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
