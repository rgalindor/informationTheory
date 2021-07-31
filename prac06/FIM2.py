#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import sys


def entropy(dict, total):

	freqs = list()
	for c in dict:
		freqs.append(dict[c] / float(total))
	#Entropía
	ent = 0.0
	for freq in freqs:
		myLog = 0;
		if (freq > 0):
			myLog = math.log(freq, 2)
		ent = ent + freq * myLog
	ent = -ent
	if ent == -0.0:
		ent = 0.0
	return ent


archIN = sys.argv[1];
maxK	 = int(sys.argv[2]);

f = open(archIN, 'r')

diccionariosX = []
diccionariosY = []
diccionariosXY = []

for k in range(maxK+1):
	diccionariosX += [{}]
	diccionariosY += [{}]
	diccionariosXY += [{}]


lineas = []
l = 0;
for line in f:
  if line!="\n":
	a=line.strip()
	if (l<maxK+1):
		lineas=lineas+[a]

	else:
		lineas=lineas[1:len(lineas)]
		lineas=lineas+[a]
		x = str(lineas[0]);
		for k in range(maxK+1):
			esteDictX = diccionariosX[k];
			esteDictY = diccionariosY[k];
			esteDictXY = diccionariosXY[k];
			y  = str(lineas[k]);
			xy = str(lineas[0]+lineas[k]);
			esteDictX[x] = esteDictX.get(x, 0) + 1;
			esteDictY[y] = esteDictY.get(y, 0) + 1;
			esteDictXY[xy] = esteDictXY.get(xy, 0) + 1;
	l = l+1;


for k in range(maxK+1):
	esteDictX = diccionariosX[k];
	esteDictY = diccionariosY[k];
	esteDictXY = diccionariosXY[k];

	HX = entropy(esteDictX,l-k);
	HY = entropy(esteDictY,l-k);
	HXY = entropy(esteDictXY,l-k);



	I = HX+HY-HXY
	print(str(k)+" "+str(HX)+" "+str(HY)+" "+str(HXY)+" "+str(I) )	
	

