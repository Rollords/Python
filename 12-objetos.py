#diccionarios
cancion = {
    'artista': 'Ricardo Arjona',
    'nombre': 'el problema'
}

print(cancion['artista'])
artista = cancion['artista']
print(artista) # ricaardo arjona 


#agregar una llave a mi diccionario
cancion['playlis_id'] = 'Romanticas'
print(cancion)

#eliminar una llave de mi diccionario
del cancion['playlis_id']
print (cancion)