"""Les données de l'épisode, et quelques garde-fous."""

import csv
from pathlib import Path

# Dossier data/ du projet, calculé à partir de ce fichier (jamais en dur).
DOSSIER_DATA = Path(__file__).resolve().parent.parent / "data"

# Données du juge (b012 à b017), prix en milliers d'euros.
SURFACES_JUGE = [20, 30, 40, 50, 60, 80]
PRIX_JUGE = [85, 110, 140, 170, 195, 260]

# Données arrondies (b023 à b027), prix en milliers d'euros.
TRAIN_X = [20, 40, 60, 80]
TRAIN_Y = [82, 138, 198, 262]
TEST_X = [30, 70]
TEST_Y = [114, 226]

# Ventes en euros (b035 à b042) : le réglage 3000 / 5000 en découle.
VENTES_TRAIN = [(20, 65500), (35, 108500), (50, 156500), (65, 199500)]
VENTES_TEST = [(30, 96000), (60, 183000)]

# Défi (b052 à b054) : (surface, pièces, prix en milliers d'euros).
DEFI = [(30, 1, 105), (45, 2, 155), (60, 3, 205),
        (80, 3, 265), (100, 4, 330)]


def charger_appartements(nom_fichier="appartements.csv"):
    """Lit le CSV des six appartements (b007) : liste de (surface, prix)."""
    chemin = DOSSIER_DATA / nom_fichier
    donnees = []
    with open(chemin, encoding="utf-8", newline="") as fichier:
        for ligne in csv.DictReader(fichier):
            donnees.append((int(ligne["surface_m2"]), int(ligne["prix_k_euros"])))
    return donnees


def separer_colonnes(couples):
    """Transforme une liste de couples (x, y) en deux listes xs et ys."""
    xs = [x for x, _ in couples]
    ys = [y for _, y in couples]
    return xs, ys


def decouper(xs, ys, n_train):
    """Découpe en entraînement (les n_train premiers) et test (le reste)."""
    return xs[:n_train], ys[:n_train], xs[n_train:], ys[n_train:]


def message_coherence(xs, ys):
    """Renvoie None si les longueurs concordent, sinon un message d'alerte."""
    if len(xs) != len(ys):
        return f"Données incohérentes : {len(xs)} surfaces, {len(ys)} prix"
    return None


def dans_le_domaine(valeur, exemples):
    """Vrai si la valeur reste entre le min et le max des exemples vus."""
    return min(exemples) <= valeur <= max(exemples)
