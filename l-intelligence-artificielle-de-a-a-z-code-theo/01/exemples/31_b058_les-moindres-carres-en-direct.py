# Exemple 31 — Les moindres carrés, en direct
# Sortie attendue :
# 2.0 20.0
# 120.0

surfaces = [20, 40, 60]
prix = [60, 100, 140]

n = len(surfaces)
ms = sum(surfaces) / n
mp = sum(prix) / n

num = sum((s - ms) * (p - mp) for s, p in zip(surfaces, prix))
den = sum((s - ms) ** 2 for s in surfaces)

w = num / den
b = mp - w * ms
print(w, b)
print(w * 50 + b)
