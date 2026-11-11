# Exemple 10 — Chercher le meilleur réglage
# Sortie attendue :
# poids : 3 biais : 20
# coût entraînement : 6.25
# coût test : 12.5

surfaces = [20, 30, 40, 50, 60, 80]
prix = [85, 110, 140, 170, 195, 260]
train_s, train_p = surfaces[:4], prix[:4]
test_s, test_p = surfaces[4:], prix[4:]

def mse(poids, biais, xs, ys):
    total = 0
    for x, y in zip(xs, ys):
        total += (poids * x + biais - y) ** 2
    return total / len(ys)

meilleur = None
for poids in range(6):
    for biais in range(0, 60, 10):
        cout = mse(poids, biais, train_s, train_p)
        if meilleur is None or cout < meilleur[0]:
            meilleur = (cout, poids, biais)

cout, poids, biais = meilleur
print("poids :", poids, "biais :", biais)
print("coût entraînement :", cout)
print("coût test :", mse(poids, biais, test_s, test_p))
