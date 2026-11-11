"""Les modèles : des fonctions dont les paramètres sont des boutons à régler."""


def modele_fixe(surface):
    """Premier modèle de l'épisode (b002) : réglages écrits à la main.

    Le 3 et le 10 ont été choisis au hasard par un humain.
    """
    return 3 * surface + 10


def modele(surface, poids, biais):
    """Régression linéaire : prix = poids * surface + biais.

    - poids : la pente, ce que rapporte chaque mètre carré en plus ;
    - biais : le point de départ, le prix pour zéro mètre carré.
    """
    return poids * surface + biais


def modele_deux_entrees(surface, pieces, p1, p2, b):
    """Modèle à trois boutons (b044) : surface et nombre de pièces."""
    return p1 * surface + p2 * pieces + b


def predire_tous(surfaces, poids, biais):
    """Applique le modèle linéaire à une liste de surfaces."""
    return [modele(s, poids, biais) for s in surfaces]
