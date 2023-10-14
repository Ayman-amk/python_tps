nombre_articles = 3

total_facture = 0

for i in range(nombre_articles):
    nom_article = input(f"Entrez le nom de l'article {i + 1} : ")
    prix_article = float(input(f"Entrez le prix de l'article {i + 1} : "))
    quantite_article = int(input(f"Entrez la quantité de l'article {i + 1} : "))

    montant_ht = prix_article * quantite_article
    montant_ttc = montant_ht + (montant_ht * 0.2)

    total_facture += montant_ttc

    print(f"Montant TTC pour {nom_article} : {montant_ttc:.2f} MAD")

print(f"Montant total de la facture : {total_facture:.2f} MAD")
