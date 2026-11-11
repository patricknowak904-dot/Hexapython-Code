# Exemple 5 — Nos données : six appartements
# Sortie attendue :
# 20 m2 -> 70 000 euros
# 30 m2 -> 100 000 euros
# 45 m2 -> 140 000 euros
# 60 m2 -> 190 000 euros
# 75 m2 -> 230 000 euros
# 90 m2 -> 280 000 euros
# 6 exemples

donnees = [(20, 70), (30, 100), (45, 140),
           (60, 190), (75, 230), (90, 280)]

for surface, prix in donnees:
    print(f"{surface} m2 -> {prix} 000 euros")
print(len(donnees), "exemples")
