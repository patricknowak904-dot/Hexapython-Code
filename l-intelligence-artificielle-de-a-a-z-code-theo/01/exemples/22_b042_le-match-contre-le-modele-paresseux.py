# Exemple 22 — Le match contre le modèle paresseux
# Sortie attendue :
# modele bete : 44060 euros
# notre IA : 1581 euros

train = [(20, 65500), (35, 108500),
         (50, 156500), (65, 199500)]
test = [(30, 96000), (60, 183000)]
moyenne = sum(p for _, p in train) / len(train)

def mse(predire):
    erreurs = [(predire(s) - p) ** 2 for s, p in test]
    return sum(erreurs) / len(erreurs)

bete = mse(lambda s: moyenne)
ia = mse(lambda s: 3000 * s + 5000)
print("modele bete :", round(bete ** 0.5), "euros")
print("notre IA :", round(ia ** 0.5), "euros")
