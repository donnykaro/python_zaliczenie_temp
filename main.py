# importujesz zewnetrzna biblioteke
import sys
wyniki_uzytkownika = []
#sprobuj pobrac input
n = input()
# blok try except umozliwia wylapanie bledu
try:
    # sprobuj zmienic typ n ze string na int(domyslny typ jaki zwraca input to string)
    n = int(n)
except ValueError:
    # jezeli wystapil blad podczas konwersji wypisz BLAD i zakoncz program
    print('BLAD')
    # sys.exit(0) konczy program
    sys.exit(0)

t0 = 0
t1 = 1
t2 = 2

if int(n) < 0:
    # jezeli n jest mniejszy od 0 wypisz BLAD i zakoncz program, jak powyzej
    print('BLAD')
    sys.exit(0)
else:
    # jezeli n nie jest mniejsze od 0 i jest typu int to zmien typ n na int
    n = int(n)
for n in range(0, int(n)):
    t0 = 0
    t1 = 1
    t2 = 2
    p = input()

    # blok try except umozliwia wylapanie bledu
    try:
        # sprobuj zmienic typ p ze string na int(domyslny typ jaki zwraca input to string)
        p = int(p)
    except ValueError:
        # jezeli wystapil blad podczas konwersji dodaj do tablicy wyniki_uzytkownika tablice [p, 'BLAD'],
        # to tablica wewnatrz tablicy, bedzie to wygladalo mniej wiecej tak [['asd', 'BLAD'], [3, 'TAK']]
        # tego nie musisz wiedziec, ale warto sobie ogarnac jak rozumiesz normalne listy
        wyniki_uzytkownika.append([p, 'BLAD'])
    else:
        if int(p) < 2:
            # jezeli jest mniejsza niz 2 to jak powyzej, dodajemy tablice jak wyzej
            wyniki_uzytkownika.append([p, 'BLAD'])
        else:
            # jezeli liczba przypadkow jest int'em, jest wiekszy od 0, i konkretny przerabiany przypadek
            # tez jest int'em i jest wiekszy od 2 to uruchamiamuy nieskonczona petle, ktora sie zakonczy
            # tylko kiedy uzyjemy instrukcji break
            while True:
                # schemat samego algorytmu jest prosty, czysta matematyka, rozpisz sobie na kartce,
                # bo inaczej tego nie zrozumiesz, to tyczy sie tez kodu za else'm, bo if, elif to instrukcje
                # sprawdzajace kiedy maja przerwac dzialanie petli
                wynik = t0 + t1 + t2
                if p == wynik:
                    # jezeli podany przypadek p jest rowny z wynik, czyli aktualnym elementem ciagu
                    # zapisujemy wynik jako tablice w tablicy jak wyzej, tyle ze zamiast blad piszac 'TAK'
                    # i konczymy petle przechodzac do sprawdzenia kolejnego przypadku
                    wyniki_uzytkownika.append([str(p), 'TAK'])
                    break
                elif wynik > p:
                    # jezeli podany przypadek p jest wiekszy od wynik, czyli aktualnym elementem ciagu
                    # zapisujemy wynik jako tablice w tablicy jak wyzej, tyle ze zamiast blad piszac 'NIE'
                    # i konczymy petle przechodzac do sprawdzenia kolejnego przypadku
                    wyniki_uzytkownika.append([str(p), 'NIE'])
                    break
                else:
                    t0 = t1
                    t1 = t2
                    t2 = wynik

# petla for w zasiegu od 0 to ilosci wynikow w liscie wyniki_uzytkonwika
for i in range(0, len(wyniki_uzytkownika)):
    if wyniki_uzytkownika[i][1] == 'BLAD':
        # jezeli w przypadku okreslonym przez wyniki_uzytkownika[i], wewnatrz niego w elemencie o indexie 1
        # jest zapis 'BLAD' to wypisz 'BLAD'
        print('BLAD')
    else:
        # inaczej wypisz wynik_uzytkownika[i][0] co reprezentuje poprawny przypadek(typu int i wiekszy od 2)
        # plus \t co oznacza znak tabulacji i plus wyniki_uzytkownika[i][1] co reprezentuje TAK jezeli liczba
        # nalezy do ciagu Tribbonacciego, albo NIE jezeli nie jest
        print(f"{wyniki_uzytkownika[i][0]}\t{wyniki_uzytkownika[i][1]}")


# zeby w pelni zrozumiec kod ogarnij sobie 'tablice dwuwymiarowe python' i
# 'bledy i wyjatki python', szczegolnie to drugie
