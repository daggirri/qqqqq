import itertools

# Wczytanie wejścia, podział po przecinku i usunięcie zbędnych spacji
pracownicy = [p.strip() for p in input().split(',')]

# 1. Ćwiczenie pierwsze: 3-osobowe grupy
# combinations tworzy wszystkie unikalne 3-elementowe zestawy
grupy_3_osobowe = list(itertools.combinations(pracownicy, 3))
print(grupy_3_osobowe)

# 2. Ćwiczenie drugie: podział na 2 niepuste zespoły
# Wykorzystujemy załadowaną przez platformę funkcję set_partitions 
# Podajemy argument 2, bo chcemy dokładnie 2 zespoły
podzial_na_2 = list(set_partitions(pracownicy, 2))
print(podzial_na_2)