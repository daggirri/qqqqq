import itertools

# Wczytanie liczby pytań (n)
n = int(input().strip())

# Dozwolone odpowiedzi
odpowiedzi = ['A', 'B', 'C']

# 1. Wszystkie możliwe konfiguracje (iloczyn kartezjański)
# repeat=n oznacza "losuj po jednej odpowiedzi n razy"
wszystkie_kombinacje = list(itertools.product(odpowiedzi, repeat=n))

# Zamieniamy je na listę krotek dla zgodności z wyjściem w zadaniu
# Wypisujemy od razu (itertools.product domyślnie generuje w porządku leksykograficznym)
print(wszystkie_kombinacje)

# 2. Konfiguracje zawierające co najmniej raz literę 'B'
# Filtrujemy wygenerowaną przed chwilą listę za pomocą wyrażenia składanego
z_litera_b = [kombinacja for kombinacja in wszystkie_kombinacje if 'B' in kombinacja]

# Wypisujemy wynik (porządek pozostaje prawidłowy, bo wyciągamy je z posortowanej już listy)
print(z_litera_b)