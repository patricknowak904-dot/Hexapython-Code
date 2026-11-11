# Exemple 26 — Piège n°3 : zip qui coupe sans prévenir
# Sortie attendue :
# 3
# (60, 190000)

surfaces = [30, 45, 60, 80]
prix = [100000, 145000, 190000]
paires = list(zip(surfaces, prix))
print(len(paires))
print(paires[-1])
