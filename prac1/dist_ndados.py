#!/usr/bin/python
#dist n dados con m caras


import sys
import math

dados = int(sys.argv[1])
caras = int(sys.argv[2])

edos = dict()
for i in range(0,caras*dados+1): edos[i] = edos.get(i,0)

#lista en la que cada dado tiene una posicion distinguible
#donde se muestra cada cara
L = list()
for j in range(dados): L.append(1)

#funcion recursiva que aumenta en una la 
#posicion p en la lista L modulo m
def aum(L,m,p):
	if L[p] < m:
		L[p] += 1
	else:
		p += 1
		L[p-1] = 1
		aum(L,m,p)
	

for i in range(caras**dados - 1):
	edos[sum(L)] += 1
	aum(L,caras,0)

for j in range(len(edos.values())):
	print str(edos.values()[j])+"\n",
