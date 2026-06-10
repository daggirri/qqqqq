import sys
import networkx as nx

# 1. Wczytanie liczby miejsc (n) i liczby szlaków (m)
n = int(input().strip())
m = int(input().strip())

# Wczytanie linii z miejscami (np. "A, B, C, D, E, F")
# Dzielimy tekst po przecinku i usuwamy białe znaki (spacje) za pomocą strip()
miejsca = [x.strip() for x in input().split(',')]

# Janka mieszka w pierwszym miejscu na liście - to nasz punkt startowy
start = miejsca[0]

# 2. Utworzenie pustego grafu i dodanie dróg
G = nx.Graph()

for _ in range(m):
    u, v = input().split()
    G.add_edge(u, v)

# 3. Szukanie najkrótszych ścieżek za pomocą wbudowanej funkcji
# Zwraca słownik w formacie {miejsce: odległość_od_startu}
odleglosci = nx.single_source_shortest_path_length(G, start)

# 4. Wybranie miejsc, do których da się dojść w max 3 godziny
wynik = [
    miejsce for miejsce, czas in odleglosci.items()
    # Czas musi być <= 3, ale też > 0 (żeby nie wypisać punktu startowego)
    if 0 < czas <= 3
]

# 5. Uporządkowanie leksykograficzne (alfabetyczne) i wypisanie wyniku
wynik.sort()
print(wynik)