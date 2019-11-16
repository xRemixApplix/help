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
    # On retourne l'element dans le type demande en parametre
    return typeN(str(elt)[::-1])

print(miroir(34567,int))