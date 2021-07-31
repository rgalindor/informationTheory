import sys;

nombre = sys.argv[1];

archivoEn = open(nombre,"r");
limite    = int(sys.argv[2]);
archivoSa = open(nombre+".cL","w");


Lineas = [];
contador = []
line = archivoEn.readline().strip()
Lineas = Lineas + [line]
for j in range(len(line)):
	if (line[j]=='-'):
		contador = contador + [1];
	else:
		contador = contador + [0];

while 1:
	line = archivoEn.readline().strip()
	if not line:
		break
	line = line.lower()
	Lineas = Lineas + [line]
	for j in range(len(line)):
		if (line[j]=='-'):
			contador[j]+= 1;
		else:
			contador[j]+= 0;
		
archivoEn.close()

for j in range(len(Lineas)):
	for i in range(len(Lineas[j])):
		if (contador[i]<limite):
			archivoSa.write(Lineas[j][i]);
	archivoSa.write("\n");

archivoSa.close();
