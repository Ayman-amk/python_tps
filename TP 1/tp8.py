notes = []
coefficients = []

for i in range(4):
    note = float(input(f"Entrez la note {i + 1} : "))
    coefficient = float(input(f"Entrez le coefficient de la note {i + 1} : "))
    notes.append(note)
    coefficients.append(coefficient)

somme_notes = sum([notes[i] * coefficients[i] for i in range(4)])
somme_coefficients = sum(coefficients)
moyenne = somme_notes / somme_coefficients

print(f"Moyenne Geenrale : {moyenne:.2f}")

if moyenne >= 10:
    print("Semestre validé :-)")
elif moyenne >= 7:
    print("Rattrapage :-| ")
else:
    print("Semestre non validé :-(")
