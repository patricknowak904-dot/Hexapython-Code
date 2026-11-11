# Exemple 29 — Solution : la recherche à trois boutons
# Sortie attendue :
# Essais : 1386
# Meilleur réglage : (3, 5, 10)
# Coût : 0.0

donnees = [(30, 1, 105), (45, 2, 155), (60, 3, 205),
           (80, 3, 265), (100, 4, 330)]

def modele(s, p, w1, w2, b):
    return w1 * s + w2 * p + b

def mse(w1, w2, b):
    total = 0
    for s, p, prix in donnees:
        total += (modele(s, p, w1, w2, b) - prix) ** 2
    return total / len(donnees)

meilleur = None
essais = 0
for w1 in range(6):
    for w2 in range(11):
        for b in range(21):
            essais += 1
            cout = mse(w1, w2, b)
            if meilleur is None or cout < meilleur[0]:
                meilleur = (cout, w1, w2, b)

print("Essais :", essais)
print("Meilleur réglage :", meilleur[1:])
print("Coût :", meilleur[0])
