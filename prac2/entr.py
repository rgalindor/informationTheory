#!/usr/bin/python
# -*- coding: utf-8 -*-

import inf_mutua as imt
import sys

def lee(f):
	d = {}
	a = open(f,'r')
	l = a.readlines()
	for v in range(len(l)):
		if l[v].find('/')>0:
			nd = l[v].split()[0].split('/')
			print str(nd[0])+"/"+str(nd[1])
			d[v] = int(nd[0]) / float(nd[1])
		else:
			d[v] = float(l[v].split()[0])
	return d

NombreArchivo = sys.argv[1];
Datos = lee(NombreArchivo)
Entropia = imt.H(Datos)
print "\n\nEntropia= "+str(Entropia)
