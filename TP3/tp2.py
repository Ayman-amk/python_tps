import math

def delta(a, b, c):
    return b**2 - 4*a*c

def NombreRacine(a, b, c):
    D = delta(a, b, c)
    if D > 0:
        return 2
    elif D == 0:
        return 1
    else:
        return 0

def AfficheNombreRacine(a, b, c):
    nb_solutions = NombreRacine(a, b, c)
    if nb_solutions == 2:
        print("Il y a 2 solutions.")
    elif nb_solutions == 1:
        print("Il y a 1 solution.")
    else:
        print("Il n'y a pas de solution réelle.")

def Racine1(a, b, c):
    D = delta(a, b, c)
    if D >= 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        return x1
    else:
        return None

def Racine2(a, b, c):
    D = delta(a, b, c)
    if D >= 0:
        x2 = (-b - math.sqrt(D)) / (2*a)
        return x2
    else:
        return None

def conversion_temps(h, m, s):
    total_secondes = h * 3600 + m * 60 + s
    return total_secondes

def temps_ecoule(h1, m1, s1, h2, m2, s2):
    temps1 = conversion_temps(h1, m1, s1)
    temps2 = conversion_temps(h2, m2, s2)
    duree = abs(temps1 - temps2)
    return duree

def conversion_distance(km, m, cm):
    distance_en_metres = km * 1000 + m + cm / 100
    return distance_en_metres

def vitesse(distance, temps):
    distance_en_metres = conversion_distance(*distance)
    temps_en_secondes = conversion_temps(*temps)
    if temps_en_secondes == 0:
        return "La vitesse est Undifined (div par zero)"
    vitesse_mps = distance_en_metres / temps_en_secondes
    return vitesse_mps

