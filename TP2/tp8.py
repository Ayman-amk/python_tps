def rechercher_occurrences(L, val):
    occurrences = [i for i, x in enumerate(L) if x == val]
    return len(occurrences), occurrences

L = [1, 2, 3, 2, 4, 2, 5]
valeur_a_rechercher = 2
nombre_occurrences, indices = rechercher_occurrences(L, valeur_a_rechercher)
print(f"Nombre d'occurrences : {nombre_occurrences}")
print(f"Indices des occurrences : {indices}")
