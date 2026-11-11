# Exemple 21 — Un modèle entraîné, c'est quoi ?
# Sortie attendue :
# {"poids": 3000, "biais": 5000}
# 30 caracteres

import json

modele = {"poids": 3000, "biais": 5000}
texte = json.dumps(modele)
print(texte)
print(len(texte), "caracteres")
