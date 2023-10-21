taille = int(input("Donner la taille de triangle : "))

for i in range(1, taille + 1):
    print("*" * i)
print("-------------------------------------")
for i in range(1, taille + 1):
    print(f"{i}" * i)