import numpy as np
arreglo1= np.zeros(8)
digits= 8
for a in range (digits):
    arreglo1[a]= int(input("Digito "+str(a+1)+": "))
suma= 0
potencia= 7
b= 0
for b in range (len(arreglo1)):
    if(arreglo1[b] == 1):
        suma = suma + (2**potencia)
    potencia= potencia-1

print("Esto "+str(arreglo1) +" en decimal es: " +str(suma))
