#COMO SABER SI UN NUMERO ES PAR 
numero = input('Agrega un numero y te dire si es par o impar \r\n')

numero = int(numero)
if numero %2 ==0: 
    print (f'tu numero es {numero}  y es par')
else:
    print(f'tu numero es {numero}  y es impar')