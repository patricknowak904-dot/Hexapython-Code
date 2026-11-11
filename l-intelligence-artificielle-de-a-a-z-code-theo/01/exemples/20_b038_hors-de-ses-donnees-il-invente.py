# Exemple 20 — Hors de ses données, il invente
# Sortie attendue :
# 1 m2 -> 8000 euros
# 5 m2 -> 20000 euros
# 500 m2 -> 1505000 euros

def modele(surface, poids=3000, biais=5000):
    return poids * surface + biais

for s in [1, 5, 500]:
    print(f"{s} m2 -> {modele(s)} euros")
