# Exemple 14 — Notre IA complète, en Python pur
# Sortie attendue :
# Réglage : 3.0 20.0
# MSE test : 16.0
# 55 m² : 185.0 k€

# Une IA en Python pur : prix d'un appartement
train_x = [20, 40, 60, 80]
train_y = [82, 138, 198, 262]
test_x, test_y = [30, 70], [114, 226]

def modele(x, poids, biais):
    return poids * x + biais

def mse(xs, ys, poids, biais):
    erreurs = [(modele(x, poids, biais) - y) ** 2
               for x, y in zip(xs, ys)]
    return sum(erreurs) / len(erreurs)

def entrainer(xs, ys):
    mx = sum(xs) / len(xs)
    my = sum(ys) / len(ys)
    haut = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    bas = sum((x - mx) ** 2 for x in xs)
    poids = haut / bas
    return poids, my - poids * mx

poids, biais = entrainer(train_x, train_y)
print("Réglage :", poids, biais)
print("MSE test :", mse(test_x, test_y, poids, biais))
print("55 m² :", modele(55, poids, biais), "k€")
