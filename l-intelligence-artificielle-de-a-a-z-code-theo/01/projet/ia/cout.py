"""Les juges : des fonctions de coût qui notent un réglage par un seul nombre."""

from ia.modele import modele


def somme_erreurs(xs, ys, poids, biais):
    """Premier juge, naïf (b012) : la somme des erreurs.

    Défaut : les erreurs positives et négatives s'annulent !
    """
    total = 0
    for x, y in zip(xs, ys):
        total += modele(x, poids, biais) - y
    return total


def mse_valeurs(vrais, predits):
    """Erreur quadratique moyenne entre vraies valeurs et prédictions.

    Une liste vide provoque volontairement une ZeroDivisionError (b047) :
    mieux vaut une erreur bruyante qu'un chiffre faux et silencieux.
    """
    total = 0
    for v, p in zip(vrais, predits):
        total += (v - p) ** 2
    return total / len(vrais)


def mse(xs, ys, poids, biais):
    """MSE du modèle linéaire (poids, biais) sur les exemples (xs, ys)."""
    predits = [modele(x, poids, biais) for x in xs]
    return mse_valeurs(ys, predits)


def rmse(xs, ys, poids, biais):
    """Racine de la MSE : l'erreur typique, dans l'unité des prix (b026)."""
    return mse(xs, ys, poids, biais) ** 0.5


def mae_valeurs(vrais, predits):
    """Écart absolu moyen (b015) : on retire simplement le signe."""
    total = 0
    for v, p in zip(vrais, predits):
        total += abs(v - p)
    return total / len(vrais)


def mse_predicteur(predire, exemples):
    """MSE d'une fonction de prédiction quelconque sur des couples (x, y)."""
    erreurs = [(predire(s) - p) ** 2 for s, p in exemples]
    return sum(erreurs) / len(erreurs)
