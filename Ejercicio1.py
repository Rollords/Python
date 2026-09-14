#Crea un programa que permita registrar productos en una lista dentro de un diccionario llamado inventario. 
#El usuario debe poder ingresar nombres de productos de forma continua hasta que escriba la palabra "fin" (sin importar si la escribe en mayúsculas o minúsculas). Al finalizar, muestra el total de productos registrados.

inventario = {}

inventario['productos'] = [] 



def app():

    nombre_carrito= True

    while nombre_carrito:

        nombre = input('Que nombre le quieres poner a tu carrito de compras? :D \n')

        if nombre:

            inventario['nombre'] = nombre

            nombre_carrito= False

            agregar_producto()

            mostrar_producto()

def agregar_producto():

    print('Estas en tu carrito', inventario['nombre'],' que compraras hoy? :D')

    while True:
        producto= input('Que producto vas a agregar?, escribe "fin" para terminar de comprar:\n')

        if producto.lower()== 'fin' or producto.upper()== 'FIN':
            break

        inventario['productos'].append(producto)

        print('Producto agregado:\n', producto)

    print('Carrito Completo')
    

def mostrar_producto():
    print(f'Productos en el carrito:', len(inventario['productos']),'\r\n')

    for producto in inventario['productos']:
        print(producto)
        
app() 

