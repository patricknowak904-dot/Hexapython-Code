# Exemple 30 — Le modèle et son juge
# Sortie attendue :
# 2 20 0.0
# 2 30 100.0

def modele(s, w, b):
    return w * s + b

def mse(vrais, preds):
    n = len(vrais)
    return sum((v - p) ** 2 for v, p in zip(vrais, preds)) / n

surfaces = [20, 40, 60]
prix = [60, 100, 140]

for w, b in [(2, 20), (2, 30)]:
    preds = [modele(s, w, b) for s in surfaces]
    print(w, b, mse(prix, preds))
