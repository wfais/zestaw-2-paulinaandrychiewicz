def rzymskie_na_arabskie(rzymskie):
    if not isinstance(rzymskie, str):
        raise TypeError(f"Oczekiwano stringa, otrzymano {type(rzymskie).__name__}")
    
    rzymskie = rzymskie.upper()
    
    mapa_rzymskie = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    wartosc = 0
    i = 0

    while i < len(rzymskie):
        if rzymskie[i] not in mapa_rzymskie:
            raise ValueError(f"Nieprawidłowy znak rzymski: {rzymskie[i]}")
        if i + 1 < len(rzymskie) and mapa_rzymskie[rzymskie[i]] < mapa_rzymskie[rzymskie[i + 1]]:
            wartosc += mapa_rzymskie[rzymskie[i + 1]] - mapa_rzymskie[rzymskie[i]]
            i += 2
        else:
            wartosc += mapa_rzymskie[rzymskie[i]]
            i += 1

    if arabskie_na_rzymskie(wartosc) != rzymskie:
        raise ValueError(f"Nieprawidłowa liczba rzymska: {rzymskie}. Czy chodziło o {arabskie_na_rzymskie(wartosc)}?")        

    return wartosc

def arabskie_na_rzymskie(arabskie):
    if not isinstance(arabskie, int):
        raise TypeError(f"Oczekiwano integera, otrzymano {type(arabskie).__name__}")

    if arabskie < 1 or arabskie > 3999:
        raise ValueError("Liczba musi być w zakresie od 1 do 3999")
    
    mapa_arabskie = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]

    rzymskie = ""
    for wartosc, symbol in mapa_arabskie:
    
        while arabskie >= wartosc:
            rzymskie += symbol
            arabskie -= wartosc

    return rzymskie

if __name__ == '__main__':
    try:
        # Przykłady konwersji rzymskiej na arabską
        rzymska = "MCMXCIV"
        print(f"Liczba rzymska {rzymska} to {rzymskie_na_arabskie(rzymska)} w arabskich.")
        
        # Przykłady konwersji arabskiej na rzymską
        arabska = 1994
        print(f"Liczba arabska {arabska} to {arabskie_na_rzymskie(arabska)} w rzymskich.")
        
    except ValueError as e:
        print(e)
