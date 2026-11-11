# Exemple 4 — Deux paramètres : le poids et le biais
# Sortie attendue :
# 160
# 140
# 200

def modele(surface, poids, biais):
    return poids * surface + biais

print(modele(50, 3, 10))
print(modele(50, 2, 40))
print(modele(50, 4, 0))
