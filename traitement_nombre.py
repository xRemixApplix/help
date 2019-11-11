#-*- coding: utf8 -*-

"""
    Module regroupant toutes les fonctions utilisees pour le traitement des nombres
"""

def decompose(n) :
    """
        Fonction qui decompose le nombre n en parametre 
        en liste (list_facteur) de nombres premier multiplicateur du nombre n

        Paramètres :
            n       : Element a decomposer en liste de nombre premier.

        Sortie :
            list_facteur    : Liste de multiplicateurs premier
    """
    # Initialisation d'une liste vide
    list_facteur = []
    # On débute la verification à partir de 2 (1 n'étant pas un nombre premier)
    d=2
    # On teste la divisibilite du nombre par 2, puis son quotiant jusqu'a obtenir un nombre impair
    while n%d==0:
        list_facteur.append(d)
        q=n//d
        n=q
    # On fait de même avec 3, puis avec tout les nombres impairs (de 2 en 2)
    d=3
    while d<=n:
        while n%d==0:
            list_facteur.append(d)
            q=n//d
            n=q
        d += 2
    # Retourne la liste de nombre premier
    return list_facteur