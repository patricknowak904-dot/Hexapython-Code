"""Petite boîte à outils d'IA en Python pur (épisode 1 d'HexaPython).

Modules :
- modele       : les fonctions paramétrées (nos machines à boutons)
- cout         : les juges (somme des erreurs, MSE, RMSE...)
- recherche    : force brute et moindres carrés
- donnees      : les jeux de données de l'épisode et des garde-fous
- non_supervise: un regroupement minuscule, sans étiquettes
- sauvegarde   : enregistrer un modèle au format JSON
"""


def titre(numero, texte):
    """Affiche un titre de section bien visible dans le terminal."""
    print()
    print("=" * 66)
    print(f"[{numero}] {texte}")
    print("=" * 66)
