def inserer_valeur_triee(L, val):
    position = 0
    while position < len(L) and L[position] < val:
        position += 1
    L.insert(position, val)


liste_triee = [1, 3, 5, 7, 9]
valeur_a_inserer = 4
inserer_valeur_triee(liste_triee, valeur_a_inserer)

print(liste_triee)
