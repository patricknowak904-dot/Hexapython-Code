# Exemple 11 — L'explosion combinatoire
# Sortie attendue :
# 1 bouton(s) : 101 essais
# 2 bouton(s) : 10201 essais
# 3 bouton(s) : 1030301 essais
# 10 bouton(s) : 110462212541120451001 essais

valeurs = 101  # crans par bouton
for boutons in [1, 2, 3, 10]:
    essais = valeurs ** boutons
    print(boutons, "bouton(s) :", essais, "essais")
