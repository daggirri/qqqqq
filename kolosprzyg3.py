n, m = map(int, input().split())

zbior = {i : set() for i in range(1, n + 1)}

for _ in range(m):
    u, v = map(int, input().split())
    zbior[u].add(v)
    zbior[v].add(u)
    
wynik = [
    osoba for osoba in range(1, n + 1)
    if all(len(zbior[osoba]) >= len(zbior[znajomy]) for znajomy in zbior[osoba])
]

print(wynik)