# Exemple 23 — Un modèle à deux entrées
# Sortie attendue :
# 170000
# 270000

def modele(surface, pieces, p1, p2, b):
    return p1 * surface + p2 * pieces + b

print(modele(50, 2, 3000, 5000, 10000))
print(modele(80, 4, 3000, 5000, 10000))
