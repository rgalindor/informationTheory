#!/usr/bin/python2.5
#-*- coding:utf-8 -*-

import math, random

def lee_archivo(f):
	"""
	lee el archivo con un par de columnas que representan
	los dos sistemas a analizar

	regresa [X, xmax, xmin, Y, ymax, ymin]: serie X max y min en X e Y max y min en Y
	"""
	X = []
	Y = []
	xmin = ymin = 1e10000
	xmax = ymax = -1e10000
	r = open(f,"r")
	mas = True
	l = r.readline()
	while mas:
		if l == '':
			mas = False
			break
		else:
			xi = float(l.split()[0])
		 	if xi > xmax:
				xmax = xi
			elif xi < xmin:
				xmin = xi
			X.append(xi)
			yi = float(l.split()[1])
			if yi > ymax:
				ymax = yi
			elif yi < ymin:
				ymin = yi
			Y.append(yi)
		l = r.readline()
	
	r.close()
	return [X, xmax, xmin, Y, ymax, ymin]

def lee_ventana(x, tvent=0):
	"""
	se lee el mismo archivo que contiene la serie de tiempo 
	de valores enteros a analizar y se va a analizar dependiendo 
	del el tamano de la ventana 
	input: manejador x, manejador y, tamaño ventna tvent
	
	regresa [X,Y]: la ventana de la serie X y la serie Y
	"""
	X = []

	lx = x.read(tvent)
	
	for i in xrange(len(lx)):
		X.append(int(lx[1]))

	return X


def discreto(var, max, min, n_edos):
	"""
	discretiza la variable v dentro
	del rango establecido por max y  min 
	con la cantidad de estados definidos en n_edos

	regresa dig: un entero que var discretizada
	"""
	intervalo = max - min
	R = float(intervalo) / float(n_edos)
	
	dig = int((var-min) / R) - 1
	if dig < 0:
		return 0

	return dig


def discretiza(V, vmax, vmin, n): 
	"""
	discretiza el conjunto de datos que se le paso en el
	parametro, tambien se tiene que especificar el valor
	minimo, maximo y el numero de estados 

	regresa D: lista con los valores discretos de P	
	"""
	D = []
	for i in xrange(len(V)):
		d = discreto(V[i], vmax, vmin, n)
		D.append(d)
	return D



def prob(X):
	"""
	determina la probabiliad de los elementos en 
	el conjunto X
	
	regresa [D, P, N]: un vector con 3 objetos:
	D. cantidad de ocurrencias de cada simbolo en X
	P. probabilidad de ocurrencia de cada simbolo en X
	N. la cantidad original de elementos en X
	"""
	D = {} #diccionario donde guardamos la ocurrencia de cada simbolo
	P = {} #diccionario donde van a estar las probabilidades
	N = len(X)
        
        #contamos las ocurrencias
	for i in xrange(len(X)):
		D[X[i]] = 0
	for i in xrange(len(X)):
		D[X[i]] += 1

	#determinamos probabilidades
	for i in xrange(len(D)):
		P[D.keys()[i]] = 0
		P[D.keys()[i]] = float(D.values()[i]) / N

	return [P, N]



def prcond(X,Y):
	"""
	determina la probabilidad conjunta 
	entre los conjuntos X e Y que deben estar
	discretizados

	regresa [PX, PY, PXY]:
	PX: probabilidad de aparicion de X
	PY: probabilidad de aparicion de Y
	PXY: probabilidad conjunta de los sistemas X e Y
	"""
	[PX,NX] = prob(X)
	[PY,NY] = prob(Y)

	D = dict()
	P = dict()
	tot = 0 

	for i in range(len(X)):
		for j in range(len(Y)):
			D[X[i],Y[i]] = 0

	for i in range(len(X)):
		for j in range(len(Y)):
			D[X[i],Y[j]] +=  1
			tot += 1

	for i in range(len(D)):
 		P[i] = P.get(i,0) + (float(D.values()[i])/tot)*DY[D.keys()[i][1]]
	
	return [PX, PY, P]

def H(X):
	"""
	Regresa la Entropia de Shannon de p en los estados que deben venir 
	en un diccionario como esta definido in prob, las unidades de
	H esta en bits

	regresa H: float con la entropia de X
	"""
	H = 0.0
	
	for j in range(len(X)):
		H += X.values()[j] * math.log(X.values()[j],2)
	#H = -H / log(2)
	
	return -H



def Hxy(P):
	"""
	calcula la entropia conjunta
	recibe 	P: entropia de estados conjuntos
	       	estados: cantidad de estados distintos en X
		num_est: cantidad de estados distintos en Y

	regresa la entropía conjunta entre dos sistemas
	"""
	HXY = 0.0
	for i in xrange(len(P)):
		HXY += P[i,j] * math.log(P[i,j],2)
	#HXY = -HXY / math.log(2)
	
	return -HXY



def inf_mutua(H1, H2, HXY):
	"""
	calcula la entropia conjunta de H1 y H2
	recibe tambien HXY que es la entropia conjunta de H1 y H2

	regresa la informacion mutua dependiendo de la entropia
	del primer sistema, la del segundo y la conjunta
	"""
	I = H1 + H2 - HXY
	return I
