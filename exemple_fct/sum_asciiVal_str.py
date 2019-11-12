#-*- coding: utf8 -*-

"""
    Exemple d'utilisation des fonctions map(), chr(), ord()pour faire 
    la somme des valeurs ASCII d'une chaine de caracteres et retourner la valeur moyenne arrondi à l'entier inférieur sous forme de lettre.
"""

names = "ABC"

print(chr(sum(map(ord,names))//len(names.upper())))
