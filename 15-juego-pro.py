#COMO SABER SI UN NUMERO ES PAR 

#pregunta = input('Agrega un numero y te dire si es par o impar \r\n')
#pregunta += '\r\n escribe "cerrar" para salir de la app\r\n'
pregunta = True

while True:
    entrada = input('Agrega un numero (o escribe "cerrar para salir")  \r\n').strip()
    if entrada.lower() == "cerrar":
        print('programa finalizado')
        break
    try:
        numero = int(entrada)
        if numero %2 ==0: 
            print (f'tu numero es {numero}  y es par')
        else:
            print(f'tu numero es {numero}  y es impar')
    except ValueError:
        print('Por favor ingrese un numnero valido')