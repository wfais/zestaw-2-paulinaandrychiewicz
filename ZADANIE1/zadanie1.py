def dodaj_element(wejscie):
    
    def znajdz_max_glebokosc(element, glebokosc=0):
        max_glebokosc = glebokosc if isinstance(element, list) else glebokosc - 1
        if isinstance(element, (list, tuple)):
            for i in element:
                if isinstance(i, (list, tuple, dict)):
                    max_glebokosc = max(max_glebokosc, znajdz_max_glebokosc(i, glebokosc + 1))
        elif isinstance(element, dict):
            for wartosc in element.values():
                if isinstance(wartosc, (list, tuple, dict)):
                    max_glebokosc = max(max_glebokosc, znajdz_max_glebokosc(wartosc, glebokosc + 1))   
        return max_glebokosc                         
        
    def dodaj_na_glebokosci(element, docelowa_glebokosc, aktualna_glebokosc=0):
        if aktualna_glebokosc == docelowa_glebokosc:
            if isinstance(element, list):
                nowa_wartosc = element[-1] + 1 if element else 1
                element.append(nowa_wartosc)
            return
        if isinstance(element, (list,tuple)):
            for i in element:
                if isinstance(i, (list, tuple, dict)):
                    dodaj_na_glebokosci(i, docelowa_glebokosc, aktualna_glebokosc + 1)
        elif isinstance(element, dict):
            for wartosc in element.values():
                if isinstance(wartosc, (list, tuple, dict)):
                        dodaj_na_glebokosci(wartosc, docelowa_glebokosc, aktualna_glebokosc + 1)   
        
    maksymalna_glebokosc = znajdz_max_glebokosc(wejscie)
    dodaj_na_glebokosci(wejscie, maksymalna_glebokosc)    

    return wejscie

if __name__ == '__main__':
    input_list = [
     1, 2, [3, 4, [5, {"klucz": [5, 6], "tekst": [1, 2]}], 5],
     "hello", 3, [4, 5], 5, (6, (1, [7, 8]))
    ]
    output_list = dodaj_element(input_list)
    print(output_list)   