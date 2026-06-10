import itertools

n, k = map(int, input().split())

perms = itertools.permutations(range(1, n + 1), k)

wynik = [
    list(p) for p in perms
    if all(abs(p[i] - p[i + 1]) != 1 for i in range (k - 1))
]

print(wynik)