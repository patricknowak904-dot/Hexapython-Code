# Exemple 8 — La fonction de coût MSE
# Sortie attendue :
# 8.3
# 3308.3

surfaces = [20, 30, 40, 50, 60, 80]
prix = [85, 110, 140, 170, 195, 260]

def mse(poids, biais):
    total = 0
    for s, p in zip(surfaces, prix):
        erreur = (poids * s + biais) - p
        total += erreur ** 2
    return total / len(prix)

print(round(mse(3, 20), 1))
print(round(mse(0, 160), 1))
