# Exemple 12 — Les moindres carrés (Legendre, 1805)
# Sortie attendue :
# poids : 3.0
# biais : 20.0

surfaces = [20, 40, 60, 80]
prix = [82, 138, 198, 262]
n = len(surfaces)
mx = sum(surfaces) / n
my = sum(prix) / n
haut = sum((x - mx) * (y - my)
           for x, y in zip(surfaces, prix))
bas = sum((x - mx) ** 2 for x in surfaces)
poids = haut / bas
biais = my - poids * mx
print("poids :", poids)
print("biais :", biais)
