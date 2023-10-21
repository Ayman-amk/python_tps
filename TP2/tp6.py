liste = input("Entrez une liste de nombres (séparés par des espaces) : ")
liste = liste.split()  # Diviser la chaîne d'entrée en une liste de nombres

liste = [int(x) for x in liste]

nombre_a_supprimer = int(input("Entrez le nombre a supprimer : "))

liste_sans_occurrences = [x for x in liste if x != nombre_a_supprimer]

print("Liste sans les occurrences de", nombre_a_supprimer, ":", liste_sans_occurrences)
