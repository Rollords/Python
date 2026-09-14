playlist = {}

playlist['canciones'] = [] #crear un diccionario  



def app(): #funcion principal

    agregar_playlist= True

    while agregar_playlist:

        nombre_playlist = input('Como deseas nombrar tu playlist\n')

       

        if nombre_playlist:

            playlist['nombre'] = nombre_playlist

            agregar_playlist = False

            agregar_canciones()

            mostrar_resumen()

           

def agregar_canciones():

    print('Agregando canciones a la playlist', playlist['nombre'])

    while True:

        cancion = input('ingresa el nombre de la cancion o presiona X para salir:')

        if cancion.lower()== 'x':

            break

       

        playlist['canciones'].append(cancion)

       

        print('Cancion Agregada', cancion)

       

    print('Playlist completa')

    print(playlist)



def mostrar_resumen():

    print(f'Playlist', playlist['nombre'])

    print(f'Canciones de la Playlist \r\n')

    for cancion in playlist['canciones']:

      print(cancion)

app();

