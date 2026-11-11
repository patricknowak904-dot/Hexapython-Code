# Exemple 7 — Additionner les erreurs ?
# Sortie attendue :
# 0
# 0

surfaces = [20, 30, 40, 50, 60, 80]
prix = [85, 110, 140, 170, 195, 260]

def somme_erreurs(poids, biais):
    total = 0
    for s, p in zip(surfaces, prix):
        total += (poids * s + biais) - p
    return total

print(somme_erreurs(3, 20))
print(somme_erreurs(0, 160))
