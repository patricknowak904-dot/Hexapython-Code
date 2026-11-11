# Exemple 27 — La parade : vérifier avant d'entraîner
# Sortie attendue :
# Données incohérentes : 4 surfaces, 3 prix

surfaces = [30, 45, 60, 80]
prix = [100000, 145000, 190000]
if len(surfaces) != len(prix):
    print("Données incohérentes :", len(surfaces),
          "surfaces,", len(prix), "prix")
