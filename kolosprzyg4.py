import networkx as nx

# Wczytanie danych
n, m = map(int, input().split())

G = nx.Graph()

for _ in range(m):
    u, v = map(int, input().split())
    G.add_edge(u, v)

cel1, cel2 = map(int, input().split())

trasa1 = (nx.shortest_path_length(G, source= 1, target= cel1) + nx.shortest_path_length(G, source=cel1, target= cel2))
trasa2 = (nx.shortest_path_length(G, source= 1, target= cel2) + nx.shortest_path_length(G, source=cel2, target= cel1))

print(min(trasa1, trasa2))