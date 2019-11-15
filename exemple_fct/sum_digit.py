#-*- coding: utf8 -*-

"""
    Exemple effectuant la somme des digits donnés (somme qui se réinitialise si on croise un 0)
"""

digit="123450987"
print(sum(map(int,digit.split('0')[-1])))