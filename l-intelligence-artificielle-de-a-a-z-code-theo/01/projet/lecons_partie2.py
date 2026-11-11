"""Partie 2 : supervisé, prédiction, pièges, défi et bilan (b028 à b068)."""

from ia import titre
from ia.cout import mse, mse_predicteur, mse_valeurs
from ia.donnees import (DEFI, PRIX_JUGE, SURFACES_JUGE, VENTES_TEST,
                        VENTES_TRAIN, dans_le_domaine, message_coherence,
                        separer_colonnes)
from ia.modele import modele, modele_deux_entrees
from ia.non_supervise import couper_au_plus_grand_ecart, ecarts_successifs
from ia.recherche import moindres_carres, recherche_grille, recherche_grille_3d
from ia.sauvegarde import charger_modele, sauvegarder_modele, vers_texte
from lecons_partie1 import ia_complete

# Réglage en euros, appris sur VENTES_TRAIN (voir lecon_reference).
POIDS_EUROS = 3000
BIAIS_EUROS = 5000


def modele_euros(surface, poids=POIDS_EUROS, biais=BIAIS_EUROS):
    """Notre droite réglée, en euros (b035)."""
    return poids * surface + biais


def lecon_supervise():
    """b029 : chaque exemple arrive avec son étiquette."""
    titre("b029", "Apprentissage supervisé : des exemples étiquetés")
    donnees = [(30, 95000), (45, 140000), (60, 185000)]
    for surface, prix in donnees:
        print(f"{surface} m2 -> {prix} euros")


def lecon_comparaison():
    """b031 : les deux familles côte à côte."""
    titre("b031", "Supervisé contre non supervisé")
    print("Supervisé     : données + étiquettes -> prédire la bonne réponse")
    print("Non supervisé : données seules       -> trouver une structure cachée")


def lecon_non_supervise():
    """b032 : deux groupes découverts sans aucun prix."""
    titre("b032", "Non supervisé : des surfaces, aucun prix")
    surfaces = [22, 25, 28, 70, 75, 81]
    print("Écarts successifs :", ecarts_successifs(sorted(surfaces)))
    groupe_a, groupe_b = couper_au_plus_grand_ecart(surfaces)
    print("Groupe A :", groupe_a)
    print("Groupe B :", groupe_b)


def lecon_choisir():
    """b033 : une seule question pour choisir."""
    titre("b033", "Ai-je la réponse que je veux prédire ?")
    cas = [
        ("Prix d'appartements (ventes passées connues)", True),
        ("Familles de clients à découvrir", False),
    ]
    for description, a_les_reponses in cas:
        print(description, "->", "supervisé" if a_les_reponses else "non supervisé")


def lecon_lire_parametres():
    """b034 : le poids est le prix d'un m2 en plus, le biais le point de départ."""
    titre("b034", "Lire les boutons : ils ont un sens")
    p40 = modele(40, POIDS_EUROS, BIAIS_EUROS)
    p41 = modele(41, POIDS_EUROS, BIAIS_EUROS)
    print(p40, p41, p41 - p40)
    print(modele(0, POIDS_EUROS, BIAIS_EUROS))


def lecon_predictions():
    """b035 et b037 : prédire, puis vérifier si l'on est en terrain connu."""
    titre("b035", "Utiliser notre IA pour de vrai")
    for s in [25, 52, 90]:
        print(f"{s} m2 -> {modele_euros(s)} euros")
    titre("b037", "Terrain connu ou extrapolation ?")
    surfaces_vues = [s for s, _ in VENTES_TRAIN]
    print("Surfaces d'entraînement : de", min(surfaces_vues), "à", max(surfaces_vues), "m2")
    for s in [25, 52, 90]:
        statut = "terrain connu" if dans_le_domaine(s, surfaces_vues) else "EXTRAPOLATION"
        print(f"{s} m2 : {statut}")


def lecon_extrapolation():
    """b038 : le modèle répond avec aplomb, même à l'absurde."""
    titre("b038", "Poussons la droite jusqu'à l'absurde")
    for s in [1, 5, 500]:
        print(f"{s} m2 -> {modele_euros(s)} euros")


def lecon_sauvegarde():
    """b039-b040 : un modèle entraîné, c'est d'abord des paramètres."""
    titre("b039", "Ce qu'on garde vraiment : deux nombres")
    parametres = {"poids": POIDS_EUROS, "biais": BIAIS_EUROS}
    texte = vers_texte(parametres)
    print(texte)
    print(len(texte), "caracteres")
    chemin = sauvegarder_modele(parametres)
    recharge = charger_modele()
    print("Modèle enregistré dans sorties/" + chemin.name)
    print("Rechargé, il prédit 52 m2 ->", modele(52, recharge["poids"], recharge["biais"]), "euros")
    titre("b040", "Une question d'échelle")
    print("Notre IA : 2 paramètres | grands modèles de langage : des milliards")


def lecon_reference():
    """b041-b042 : toujours se comparer à un modèle bête."""
    titre("b042", "Le match : modèle paresseux contre notre droite")
    surfaces, prix = separer_colonnes(VENTES_TRAIN)
    moyenne = sum(prix) / len(prix)
    cout_bete = mse_predicteur(lambda s: moyenne, VENTES_TEST)
    cout_ia = mse_predicteur(lambda s: POIDS_EUROS * s + BIAIS_EUROS, VENTES_TEST)
    print("modele bete :", round(cout_bete ** 0.5), "euros")
    print("notre IA :", round(cout_ia ** 0.5), "euros")
    print("(le modèle bête répond toujours", moyenne, "euros)")
    print("Notre IA se trompe environ", round((cout_bete / cout_ia) ** 0.5), "fois moins")
    poids, biais = moindres_carres(surfaces, prix)
    print("Réglage appris par moindres carrés sur ces ventes :", poids, biais)


def lecon_deux_entrees():
    """b044-b045 : un bouton de plus pour écouter une information de plus."""
    titre("b044", "Deux informations : surface et nombre de pièces")
    print(modele_deux_entrees(50, 2, 3000, 5000, 10000))
    print(modele_deux_entrees(80, 4, 3000, 5000, 10000))


def lecon_pieges():
    """b046 à b050 : unités, test vide, zip silencieux."""
    titre("b046", "Piège n°1 : les unités")
    surface = 60
    print(3000 * surface + 10000)
    print(3 * surface + 10)

    titre("b047", "Piège n°2 : un ensemble de test vide")
    test_vrais = []
    test_predits = []
    try:
        print(mse_valeurs(test_vrais, test_predits))
    except ZeroDivisionError as erreur:
        print("ZeroDivisionError :", erreur)
    print("Bon réflexe : taille du test =", len(test_vrais), "exemple(s)")

    titre("b048", "Piège n°3 : zip abandonne sans prévenir")
    surfaces = [30, 45, 60, 80]
    prix = [100000, 145000, 190000]
    paires = list(zip(surfaces, prix))
    print(len(paires))
    print(paires[-1])

    titre("b050", "La parade : comparer les longueurs")
    message = message_coherence(surfaces, prix)
    if message:
        print(message)
    # Depuis Python 3.10, zip(..., strict=True) proteste aussi.
    try:
        list(zip(surfaces, prix, strict=True))
    except ValueError as erreur:
        print("Avec zip(..., strict=True) :", erreur)


def lecon_defi():
    """b052 à b056 : le défi à trois boutons et sa solution."""
    titre("b052", "Le défi : un modèle à trois boutons")
    for s, p, prix in DEFI:
        print(f"{s} m2, {p} pièce(s) -> {prix} k€")
    titre("b054", "La solution : trois boucles imbriquées")
    meilleur, essais = recherche_grille_3d(DEFI, range(6), range(11), range(21))
    print("Essais :", essais)
    print("Meilleur réglage :", meilleur[1:])
    print("Coût :", meilleur[0])
    titre("b055-b056", "Chaque curseur multiplie le travail")
    total = essais
    for curseur, crans in [("étage (0 à 10)", 11), ("quartier (0 à 20)", 21)]:
        total *= crans
        print(f"+ un bouton {curseur} : {total} essais")


def lecon_recapitulatif():
    """b057 à b059 : le modèle, le juge et les deux façons de chercher."""
    titre("b057", "Le modèle et son juge")
    surfaces = [20, 40, 60]
    prix = [60, 100, 140]
    for w, b in [(2, 20), (2, 30)]:
        preds = [modele(s, w, b) for s in surfaces]
        print(w, b, mse_valeurs(prix, preds))

    titre("b058", "Les moindres carrés, encore une fois")
    w, b = moindres_carres(surfaces, prix)
    print(w, b)
    print(w * 50 + b)

    titre("b059", "Force brute contre formule")
    (cout_g, wg, bg), essais = recherche_grille(SURFACES_JUGE, PRIX_JUGE,
                                                range(6), range(0, 60, 10))
    wf, bf = moindres_carres(SURFACES_JUGE, PRIX_JUGE)
    cout_f = mse(SURFACES_JUGE, PRIX_JUGE, wf, bf)
    print(f"Force brute ({essais} essais) : poids {wg}, biais {bg}, MSE {cout_g:.2f}")
    print(f"Formule (une seule passe) : poids {wf:.3f}, biais {bf:.3f}, MSE {cout_f:.2f}")
    print("La bonne réponse tombait entre deux crans : la grille l'a ratée.")


def lecon_bilan():
    """b061 à b068 : six idées, un quiz, la promesse tenue et la suite."""
    titre("b061", "Six idées à retenir")
    idees = [
        "Un modèle est une fonction dont les paramètres sont appris à partir de données.",
        "Régression linéaire : un poids (prix du m2) et un biais (prix de départ).",
        "Un juge chiffré, la fonction de coût : ici la MSE.",
        "On garde un ensemble de test pour juger sur des cas jamais vus.",
        "Avec étiquettes : supervisé ; groupes sans étiquettes : non supervisé.",
        "Tout essayer marche pour deux boutons, puis explose.",
    ]
    for numero, idee in enumerate(idees, start=1):
        print(f"  {numero}. {idee}")

    titre("b062", "Trois questions éclair")
    quiz = [
        ("Clients avec âge, revenu et achat oui/non : supervisé ?",
         "Oui, chaque exemple a sa bonne réponse."),
        ("Pourquoi mettre les erreurs au carré ?",
         "Pour éviter les annulations et punir les gros ratés."),
        ("Erreur minuscule sur l'entraînement : je déploie ?",
         "Pas encore : il faut d'abord juger sur le test."),
    ]
    for question, reponse in quiz:
        print("Q :", question)
        print("R :", reponse)

    titre("b063", "La promesse tenue : une IA en Python pur")
    poids, biais, mse_test, prix_55 = ia_complete()
    print(f"Réglage appris : poids {poids}, biais {biais}")
    print(f"MSE test : {mse_test} | prédiction pour 55 m² : {prix_55} k€")

    titre("b064", "La suite de la saison")
    suite = ["La descente de gradient", "La classification",
             "Préparer de vraies données", "Le surapprentissage",
             "Le premier neurone artificiel"]
    for numero, etape in enumerate(suite, start=2):
        print(f"  Épisode {numero} (ou plus) : {etape}")

    titre("b065-b068", "La question ouverte")
    print("Comment régler des millions de paramètres sans tout essayer ?")
    print("Réponse au prochain épisode : la descente de gradient.")
    print("Et toi, quel prix aimerais-tu prédire ? Dis-le en commentaire !")


def executer_partie2():
    """Enchaîne toutes les leçons de la partie 2 dans l'ordre de l'épisode."""
    lecon_supervise()
    lecon_comparaison()
    lecon_non_supervise()
    lecon_choisir()
    lecon_lire_parametres()
    lecon_predictions()
    lecon_extrapolation()
    lecon_sauvegarde()
    lecon_reference()
    lecon_deux_entrees()
    lecon_pieges()
    lecon_defi()
    lecon_recapitulatif()
    lecon_bilan()
