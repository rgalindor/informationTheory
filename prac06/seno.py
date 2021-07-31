import sys;
import math;

def buscar(intervalos,valor):
	n = len(intervalos);
	for i in range(n):
		if (intervalos[i]>valor):
			return i;
	return n+1;

xmax = float(sys.argv[1]);
dx	  = float(sys.argv[2]);
dy   = float(sys.argv[3]);

nX = int(xmax / dx);



intervalosY = []
y = -1;
while (y<1):
	intervalosY += [y];
	y = y+dy;


salida = open("sin.dat","w");

x = 0;
for i in range(nX):
	x = x + dx;
	y = math.sin(x);
	salida.write(str(buscar(intervalosY,y))+"\n");
	
