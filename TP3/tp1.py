def somme(m, n):
    if m == n:
        return m
    else:
        return m + somme(m + 1, n)

resultat = somme(5, 8)
print(resultat)
