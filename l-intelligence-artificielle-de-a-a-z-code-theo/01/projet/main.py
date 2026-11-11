"""HexaPython - L'IA de A à Z, épisode 1 : qu'est-ce qu'un modèle d'IA ?

Point d'entrée : exécute toute la progression de l'épisode, dans l'ordre.
Lancement : python main.py
"""

import sys

from lecons_partie1 import executer_partie1
from lecons_partie2 import executer_partie2


def afficher_introduction():
    """b001 et b004 : la promesse et le programme de l'épisode."""
    print("HexaPython - L'Intelligence Artificielle de A à Z")
    print("Épisode 1 : Qu'est-ce qu'un modèle d'IA ?")
    print()
    print("Promesse : une IA en Python pur qui devine le prix d'un appartement.")
    print("Fil rouge : comment deviner un prix qu'on ne lui a jamais donné ?")
    print()
    print("Programme de l'épisode (b004) :")
    etapes = [
        "Un modèle = une fonction avec des boutons (paramètres)",
        "Des données d'entraînement et de test",
        "Un juge : la fonction de coût (MSE)",
        "Chercher le meilleur réglage : force brute, puis moindres carrés",
        "Supervisé contre non supervisé",
        "Prédire, se méfier, éviter les pièges",
        "Le défi : un modèle à trois boutons",
    ]
    for numero, etape in enumerate(etapes, start=1):
        print(f"  {numero}. {etape}")


def main():
    # Évite un plantage d'affichage sur les terminaux qui ne gèrent pas l'UTF-8.
    try:
        sys.stdout.reconfigure(errors="replace")
    except AttributeError:
        pass
    afficher_introduction()
    executer_partie1()
    executer_partie2()
    print()
    print("Fin de l'épisode 1. Prochain épisode : la descente de gradient !")


if __name__ == "__main__":
    main()
