n = int(input("Veuillez entrer un nombre : "))

heures = n // 3600
n %= 3600

minutes = n // 60
secondes = n % 60

print(f"{heures}h {minutes}min {secondes}sec")
