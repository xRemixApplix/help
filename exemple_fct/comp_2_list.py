#-*- coding: utf8 -*-

"""
    Exemple de la fonction zip() pour comparer 2 listes
"""

liste_1 = ["a", "b", "c"]
liste_2 = [1, 2, 3]

for x, y in zip(liste_1, liste_2) :
    print(x, y)
