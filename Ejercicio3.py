libros_tupla = [
    {
        "id": 0,
        "isbn": "978-84-376-0494-7",
        "titulo": "Don Quijote de la Mancha",
        "autor": "Miguel de Cervantes",
        "ano": 2005,
        "editorial": "Cátedra",
        "categoria": "Novela",
        "activo": True
    },
    {
        "id": 1,
        "isbn": "978-84-9838-149-8",
        "titulo": "La sombra del viento",
        "autor": "Carlos Ruiz Zafón",
        "ano": 2001,
        "editorial": "Planeta",
        "categoria": "Misterio",
        "activo": True
    },
    {
        "id": 2,
        "isbn": "978-03-0747-472-8",
        "titulo": "Cien años de soledad",
        "autor": "Gabriel García Márquez",
        "ano": 2007,
        "editorial": "Random House",
        "categoria": "Realismo mágico",
        "activo": True
    },
    {
        "id": 3,
        "isbn": "978-84-204-7183-9",
        "titulo": "El principito",
        "autor": "Antoine de Saint-Exupéry",
        "ano": 1951,
        "editorial": "Salamandra",
        "categoria": "Fábula",
        "activo": True
    },
    {
        "id": 4,
        "isbn": "978-84-670-3397-7",
        "titulo": "El código Da Vinci",
        "autor": "Dan Brown",
        "ano": 2003,
        "editorial": "Planeta",
        "categoria": "Thriller",
        "activo": True
    },
    {
        "id": 5,
        "isbn": "978-84-9793-049-9",
        "titulo": "El alquimista",
        "autor": "Paulo Coelho",
        "ano": 1988,
        "editorial": "Grijalbo",
        "categoria": "Ficción",
        "activo": True
    },
    {
        "id": 6,
        "isbn": "978-84-0808-992-6",
        "titulo": "Los pilares de la tierra",
        "autor": "Ken Follett",
        "ano": 2010,
        "editorial": "Plaza & Janés",
        "categoria": "Novela",
        "activo": True
    },
    {
        "id": 7,
        "isbn": "978-84-1620-807-7",
        "titulo": "Sapiens: De animales a dioses",
        "autor": "Yuval Noah Harari",
        "ano": 2014,
        "editorial": "Debate",
        "categoria": "Historia",
        "activo": True
    },
    {
        "id": 8,
        "isbn": "978-84-450-7176-2",
        "titulo": "El Hobbit",
        "autor": "J. R. R. Tolkien",
        "ano": 1937,
        "editorial": "Minotauro",
        "categoria": "Fantasía",
        "activo": True
    },
    {
        "id": 9,
        "isbn": "978-84-339-2042-3",
        "titulo": "Ensayo sobre la ceguera",
        "autor": "José Saramago",
        "ano": 1995,
        "editorial": "Alfaguara",
        "categoria": "Ficción",
        "activo": True
    }
]

datos = ['nombre', 'apellido','cedula','correo']

inventario = {
    'datos_usuario': datos,
    'libros': [],
}



def biblioteca ():
    libros_elegidos = True
    usuario= {}
    while libros_elegidos:
        for dato in datos:
            texto = input(f'Cual es tu {dato}: ').strip()
            usuario[dato] = texto
        print(f'Hola {usuario['nombre']} bienvenido a la Biblioteca a continuacion veras una lista de los libros que tenemos para ti : \n')


        for libro in libros_tupla:               
            print(f'ID: {libro['id']} - {libro['titulo']} - Autor: {libro['autor']} - Categoria: {libro['categoria']}')

        elegir = input(f'Que libro deseas agregar (maximo 3 libros)')

biblioteca()