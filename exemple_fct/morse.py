#-*- coding: utf8 -*-

"""
    Exemple tranformant un numero de telephone en morse + Gestion des erreurs (numero trop long ou lettre)
"""

list=['-----','.----','..---','...--','....-','.....','-....','--...','---..','----.']
m="1258993258"
if len(m)==10:
    try:
        int(m)
    except ValueError:
        print("Untransformable")
    else:
        for i in m:print(list[int(i)],end='')
else:
    print("Untransformable")