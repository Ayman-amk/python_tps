n1 = int(input("Donner une valeur pour le premier nombre : "))
n2 = int(input("Donner une valeur pour le deuxieme nombre : "))

if (n1 > 0 and n2 > 0) or (n1 < 0 and n2 < 0):
    print("Le résultat est positif")
elif (n1 < 0 < n2) or (n1 > 0 > n2):
    print("Le résultat est négatif")
elif n1 == 0 or n2 == 0:
    print("l'un des nombre est null")
