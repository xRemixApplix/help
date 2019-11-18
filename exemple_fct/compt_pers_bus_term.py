#-*- coding: utf8 -*-

"""
    Exemple permettant de savoir combien de personne sont dans le bus arrivé au terminus
"""

line1="3"              # Nbre Arret
line2="1 2 2"          # Personne entrant a chaque arret
line3="1 2 1 2 2"      # Nbre d'arret passés avant de descendre pour chaque personne

x=[]
n = int(line1)
for i,e in enumerate(line2.split()):
    s = int(i)
    e=int(e)
    for z in range(e):
        x.append(s)
for i,e in enumerate(map(int,line3.split())):
    x[i]+=e

print(sum(e>=n for e in x))