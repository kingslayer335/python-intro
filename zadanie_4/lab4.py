# Piotr Artym, 122212
# https://github.com/kingslayer335/python-intro/tree/main/zadanie_4

import numpy as np
import pymcdm as pm

def main():
    # przykładowe dane
    criteria_units = ['zł', 'r.', '/10', '/10']
    criteria_names = ['Cena', 'Rok produkcji', 'Moc', 'Ekologia']
    alias = ["Toyota Camry", "Honda Civic", "Volkswagen Golf"]

    matrix = np.array([
        [15000, 2014, 7, 4],  # Toyota Camry
        [10500, 2008, 7, 3],  # Honda Civic
        [12000, 2007, 8, 2]  # Volkswagen Golf
    ])

    # wagi kryteriów używając metody RANCOM
    rancom = pm.weights.subjective.RANCOM(scoring=[5, 3, 6, 2])
    weights = rancom()

    # minimalizacja ceny i czasu dostawy, maksymalizacja jakości i bezpieczeństwa
    types = np.array([-1, 1, 1, 1])

    # utworzenie problemu
    create_problem(matrix, weights, types, criteria_names, criteria_units)

    # zakresy wartosci min-max dla funkcji SPOTIS
    bounds = np.array([
    [7000, 16000],
    [2001, 2024],
    [1, 10],
    [1, 10]
    ])

    # zastosowanie metody SPOTIS i wyświetlenie wyników
    func(matrix, weights, types, alias, pm.methods.SPOTIS, 'SPOTIS', bounds)
   
    # zastosowanie metody TOPSIS i wyświetlenie wyników
    func(matrix, weights, types, alias, pm.methods.TOPSIS, 'TOPSIS')
   
    # zastosowanie metody VIKOR i wyświetlenie wyników
    func(matrix, weights, types, alias, pm.methods.VIKOR, 'VIKOR')


# użycie modułu pymcdm.io do wygenerowania opisowej tabeli z kryteriami
def create_problem(matrix, weights, types, criteria_names, criteria_units):
    problem = pm.io.MCDA_problem(matrix=matrix,
                             weights=weights,
                             types=types,
                             criteria_names=criteria_names,
                             criteria_units=criteria_units)
    print(problem, '\n')

# funkcja do obliczenia wyników i wyświetlenia ich, podaje w argumencie nazwę funkcji
# i jej alias, w celu wyświetlenia wyników dla różnych metod
def func(matrix, weights, types, alias, function, function_name, *args):
    function = function(*args)
    pref = function(matrix, weights, types)
    rank = function.rank(pref)
    print(function_name,'ranking:')
    sort_results(pref, rank, alias)
    print()


# sortowanie wyników
def sort_results(pref, rank, alias):
    sorted_indices = np.argsort(rank)
    for i, idx in enumerate(sorted_indices, start=1):
        print(f"{i}. {alias[idx]} (wynik: {pref[idx]:.4f})")

if __name__ == '__main__': 
    main()