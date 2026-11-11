"""Un exemple minuscule d'apprentissage non supervisé (b032)."""


def ecarts_successifs(valeurs_triees):
    """Écart entre chaque valeur et la suivante."""
    return [b - a for a, b in zip(valeurs_triees, valeurs_triees[1:])]


def couper_au_plus_grand_ecart(valeurs):
    """Trie les valeurs et coupe là où le trou est le plus grand.

    Aucune étiquette n'est utilisée : le programme découvre seul
    deux groupes. Renvoie (groupe_a, groupe_b).
    """
    tries = sorted(valeurs)
    if len(tries) < 2:
        return tries, []
    ecarts = ecarts_successifs(tries)
    coupe = ecarts.index(max(ecarts)) + 1
    return tries[:coupe], tries[coupe:]
