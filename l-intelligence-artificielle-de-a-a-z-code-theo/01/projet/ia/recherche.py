"""Chercher les meilleurs paramètres : force brute et moindres carrés."""

from ia.cout import mse
from ia.modele import modele_deux_entrees


def recherche_grille(xs, ys, poids_possibles, biais_possibles):
    """Force brute (b017) : essaie chaque combinaison (poids, biais).

    Renvoie ((coût, poids, biais), nombre_d_essais).
    """
    meilleur = None
    essais = 0
    for poids in poids_possibles:
        for biais in biais_possibles:
            essais += 1
            cout = mse(xs, ys, poids, biais)
            # On range coût et réglage dans un même tuple : tout est mis à jour d'un coup.
            if meilleur is None or cout < meilleur[0]:
                meilleur = (cout, poids, biais)
    return meilleur, essais


def moindres_carres(xs, ys):
    """Formule directe de Legendre (1805) pour la meilleure droite (b023).

    Le poids est le rapport entre la covariation surface/prix et la
    variation de la surface seule ; le biais fait passer la droite par
    le centre de gravité du nuage de points.
    """
    if len(xs) != len(ys):
        raise ValueError("xs et ys n'ont pas la même longueur")
    if len(xs) < 2:
        raise ValueError("il faut au moins deux exemples")
    mx = sum(xs) / len(xs)
    my = sum(ys) / len(ys)
    haut = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    bas = sum((x - mx) ** 2 for x in xs)
    if bas == 0:
        raise ValueError("toutes les surfaces sont identiques : pente indéfinie")
    poids = haut / bas
    return poids, my - poids * mx


def mse_trois_boutons(donnees, w1, w2, b):
    """MSE du modèle (surface, pièces) sur des triplets (s, p, prix)."""
    total = 0
    for s, p, prix in donnees:
        total += (modele_deux_entrees(s, p, w1, w2, b) - prix) ** 2
    return total / len(donnees)


def recherche_grille_3d(donnees, w1_possibles, w2_possibles, b_possibles):
    """Solution du défi (b054) : trois boucles imbriquées, comme un cadenas."""
    meilleur = None
    essais = 0
    for w1 in w1_possibles:
        for w2 in w2_possibles:
            for b in b_possibles:
                essais += 1
                cout = mse_trois_boutons(donnees, w1, w2, b)
                if meilleur is None or cout < meilleur[0]:
                    meilleur = (cout, w1, w2, b)
    return meilleur, essais


def nombre_essais(crans_par_bouton, boutons):
    """Nombre de combinaisons à tester (b022) : l'explosion combinatoire."""
    return crans_par_bouton ** boutons
