# Exemple 15 — Des exemples avec leur réponse
# Sortie attendue :
# 30 m2 -> 95000 euros
# 45 m2 -> 140000 euros
# 60 m2 -> 185000 euros

donnees = [(30, 95000), (45, 140000), (60, 185000)]
for surface, prix in donnees:
    print(f"{surface} m2 -> {prix} euros")
