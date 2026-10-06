libros_tupla = [
    {
        "id": 0,
        "isbn": "978-84-376-0494-7",
        "titulo": "Don Quijote de la Mancha",
        "autor": "Miguel de Cervantes",
        "ano": 2005,
        "editorial": "Cátedra",
        "categoria": "Novela",
        "activo": 'Disponible'
    },
    {
        "id": 1,
        "isbn": "978-84-9838-149-8",
        "titulo": "La sombra del viento",
        "autor": "Carlos Ruiz Zafón",
        "ano": 2001,
        "editorial": "Planeta",
        "categoria": "Misterio",
        "activo": 'Disponible'
    },
    {
        "id": 2,
        "isbn": "978-03-0747-472-8",
        "titulo": "Cien años de soledad",
        "autor": "Gabriel García Márquez",
        "ano": 2007,
        "editorial": "Random House",
        "categoria": "Realismo mágico",
        "activo": 'Disponible'
    },
    {
        "id": 3,
        "isbn": "978-84-204-7183-9",
        "titulo": "El principito",
        "autor": "Antoine de Saint-Exupéry",
        "ano": 1951,
        "editorial": "Salamandra",
        "categoria": "Fábula",
        "activo": 'Disponible'
    },
    {
        "id": 4,
        "isbn": "978-84-670-3397-7",
        "titulo": "El código Da Vinci",
        "autor": "Dan Brown",
        "ano": 2003,
        "editorial": "Planeta",
        "categoria": "Thriller",
        "activo": 'Disponible'
    },
    {
        "id": 5,
        "isbn": "978-84-9793-049-9",
        "titulo": "El alquimista",
        "autor": "Paulo Coelho",
        "ano": 1988,
        "editorial": "Grijalbo",
        "categoria": "Ficción",
        "activo": 'Disponible'
    },
    {
        "id": 6,
        "isbn": "978-84-0808-992-6",
        "titulo": "Los pilares de la tierra",
        "autor": "Ken Follett",
        "ano": 2010,
        "editorial": "Plaza & Janés",
        "categoria": "Novela",
        "activo": 'Disponible'
    },
    {
        "id": 7,
        "isbn": "978-84-1620-807-7",
        "titulo": "Sapiens: De animales a dioses",
        "autor": "Yuval Noah Harari",
        "ano": 2014,
        "editorial": "Debate",
        "categoria": "Historia",
        "activo": 'Disponible'
    },
    {
        "id": 8,
        "isbn": "978-84-450-7176-2",
        "titulo": "El Hobbit",
        "autor": "J. R. R. Tolkien",
        "ano": 1937,
        "editorial": "Minotauro",
        "categoria": "Fantasía",
        "activo": 'Disponible'
    },
    {
        "id": 9,
        "isbn": "978-84-339-2042-3",
        "titulo": "Ensayo sobre la ceguera",
        "autor": "José Saramago",
        "ano": 1995,
        "editorial": "Alfaguara",
        "categoria": "Ficción",
        "activo": 'Disponible'
    }
]

datos = ['nombre', 'apellido','cedula','correo']
resultado = {}

inventario = {
    'datos_usuario': resultado,
    'libros': [],
}



def biblioteca ():
    for dato in datos :
        resultado[dato] = input(f'Cual es tu {dato}: ')
       
    print(f'\nBienvenido {inventario["datos_usuario"]['nombre']} que deseas hacer: \n')
    cedula = inventario["datos_usuario"]['cedula']
    nombre = inventario["datos_usuario"]['nombre']

    def menu():
        while True:
            print("1. Ver todos los libros")
            print("2. Pedir un libro")
            print("3. Devolver un libro")
            print("4. Ver historial de préstamos")
            print("5. Salir")
            
            opcion = input("\nSeleccione una opción (1-5): ").strip()

            if opcion == "1":
                for i , libro in enumerate(libros_tupla):
                    if libro['activo'] == 'Disponible':
                        print(f'{i} - {libro['titulo']} Autor: {libro['autor']} - Status {libro['activo']}')
                salir = input(f'\nEscribe "salir" para volver al menu \n')
                if salir == 'salir':
                    print('\n')
                    menu()
                    break
            elif opcion == "2":
                while True:
                    disponibles = [lib for lib in libros_tupla if lib["activo"] == "Disponible"]
                    
                    if not disponibles:
                        print("\nYa no hay más libros disponibles en la biblioteca.\n")
                        break

                    for lib in disponibles:
                        print(f"ID: {lib['id']} - {lib['titulo']} ({lib['categoria']})")

                    entrada = input("\nIngresa el ID del libro que deseas pedir (o escribe 'salir' para salir al menú): ")

                    if entrada == "salir":
                        print("\nVolviendo al menú principal...\n")
                        break

                    pedir_id = int(entrada)
                    encontrado = False
                    if len(inventario['libros']) <= 2 :
                        for libro in libros_tupla:
                            if libro["id"] == pedir_id and libro["activo"] == "Disponible":
                                libro["activo"] = "Prestado"
                                inventario["libros"].append(libro)
                                print(f"\nHas pedido pedido: '{libro['titulo']}'\n")
                                encontrado = True
                                break
                    if not encontrado:
                        print("\n❌ El ID ingresado no está disponible o ya cumpliste tu cuota de 3 libros.\n")

            elif opcion == "3":
                while True:
                    for lib in inventario['libros']:
                        print(f"ID: {lib['id']} - {lib['titulo']} ({lib['categoria']})")

                    text = input("\nIngresa el ID del libro que deseas devolver (o escribe 'salir' para salir al menú): ")
                    if text == 'salir':
                        print("\nVolviendo al menú principal...\n")
                        break

                    devolver_libro = int(text)

                    for libro in inventario["libros"]:
                        if libro["id"] == devolver_libro:
                            libro["activo"] = "Disponible"
                            inventario["libros"].remove(libro)
                            print(f"\nHas pedido Devuelto: '{libro['titulo']}'\n")
                        else:
                            print("\n❌Escribe un ID valido\n")
                        break

            elif opcion == "4":
                print(f'\nUsuario: {nombre} - Cedula: {cedula}.')
                for titulo in inventario['libros']:
                    print(titulo['titulo'])
                print(f'Posee: {len(inventario['libros'])} en su poder.\n')

                print("\n--- VOLVIENDO AL MENU ---\n")
                menu()
                break
            else:
                print(f'\n❌ Opción no válida. Intente de nuevo. \n')
    menu()
        
biblioteca()