#-*- coding: utf8 -*-

"""
    Exemple permettant de faire le produit de la somme des digits d'une suite de nombre sous forme de chaine de caractères
"""

chaine="1 22 33 44 55"
p=1
for y in chaine.split():p*=sum(map(int,list(y)))
print(p)