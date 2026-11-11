# Exemple 13 — Le verdict des données cachées
# Sortie attendue :
# MSE entraînement : 4.0
# MSE test : 16.0

def modele(surface, poids, biais):
    return poids * surface + biais

def mse(xs, ys, poids, biais):
    total = 0
    for x, y in zip(xs, ys):
        total += (modele(x, poids, biais) - y) ** 2
    return total / len(xs)

train_x, train_y = [20, 40, 60, 80], [82, 138, 198, 262]
test_x, test_y = [30, 70], [114, 226]
print("MSE entraînement :", mse(train_x, train_y, 3, 20))
print("MSE test :", mse(test_x, test_y, 3, 20))
