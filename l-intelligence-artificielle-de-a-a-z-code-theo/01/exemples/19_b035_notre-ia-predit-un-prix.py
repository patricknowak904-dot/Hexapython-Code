# Exemple 19 — Notre IA prédit un prix
# Sortie attendue :
# 25 m2 -> 80000 euros
# 52 m2 -> 161000 euros
# 90 m2 -> 275000 euros

def modele(surface, poids=3000, biais=5000):
    return poids * surface + biais

for s in [25, 52, 90]:
    print(f"{s} m2 -> {modele(s)} euros")
