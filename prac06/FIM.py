#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import sys


def entropy(line, radio):
	total = len(line)
	#Frecuencias
	dict = {}
	i = 0
	for i in range(i, total, radio):
		if i + radio <= total:
			tupla = ''
			for r in range(radio):
				tupla = tupla +line[i]
			if (tupla != '-'):
				dict[tupla] = dict.get(tupla, 0) + 1
	freqs = list()
	for c in dict:
		if len(c) >= radio:
			freqs.append(dict[c] / float(total))
	#Entropía
	ent = 0.0
	for freq in freqs:
		ent = ent + freq * math.log(freq, 2)
	ent = -ent
	if ent == -0.0:
		ent = 0.0
	return ent


archIN = sys.argv[1];
maxK	 = int(sys.argv[2]);

f = open(archIN, 'r')

lineas = []
for line in f:
  if line!="\n":
	a=line.strip()
	lineas=lineas+[a]


 
n = len(lineas);
for k in range(maxK+1):


	X = lineas[0:n-k];
	HX = entropy(X,1);

	Y = lineas[k:n];
	HY = entropy(Y,1);

	XY = X;
	for p in range(n-k):
		XY[p] = XY[p]+ Y[p];

	HXY = entropy(XY,1);
	I = HX+HY-HXY
	print(str(k)+" "+str(HX)+" "+str(HY)+" "+str(HXY)+" "+str(I) )	
	

