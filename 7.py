import sys

# Wczytanie liczby n
n = int(sys.stdin.read().split()[0])

# 1. Przygotowanie puli elementów do ciągu Prüfera
# Zgodnie z naszą analizą: dwie 0, dwie 2 i (n-6) jedynek
elementy = [0, 0, 2, 2] + [1] * (n - 6)

# Wykorzystujemy załadowaną wcześniej funkcję do stworzenia 
# wszystkich unikalnych ciągów Prüfera dla tych klocków
sekwencje_prufera = list(distinct_permutations(elementy))

wszystkie_drzewa = []

# 2. Dekodowanie każdego ciągu Prüfera na listę krawędzi
for prufer in sekwencje_prufera:
    # Obliczamy stopnie wierzchołków na starcie (+1 dla każdego wierzchołka)
    stopnie = [1] * n
    for p in prufer:
        stopnie[p] += 1
        
    krawedzie = []
    
    # Standardowy algorytm dekodowania kodu Prüfera
    for p in prufer:
        # Szukamy najmniejszego wierzchołka będącego liściem (stopień 1)
        for i in range(n):
            if stopnie[i] == 1:
                lisc = i
                break
        
        # Zapisujemy krawędź zawsze od mniejszego do większego wierzchołka
        u, v = min(lisc, p), max(lisc, p)
        krawedzie.append((u, v))
        
        # Odlączamy liść od drzewa (zmniejszamy stopnie obu wierzchołków)
        stopnie[lisc] -= 1
        stopnie[p] -= 1
        
    # Na koniec zostają dokładnie dwa niepołączone wierzchołki o stopniu 1
    ostatnie_dwa = [i for i in range(n) if stopnie[i] == 1]
    u, v = min(ostatnie_dwa[0], ostatnie_dwa[1]), max(ostatnie_dwa[0], ostatnie_dwa[1])
    krawedzie.append((u, v))
    
    # Sortujemy krawędzie wewnątrz drzewa leksykograficznie
    krawedzie.sort()
    wszystkie_drzewa.append(krawedzie)

# 3. Sortowanie końcowe i wypisanie
# Sortujemy listę wszystkich wygenerowanych drzew leksykograficznie
wszystkie_drzewa.sort()

# Wypisujemy każde wygenerowane drzewo w osobnej linijce
for drzewo in wszystkie_drzewa:
    print(drzewo)