import sys
# Pobranie biblioteki z archiwum platformy
sys.path.insert(0, 'networkx.zip')
import networkx as nx
import matplotlib.pyplot as plt

# Wczytanie n i m
n, m = map(int, input().split())

# 1. Tworzenie pełnego grafu dwudzielnego K_{n,m}
G = nx.Graph()
V1 = range(0, n)
V2 = range(n, n + m)

G.add_nodes_from(V1, bipartite=0)
G.add_nodes_from(V2, bipartite=1)

# Dodanie wszystkich możliwych krawędzi między V1 a V2
for u in V1:
    for v in V2:
        G.add_edge(u, v)

# Rysowanie grafu dwudzielnego (NetworkX posiada gotowy układ dla tego typu grafów)
pos = nx.bipartite_layout(G, V1)
nx.draw(G, pos, with_labels=True, node_color='lightblue')
# plt.show() # Odkomentuj, jeśli testujesz poza platformą

# 2. Wypisanie krawędzi
krawedzie = [tuple(sorted((u, v))) for u, v in G.edges()]
krawedzie.sort()
print(krawedzie)

# 3. Wypisanie krawędzi cięcia (mostów)
mosty = [tuple(sorted((u, v))) for u, v in nx.bridges(G)]
mosty.sort()
print(mosty)

# 4. Sprawdzenie, czy graf jest półeulerowski, ale NIE eulerowski
# nx.is_eulerian(G) sprawdza, czy ma cykl Eulera (czyli czy jest eulerowski)
# nx.has_eulerian_path(G) sprawdza, czy ma przynajmniej ścieżkę Eulera (czyli może być eulerowski lub półeulerowski)
# Zatem: (ma ścieżkę) AND (NIE ma cyklu) = jest półeulerowski, ale nie eulerowski.
czy_poleulerowski = nx.has_eulerian_path(G) and not nx.is_eulerian(G)
print(czy_poleulerowski)