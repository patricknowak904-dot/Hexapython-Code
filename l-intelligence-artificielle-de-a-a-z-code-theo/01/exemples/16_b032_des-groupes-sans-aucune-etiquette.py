# Exemple 16 — Des groupes, sans aucune étiquette
# Sortie attendue :
# Groupe A : [22, 25, 28]
# Groupe B : [70, 75, 81]

surfaces = [22, 25, 28, 70, 75, 81]
surfaces.sort()
ecarts = [b - a for a, b in zip(surfaces, surfaces[1:])]
coupe = ecarts.index(max(ecarts)) + 1
print("Groupe A :", surfaces[:coupe])
print("Groupe B :", surfaces[coupe:])
