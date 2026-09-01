#operadores de comparacion 

# == Igual a
# != diferente de 
# < menor que 
# > mayor que 
# <= menor igual que 
# >= mayor igual que 

a=5
b=3
es_igual = a != b
mayor = a >= b

ahorro = 10
if ahorro >= 50:
    print('Nos vamos a la playa')
else:
    print('pa la casaa')


lenguaje = 'python'

if not lenguaje == 'python':
    print(f'Super eres un crack de {lenguaje}')
else:
    print(f'debes estudiar el mas {lenguaje}')  

#booleanos  
usuario_autenticado = True
if usuario_autenticado:
    print('el usuario esta autenticado')
else:
    print('no tienes acceso a la plataforma')

#condicional con list
superheroes = ['batman','spiderman','superman','capitan america','linterna verde']

if 'batman' in superheroes:
    print('amas a superman')
else:
    print('debes buscar un super que admirar, no puedes seguir asi jajaja')


roles = ['Admin','Usuario','Super_admin','Jefazo','Invitado' ]

if 'Jefazo' in roles:
    print('Eres el mero mero :v')
else:
    print('Vaya por donde vino (y)') 



acceso_usuario = False
acceso_admin = True
if acceso_usuario:
    if acceso_admin:
        print('acceso total')
    else:
        print('el usuario no es admin')
else:
    print('no tiene acceso')