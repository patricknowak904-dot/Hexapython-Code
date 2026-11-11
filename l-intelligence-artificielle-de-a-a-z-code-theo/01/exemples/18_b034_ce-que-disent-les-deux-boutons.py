# Exemple 18 — Ce que disent les deux boutons
# Sortie attendue :
# 125000 128000 3000
# 5000

def modele(surface, poids, biais):
    return poids * surface + biais

poids, biais = 3000, 5000
p40 = modele(40, poids, biais)
p41 = modele(41, poids, biais)
print(p40, p41, p41 - p40)
print(modele(0, poids, biais))
