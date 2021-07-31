import random,sys

Alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','t','u','v','w','x','y','z','.',',',' ']

tam = int(sys.argv[1]);
archsalida = sys.argv[2];
salida = open(archsalida,'w')

for i in range(tam):
	car = random.choice(Alfabeto);
	salida.write(car);

salida.close();
