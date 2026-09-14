nombre = input('Ingresa tu  nombre por favor\r\n')
print(f'el participante es {nombre}')

#edad = input('Ingresa tu  edad por favor\r\n')
#edad =int(edad)
#print(f'el participante se llama {nombre} y su tiene  {edad} anios')
#if edad>=18:
    #print('Eres mayor de edad y puedes votar')
#else:
    #print(f'Tienes {edad} anios y no puedes votar aguanta pueblo')

#en caso que el usuario ingrese algo diferente a un numero

edad = input('cual es tu edad?')
try:
    edad= int(edad)
    if edad>=18:
        print(f'tienes {edad} anio y puedes votar por ser mayor de edad')
    else:
        print('aun no tienes la edad para votar')

except ValueError:
    print('Por favor ingresa una edad valida')