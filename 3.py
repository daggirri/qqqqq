def buduj_wieze(n, aktualna_wysokosc=0, obecny_uklad=None):
    # Inicjalizacja pustej listy przy pierwszym wywołaniu funkcji
    if obecny_uklad is None:
        obecny_uklad = []
        
    # Baza rekurencji 1: Sukces - wieża ma dokładnie wysokość n
    # Od razu wypisujemy gotowy układ na ekran
    if aktualna_wysokosc == n:
        print(obecny_uklad)
        return
        
    # Baza rekurencji 2: Porażka - wieża jest za wysoka
    # Przerywamy dalsze dokładanie klocków w tej ścieżce
    if aktualna_wysokosc > n:
        return
        
    # KROK REKURENCYJNY:
    # Dokładamy klocki w porządku leksykograficznym (alfabetycznym), czyli: C, N, Z.
    # Dzięki temu gotowe układy będą wypisywane w idealnej kolejności.
    # Klocki 'C' i 'N' zwiększają wysokość o 1, a klocek 'Z' o 3.
    
    buduj_wieze(n, aktualna_wysokosc + 1, obecny_uklad + ['C'])
    buduj_wieze(n, aktualna_wysokosc + 1, obecny_uklad + ['N'])
    buduj_wieze(n, aktualna_wysokosc + 3, obecny_uklad + ['Z'])


# Wczytanie docelowej wysokości ze standardowego wejścia
n = int(input().strip())

# Uruchomienie funkcji rekurencyjnej
buduj_wieze(n)