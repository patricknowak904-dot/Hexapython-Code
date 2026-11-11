# Exemple 6 — Un réglage à l'épreuve des vrais prix
# Sortie attendue :
# 20 70 80 10
# 30 100 100 0
# 45 140 130 -10
# 60 190 160 -30
# 75 230 190 -40
# 90 280 220 -60

donnees = [(20, 70), (30, 100), (45, 140),
           (60, 190), (75, 230), (90, 280)]

def modele(surface, poids, biais):
    return poids * surface + biais

for surface, prix in donnees:
    prediction = modele(surface, 2, 40)
    print(surface, prix, prediction, prediction - prix)
