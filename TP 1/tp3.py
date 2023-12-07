distance = float(input("Veuillez entrer la distance en kilometres : "))

temps = float(input("Veuillez entrer le temps en minutes : "))

distance_metres = distance * 1000

temps_secondes = temps * 60

vitesse_ms = round(distance_metres / temps_secondes, 2)

print("La vitesse est de", vitesse_ms, "metres par seconde.")
