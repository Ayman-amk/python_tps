import random


def jeu_deviner_nombre():
    n = random.randint(1, 100)
    nbEassais = 0

    print("On va jouer à un petit jeu, je vais générer un nombre entre 1 et 100 et tu vas le deviner en 7 essais.")

    while nbEassais < 7:
        essai = input(">>> ")

        if not essai.isdigit():
            print("Oups, vous avez saisi un nombre en dehors de l'intervalle.")
            continue

        essai = int(essai)

        if essai < 1 or essai > 100:
            print("Oups, vous avez saisi un nombre en dehors de l'intervalle.")
        elif essai < n:
            print("Oups, entrez un nombre plus grand !")
            nbEassais += 1
        elif essai > n:
            print("Oups, entrez un nombre plus petit !")
            nbEassais += 1
        else:
            nbEassais += 1
            print(f"Bravo, {essai} est le nombre que j'ai choisi. Vous l'avez deviné en {nbEassais} essais.")
            break
    else:
        print("J'ai gagné, je suis le meilleur. Le nombre que j'ai choisi est", n)
    print("Au revoir!")


jeu_deviner_nombre()
