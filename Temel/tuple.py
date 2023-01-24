# -*- coding: utf-8 -*-

tupleListe=(2,4,6,"Ankara",(2,3,4),[])
liste=[2,4,6,"Ankara",(2,3,4),()]
print(type(tupleListe))
print(type(liste))
print(tupleListe)
liste[0]=6

print(liste[1:2])
print(tupleListe[1:2])
print(liste)
print(len(tupleListe))
