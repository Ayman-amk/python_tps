L = [1, 2, 5, 8, 6, 2, 5, 9, 1, 8, 8]

nouvelle_liste = []

for element in L:
    if element not in nouvelle_liste:
        nouvelle_liste.append(element)

L = nouvelle_liste

print(L)
