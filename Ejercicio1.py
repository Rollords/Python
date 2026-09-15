#Crea un programa que permita registrar productos en una lista dentro de un diccionario llamado inventario. 
#El usuario debe poder ingresar nombres de productos de forma continua hasta que escriba la palabra "fin" (sin importar si la escribe en mayúsculas o minúsculas). Al finalizar, muestra el total de productos registrados.

inventario = {}

inventario['productos'] = []
cuenta = []

productos = {
    'leche': 10,
    'huevo': 5,
    'pollo': 20,
    'carne': 25,
    'queso': 7,
    'caraota': 5,
    'pescado': 20,
    'refresco': 10,
    'agua': 3,
    'manzana': 5,
    'pera': 7,
    'cambur': 10,
    'platano': 5,
}
def app():

    nombre_carrito= True

    while nombre_carrito:

        nombre = input('Que nombre le quieres poner a tu carrito de compras? :D \n')
        for producto in productos.keys():
            print(producto)

        if nombre:

            inventario['nombre'] = nombre

            nombre_carrito= False

            agregar_producto()

            mostrar_producto()

def agregar_producto():

    print('Estas en tu carrito', inventario['nombre'],' que compraras hoy? :D')

    while True:
        producto= input('Que producto vas a agregar?, escribe "fin" para terminar de comprar:').strip()

        if producto.lower()== 'fin':
            break

        if producto in productos.keys():
            cuenta.append(productos[producto])
        inventario['productos'].append(producto)
        print(f'Producto agregado:{producto}\n')

    print('Carrito Completo')
    

def mostrar_producto():
    print(f'Productos en el carrito:', len(inventario['productos']),'\r\n')
    

    for producto in inventario['productos']:
        print(producto)
    print(f'Total: {sum(cuenta)}$ a pagar') 
app() 

