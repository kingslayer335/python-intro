import math
import random
import time

list_a = ("kwadrat", "trojkat", "romb")
list_b = ("kolo", "szescian", "rownoleglobok")

# https://docs.python.org/3/library/functions.html#zip
# Funkcja zip() zwraca iterator, który generuje krotki utworzone z przekazanych do niej elementów.
# Krotki zawierają elementy z tych samych indeksów w każdej sekwencji.
zipped_list = zip(list_a, list_b)
print(('\nUzycie funkcji zip na dwoch listach: '),zipped_list,("\n"))

listed_zip = list(zipped_list)
print(('Zip zmieniony w liste: '),listed_zip,("\n"))

# https://docs.python.org/3/library/functions.html#enumerate
# Funkcja enumerate() zwraca iterator, który generuje krotki zawierające indeksy i odpowiadające im elementy.
# Pozwala łatwo iterować po elementach wraz z ich indeksami.
print('Enumerowana lista:')
for index, pair in enumerate(listed_zip):
    print(f"{index}: {pair}")
print("\n")

# https://docs.python.org/3/library/functions.html#sorted
# Funkcja sorted() służy do sortowania elementów iterowalnych, takich jak listy, krotki czy ciągi znaków. 
# Zwraca nową posortowaną listę, pozostawiając oryginalną sekwencję bez zmian.
list_c  = [25, 64, 16, 4, 36, 100, 9, 81, 49]
sorted_list = sorted(list_c)
print('Posortowana lista kwadratow liczb:\n',sorted_list,("\n"))

# https://docs.python.org/3/library/math.html
# Moduł math zawiera wiele funkcji które pozwalają na wykonywanie zaawansowanych operacji matematycznych.
# Funkcje działają glownie na liczbach rzeczywistych (float, int).
# Podstawowe funkcje to: sqrt(), pow(), ceil(), floor(), sin(), cos(), tan().

# https://docs.python.org/3/library/random.html
# Funkcje z modułu random służą do generowania liczb losowych i wykonywania losowych operacji.
# Podstawowe funkcje to: random(), randint(), choice(), shuffle().

# W tym przypadku wylosowana zostaje liczba z listy 'list_c', a następnie obliczany jest jej pierwiastek.
y= math.sqrt(random.choice(list_c))
print(('Pierwiastek z losowej liczby z listy kwadratow: '),y,("\n"))

# https://docs.python.org/3/library/time.html
# Moduł time zawiera funkcje związane z operacjami na czasie, takie jak pomiar czasu, opóźnienia, czy formatowanie daty i godziny.
# Jest przydatny do pracy z czasem w różnych formatach oraz do mierzenia wydajności kodu.
# Podstawowe funkcje to: time(), sleep(), strftime().

# W tym przypadku wyświetlana jest aktualna godzina w formacie HH:MM:SS.
current_time = time.strftime("%H:%M:%S")
print(('Aktualna godzina:'), current_time, ("\n"))

# https://docs.python.org/3/library/exceptions.html#IndexError
# Wyjątek IndexError jest wywolywany, gdy próbujemy odwołać się do elementu listy który nie istnieje.
# W tym przypadku spróbowałem odwołać się do losowego elementu z pustej listy.
try:
    empty_list = []
    x = random.choice(empty_list)
    print(x)
except IndexError as e:
    print("IndexError: ",e,("\n"))
    
# https://docs.python.org/3/library/exceptions.html#ValueError
# Wyjątek ValueError jest wywolywany, gdy funkcja otrzymuje argument, który ma poprawny typ, ale niepoprawną wartość.
# W tym przypadku spróbowałem obliczyć pierwiastek z liczby ujemnej.
    
try:
    y = math.sqrt(-25)
    print(('Pierwiastek z liczby: '), y)
except ValueError as e:
    print("ValueError: ",e,("\n"))

# https://docs.python.org/3/library/exceptions.html#ZeroDivisionError
# Wyjątek ZeroDivisionError jest wywolywany, gdy próbujemy podzielić przez zero.

try:
    z = 10 / 0
    print(z)
except ZeroDivisionError as e:
    print("ZeroDivisionError: ",e,("\n"))