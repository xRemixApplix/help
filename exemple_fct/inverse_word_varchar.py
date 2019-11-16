#-*- coding: utf8 -*-

"""
    Exemple permettant d'afficher à l'envers les mots d'une phrase en gardant l'ordre des mots
"""

text="Hello World"
print(*list(text[::-1].split(" "))[::-1])