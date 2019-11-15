#-*- coding: utf8 -*-

"""
    Exemple permettant de dessiner un diamond dimension n*2
"""

n = 4

print("#" * n)
for i in range(n):
    print((n - (i + 1)) * ' ' + (i + 1) * '#' + i * '#')
for i in range(n - 1, -1, -1):
    print((n - (i + 1)) * ' ' + (i + 1) * '#' + i * '#')