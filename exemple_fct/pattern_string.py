#-*- coding: utf8 -*-

"""
    Exemple permettant de trouver un pattern dans une chaine de caracteres
"""

s="CodingCodingCodingCodingCodingCodingCoding"
a=s[0]

while a*(len(s)//len(a))!=s:
    a+=s[len(a)]
    
print(a)