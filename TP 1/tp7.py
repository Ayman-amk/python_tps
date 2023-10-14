nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))

operation = input("Choisissez une opération (+, -, *, /) : ")

if operation == "+":
    resultat = nombre1 + nombre2
elif operation == "-":
    resultat = nombre1 - nombre2
elif operation == "*":
    resultat = nombre1 * nombre2
elif operation == "/":
    if nombre2 == 0:
        print("Erreur : Division par zéro n'est pas autorisée.")
    else:
        resultat = nombre1 / nombre2
else:
    print("Opération non reconnue.")

if operation in ('+', '-', '*', '/'):
    print(f"Le résultat de {nombre1} {operation} {nombre2} est égal à {resultat}.")
