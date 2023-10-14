poids = float(input("Entrez votre poids en kg: "))
taille = float(input("Entrez votre taille en m: "))

imc = poids / (taille ** 2)

print(f"Votre IMC est de {imc:.2f}.")
if imc < 16.5:
    print("Vous souffrez de famine.")
elif 16.5 <= imc < 18.5:
    print("Vous êtes en situation de maigreur.")
elif 18.5 <= imc < 25:
    print("Vous avez une corpulence normale.")
elif 25 <= imc < 30:
    print("Vous êtes en surpoids.")
elif 30 <= imc < 35:
    print("Vous souffrez d'obésité modérée.")
elif 35 <= imc < 40:
    print("Vous souffrez d'obésité sévère.")
else:
    print("Vous souffrez d'obésité morbide ou massive.")
