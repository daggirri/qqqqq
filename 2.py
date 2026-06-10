import sys
import networkx as nx
import matplotlib.pyplot as plt

# Wczytanie liczby wierzchołków (n)
n = int(input().strip())

# 1. Utworzenie pustego grafu i dodanie wierzchołków (od 0 do n-1)
G = nx.Graph()
G.add_nodes_from(range(n))

# Dodanie krawędzi: łączymy wierzchołki, których numery różnią się o dokładnie 4
for i in range(n):
    if i + 4 < n:
        G.add_edge(i, i + 4)

# 2. Rysowanie grafu z poetykietowanymi wierzchołkami (with_labels=True)
nx.draw(G, with_labels=True, node_color='lightblue', font_weight='bold')
# W systemach Moodle/CodeRunner samo wywołanie nx.draw często wystarcza, 
# aby przechwycić obraz na wyjście. Na zwykłym komputerze dodalibyśmy plt.show()

# 3. Wypisanie krawędzi uporządkowanych leksykograficznie
# Najpierw dla każdej krawędzi (pary) upewniamy się, że najmniejszy numer jest pierwszy,
# a następnie sortujemy całą listę krawędzi.
krawedzie = [tuple(sorted(e)) for e in G.edges()]
krawedzie.sort()
print(krawedzie)

# 4. Wyznaczenie składowej spójności zawierającej wierzchołek 0
# Funkcja zwraca zbiór, więc zamieniamy go na listę i sortujemy
skladowa_0 = nx.node_connected_component(G, 0)
skladowa_0_posortowana = sorted(list(skladowa_0))
print(skladowa_0_posortowana)

# 5. Sprawdzenie, czy graf jest drzewem
# Drzewo w teorii grafów musi być w pełni spójne (z każdego punktu da się dojść 
# do każdego innego) i nie posiadać cykli.
czy_drzewo = nx.is_tree(G)
print(czy_drzewo)