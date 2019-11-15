#-*- coding: utf8 -*-

"""
    Exemple de l'addition de deux transformé en binaire comme s'il etait des nombres entiers
"""

n = "13 89"
p0, p1 = [int(j) for j in n.split()]
print(int(str(bin(p0)[2:]))+int(str(bin(p1)[2:])))