#CONDICIONALES AND Y OR
#AND REVISA QUE AMBAS CONDICIONES SEAN VERDADERAS
#OR REVISA QUE AL MENOS UNA SE CUMPLA

acceso_usuario= True
acceso_admin = False
if acceso_usuario and acceso_admin:
    print('ACCESO TOTAL')
elif acceso_usuario:
    print('el usuario esta autenticado')
else:
    print('el usuario no esta autenticado')