"""Partie 1 : du modèle écrit à la main jusqu'à l'IA complète (b002 à b027)."""

from ia import titre
from ia.cout import mae_valeurs, mse, mse_valeurs, rmse, somme_erreurs
from ia.donnees import (PRIX_JUGE, SURFACES_JUGE, TEST_X, TEST_Y, TRAIN_X,
                        TRAIN_Y, charger_appartements, decouper)
from ia.modele import modele, modele_fixe
from ia.recherche import moindres_carres, nombre_essais, recherche_grille


def lecon_premier_modele():
    """b002 : une fonction toute simple, réglée à la main."""
    titre("b002", "Le cœur de notre future IA : une fonction")
    print(modele_fixe(50))


def lecon_boutons():
    """b005-b006 : même entrée, même fonction, trois réglages."""
    titre("b006", "Deux boutons : modele(surface, poids, biais)")
    print(modele(50, 3, 10))
    print(modele(50, 2, 40))
    print(modele(50, 4, 0))


def lecon_donnees():
    """b007-b008 : les exemples, chacun avec sa bonne réponse."""
    titre("b007", "Six appartements (lus dans data/appartements.csv)")
    donnees = charger_appartements()
    for surface, prix in donnees:
        print(f"{surface} m2 -> {prix} 000 euros")
    print(len(donnees), "exemples")
    print()
    print("Le chemin complet (b008) : données -> réglage du modèle -> prédiction")
    return donnees


def prix_regle_manuelle(surface):
    """Programmation classique (b009) : c'est nous qui écrivons la règle."""
    if surface < 40:
        return 90
    if surface < 70:
        return 180
    return 260


def lecon_regles_vs_apprentissage(donnees):
    """b009 : données + règles -> réponses, contre données + réponses -> règle."""
    titre("b009", "Programmation classique : des règles écrites à la main")
    for surface, prix in donnees:
        print(f"{surface} m2 : vrai prix {prix} | règle manuelle {prix_regle_manuelle(surface)}")
    print("Avec l'apprentissage, on donne les réponses... et la machine trouve la règle.")


def lecon_tableau_erreurs(donnees):
    """b010 : surface, vrai prix, prédiction, écart."""
    titre("b010", "Un réglage testé sur six appartements (poids 2, biais 40)")
    for surface, prix in donnees:
        prediction = modele(surface, 2, 40)
        print(surface, prix, prediction, prediction - prix)


def lecon_juge_aveugle():
    """b012 : la somme des erreurs ne distingue pas un bon modèle d'un absurde."""
    titre("b012", "Premier juge : la somme des erreurs... aveugle !")
    print(somme_erreurs(SURFACES_JUGE, PRIX_JUGE, 3, 20))
    print(somme_erreurs(SURFACES_JUGE, PRIX_JUGE, 0, 160))


def lecon_mse():
    """b013 et b016 : l'erreur quadratique moyenne fait la différence."""
    titre("b013", "Le vrai juge : l'erreur quadratique moyenne (MSE)")
    bon = mse(SURFACES_JUGE, PRIX_JUGE, 3, 20)
    absurde = mse(SURFACES_JUGE, PRIX_JUGE, 0, 160)
    print(round(bon, 1))
    print(round(absurde, 1))
    print()
    print("b016 - coût divisé par environ", round(absurde / bon),
          "entre le modèle absurde et le bon réglage")


def lecon_carre_vs_absolu():
    """b014-b015 : le carré punit lourdement les gros ratés."""
    titre("b014-b015", "Pourquoi le carré ? Impitoyable avec les gros ratés")
    for erreur in [2, 10, 100]:
        print("erreur", erreur, "-> coût", erreur ** 2)
    print()
    vrais = [0] * 10
    dix_petits = [1] * 10        # dix petites erreurs de 1
    un_gros = [0] * 9 + [10]     # neuf réponses justes, un raté de 10
    print("écart absolu moyen : dix petits ratés", mae_valeurs(vrais, dix_petits),
          "| un gros raté", mae_valeurs(vrais, un_gros))
    print("MSE                : dix petits ratés", mse_valeurs(vrais, dix_petits),
          "| un gros raté", mse_valeurs(vrais, un_gros))


def lecon_recherche_grille():
    """b017-b019 : la machine cherche seule, sur l'entraînement uniquement."""
    titre("b017", "Laisser la machine chercher : la force brute")
    train_s, train_p, test_s, test_p = decouper(SURFACES_JUGE, PRIX_JUGE, 4)
    meilleur, essais = recherche_grille(train_s, train_p, range(6), range(0, 60, 10))
    cout, poids, biais = meilleur
    print("poids :", poids, "biais :", biais)
    print("coût entraînement :", cout)
    print("coût test :", mse(test_s, test_p, poids, biais))
    print(f"({essais} essais)")
    titre("b019", "La recette de presque tous les modèles")
    etapes = [
        "Choisir une forme de modèle (ici une droite à deux boutons)",
        "Choisir un juge (ici la MSE)",
        "Chercher le réglage qui minimise le coût sur l'entraînement",
        "Vérifier sur des données jamais vues (le test)",
    ]
    for numero, etape in enumerate(etapes, start=1):
        print(f"  {numero}. {etape}")


def lecon_explosion():
    """b020 à b022 : chaque bouton multiplie le nombre d'essais."""
    titre("b020", "Le hic : une grille plus fine coûte très cher")
    print("Grille grossière : 6 x 6 =", 6 * 6, "essais")
    print("Grille fine      : 1000 x 1000 =", 1000 * 1000, "essais")
    titre("b022", "L'explosion combinatoire")
    valeurs = 101  # crans par bouton
    for boutons in [1, 2, 3, 10]:
        essais = nombre_essais(valeurs, boutons)
        print(boutons, "bouton(s) :", essais, "essais")
    secondes = nombre_essais(valeurs, 10) / 1_000_000_000
    annees = secondes / (365 * 24 * 3600)
    print("À un milliard d'essais par seconde :", round(annees), "ans pour 10 boutons")


def lecon_moindres_carres():
    """b023 : la formule directe, sans rien essayer."""
    titre("b023", "La formule de Legendre (1805) : les moindres carrés")
    poids, biais = moindres_carres(TRAIN_X, TRAIN_Y)
    print("poids :", poids)
    print("biais :", biais)


def lecon_ressorts():
    """b024 : la règle reliée par des ressorts cherche l'énergie minimale."""
    titre("b024", "Les ressorts : l'énergie est la somme des carrés")
    for poids, biais in [(3, 20), (3.1, 20), (3, 22)]:
        energie = sum((modele(x, poids, biais) - y) ** 2
                      for x, y in zip(TRAIN_X, TRAIN_Y))
        print(f"règle poids {poids}, biais {biais} -> énergie des ressorts : {energie:.1f}")
    print("La position d'équilibre (poids 3, biais 20) est la droite des moindres carrés.")


def lecon_train_test():
    """b025-b026 : juger sur l'entraînement et sur le test, puis la RMSE."""
    titre("b025", "Juger sur des appartements jamais vus")
    print("MSE entraînement :", mse(TRAIN_X, TRAIN_Y, 3, 20))
    print("MSE test :", mse(TEST_X, TEST_Y, 3, 20))
    titre("b026", "RMSE : revenir à des euros")
    erreur_typique = rmse(TEST_X, TEST_Y, 3, 20)
    print("RMSE test :", erreur_typique, "milliers d'euros")
    print("Soit environ", round(100 * erreur_typique / 200), "% d'un bien à 200 000 euros")


def ia_complete():
    """b027 : entraîner, évaluer, prédire. Renvoie (poids, biais, mse_test, prix_55)."""
    poids, biais = moindres_carres(TRAIN_X, TRAIN_Y)
    mse_test = mse(TEST_X, TEST_Y, poids, biais)
    return poids, biais, mse_test, modele(55, poids, biais)


def lecon_ia_complete():
    """b027 : notre IA complète, en Python pur."""
    titre("b027", "Notre IA complète, en Python pur")
    poids, biais, mse_test, prix_55 = ia_complete()
    print("Réglage :", poids, biais)
    print("MSE test :", mse_test)
    print("55 m² :", prix_55, "k€")


def executer_partie1():
    """Enchaîne toutes les leçons de la partie 1 dans l'ordre de l'épisode."""
    lecon_premier_modele()
    lecon_boutons()
    donnees = lecon_donnees()
    lecon_regles_vs_apprentissage(donnees)
    lecon_tableau_erreurs(donnees)
    lecon_juge_aveugle()
    lecon_mse()
    lecon_carre_vs_absolu()
    lecon_recherche_grille()
    lecon_explosion()
    lecon_moindres_carres()
    lecon_ressorts()
    lecon_train_test()
    lecon_ia_complete()
