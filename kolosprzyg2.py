import itertools

n, l, k = map(int, input().split())

str = itertools.product(range(l + 1), repeat= n)

wynik = [
    list(x) for x in str
    if sum(el**2 for el in x) == k
]

print(wynik)