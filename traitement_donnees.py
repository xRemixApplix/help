#-*- coding: utf8 -*-

"""
    Module regroupant toutes les fonctions utilisees pour le traitement de donnees
"""

def miroir(elt, typeN):
    """
        Fonction retournant l'element miroir de l'element donne en parametre

        Paramètres :
            elt     : Element a inverser.
            typeN   : Type de l'element.
    """
    # Initialisation d'une liste vide
    list = []
    # Parcours de la chaine de caractere
    for char in str(elt):
        # On met chaque caractère de la chaine dans une liste
        list.append(char)
    # Inversion de la liste
    list.reverse()
    # On retourne l'element dans le type demande en parametre
    return typeN("".join(list))
