#OPERADORES DE COMPARACIOM
# == IGUAL  A
# != DIFERENTE DE 
# < MENOR QUE
# >  MAYOR QUE
# <= MENOR IGUAL QUE
# >= MAYOR IGUAL QUE 

a = 5
b= 3
es_igual = a !=  b #true
mayor= a >=b #True

ahorro = 10
if ahorro >= 50:
    print('nos vamos para la playita')
else:
    print('nos quedamos en la casa')

#condicional negando cuando trabajamos string     
lenguaje = 'php'
if not lenguaje == 'python':
    print(f'super eres un crack de {lenguaje}')
else:
    print(f'debes estudiar el mas {lenguaje}')
    
#booleanos
usuario_autenticado = True
if usuario_autenticado:
    print('el usuario esta autenticado')
else:
    print('no tienes acceso a la plataforma')
    
#condicional con list
superheroes = ['batman', 'spiderman', 'superman', 'capitan america', 'linterna verde']
if 'batman2' in superheroes:
    print ('eres un super')
else:
    print('debes buscar un super que admirar, no puedes seguir asi jajaaj')
    
#anidar condicionales

acceso_usuario = False
acceso_admin = True
if acceso_usuario:
    if acceso_admin:
        print('acceso total')
    else:
        print('el usuario  no es admin')
else:
    print('no tiene acceso')
    

