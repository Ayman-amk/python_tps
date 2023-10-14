def calculer_salaire(grade, htravail):
    tarif = {
        'A': {'th': 200, 'prime': 1000, 'hprime': 20},
        'B': {'th': 150, 'prime': 800, 'hprime': 20},
        'C': {'th': 120, 'prime': 500, 'hprime': 15},
        'D': {'th': 100, 'prime': 350, 'hprime': 15},
        'E': {'th': 80, 'prime': 100, 'hprime': 10}
    }

    if grade in tarif:
        th = tarif[grade]['th']
        prime = tarif[grade]['prime']
        hprime = tarif[grade]['hprime']

        heures_normales = htravail % hprime
        primes = (htravail // hprime) * prime

        salaire = (th * htravail) + primes
        return salaire
    else:
        return "Grade inconnu x-("

grade = input("Entrez le grade de l'employé (A, B, C, D, E) : ")
htravail = int(input("Entrez le nombre d'heures travaillées : "))

salaire = calculer_salaire(grade, htravail)

if isinstance(salaire, str):
    print(salaire)
else:
    print(f"Le salaire de l'employé est de {salaire} DH.")
