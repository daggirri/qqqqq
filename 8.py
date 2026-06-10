import sys

def generuj_ciagi(n, obecny_ciag=None, licznik_zer=0):
    # Inicjalizacja pustej listy przy pierwszym wywołaniu
    if obecny_ciag is None:
        obecny_ciag = []
        
    # 1. Baza rekurencji: ciąg osiągnął docelową długość n
    if len(obecny_ciag) == n:
        # Musimy jeszcze upewnić się, że jeśli ciąg kończy się zerami,
        # to ta ostatnia seria też jest parzystej długości.
        if licznik_zer % 2 == 0:
            print(obecny_ciag)
        return

    # 2. Krok rekurencyjny (budowanie ciągu leksykograficznie: 0, 1, 2)
    
    # OPCJA A: Zawsze możemy dołożyć '0' do ciągu.
    # Powoduje to wydłużenie aktualnej serii zer o 1.
    generuj_ciagi(n, obecny_ciag + [0], licznik_zer + 1)
    
    # OPCJE B i C: Możemy dołożyć '1' lub '2' TYLKO wtedy, gdy
    # dotychczasowa seria zer (jeśli jakaś jest) ma parzystą długość.
    # Wstawienie 1 lub 2 zamyka serię zer, więc musi ona być poprawna.
    if licznik_zer % 2 == 0:
        # Skoro wstawiamy cyfrę inną niż 0, licznik zer w nowym kroku resetujemy do 0.
        generuj_ciagi(n, obecny_ciag + [1], 0)
        generuj_ciagi(n, obecny_ciag + [2], 0)

# Wczytanie liczby n ze standardowego wejścia
wejscie = sys.stdin.read().split()
if wejscie:
    n = int(wejscie[0])
    # Wywołanie głównej funkcji
    generuj_ciagi(n)