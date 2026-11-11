"""Enregistrer un modèle : ce qu'on garde, ce sont ses paramètres (b039)."""

import json
from pathlib import Path

# Dossier sorties/ dans le projet, calculé à partir de ce fichier.
DOSSIER_SORTIES = Path(__file__).resolve().parent.parent / "sorties"


def vers_texte(parametres):
    """Convertit les paramètres en texte JSON."""
    return json.dumps(parametres)


def sauvegarder_modele(parametres, nom="modele.json"):
    """Écrit le modèle dans sorties/nom et renvoie le chemin du fichier."""
    DOSSIER_SORTIES.mkdir(exist_ok=True)
    chemin = DOSSIER_SORTIES / nom
    chemin.write_text(vers_texte(parametres), encoding="utf-8")
    return chemin


def charger_modele(nom="modele.json"):
    """Relit un modèle enregistré : un simple dictionnaire de paramètres."""
    chemin = DOSSIER_SORTIES / nom
    return json.loads(chemin.read_text(encoding="utf-8"))
