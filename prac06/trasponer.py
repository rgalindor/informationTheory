import sys

nombre = sys.argv[1];

entrada = open(nombre,"r");
salida  = open(nombre+"T","w");

c = entrada.read(1);
header = 0;
while (c):
	if (c=='>'):
		header = 1;
	if ((c!='\n')&(header==0)):
		salida.write(c.lower()+"\n");
	if (c=='\n'):
		header = 0;
	c = entrada.read(1);
