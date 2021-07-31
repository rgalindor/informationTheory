#!/usr/bin/env python
# -*- coding: utf-8 -*-

#matrixentr.py <input> <radio> <by_column? -1=no,yes=ioc>?
import math
import sys

output = ''
try:
    input = sys.argv[1]
    output = input + ".output"
except IndexError:
    input = "li.txt"
    output = input + ".output"
try:
    radio = int(sys.argv[2])
except IndexError:
    radio = 1
try:
    column = int(sys.argv[3])
except IndexError:
    column = -1

def entropy(line, radio):
    if type(line).__name__ == 'str':
        line.strip()
    else:
        line = str(line)
        line = line.strip('\', ()').replace('\', \'', '')
    total = len(line)

    #Frecuencias
    dict = {}
    i = 0
    for i in range(i, total, radio):
        if i + radio <= total:
            tupla = line[i:i + radio]
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

file = open(input)
entr = 0.0
entrList = list()

if column < 0:#Por renglón
    while 1:
        line = file.readline().strip()
        if not line:
            break
        line = line.lower()
        entr = entropy(line, radio)
        entrList.append(entr)
    file.close()


else:#Por columna
    line = ''
    renglones = list()
    while 1:
        line = file.readline().strip()
        if not line:
            break
        renglones.append(list(line))
    file.close()
    renglones = zip(*renglones)
    for r in renglones:
        entr = entropy(r, radio)
        entrList.append(entr)

    file = open(input+".mif", 'w')

    MAX = 0;
    J=0;
    for j in renglones:
    	I=0;
    	J+=1;
    	for i in renglones:
			I+=1;
			concatenados = ''
			for l in range(len(j)):
				concatenados+=(j[l]+i[l]);			
			entr = entrList[J-1] + entrList[I-1] - entropy(concatenados,2);
			if (entr>MAX):
				MAX = entr;
			file.write(str(J)+" "+str(I)+" "+str(entr) + "\n")
    file.close()			

    i = renglones[0];
    salidaGPL = open(input+".gpl", 'w')
    salidaGPL.write("set cbrange [ 0.00000 : "+str(MAX)+" ] noreverse nowriteback\n");
    salidaGPL.write("set xrange [ -0.500000 : "+str(J+.05)+" ] noreverse nowriteback\n");
    salidaGPL.write("set yrange [ -0.500000 : "+str(J+.05)+" ] noreverse nowriteback\n");
    salidaGPL.write("plot '"+input+".mif'  using 1:2:3 with image\n");
    salidaGPL.close();

file = open(output, 'w')
for c in entrList:
   file.writelines(str(c) + "\n")
file.close()
