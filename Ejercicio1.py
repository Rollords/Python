#Crea un programa que permita registrar productos en una lista dentro de un diccionario llamado inventario. 
#El usuario debe poder ingresar nombres de productos de forma continua hasta que escriba la palabra "fin" (sin importar si la escribe en mayúsculas o minúsculas). Al finalizar, muestra el total de productos registrados.

inventario = {}

inventario['productos'] = []
cuenta = []

productos =[
    {'id': 0, 'nombre':'leche','precio': 10},
    {'id': 1,'nombre':'huevo','precio': 5},
    {'id': 2,'nombre':'pollo','precio': 20},
    {'id': 3,'nombre':'carne','precio': 25},
    {'id': 4,'nombre':'queso','precio': 7},
    {'id': 5,'nombre':'caraota','precio': 5},
    {'id': 6,'nombre':'pescado','precio': 20},
    {'id': 7,'nombre':'refresco','precio': 10},
    {'id': 8,'nombre':'agua','precio': 3},
    {'id': 9,'nombre':'manzana','precio': 5},
    {'id': 10,'nombre':'pera','precio': 7},
    {'id': 11,'nombre':'cambur','precio': 10},
    {'id': 12,'nombre':'platano','precio': 5}
    ]
    
def app():

    nombre_carrito= True

    while nombre_carrito:

        nombre = input('Que nombre le quieres poner a tu carrito de compras? :D \n')
        for producto in productos:
            print(f'ID: {producto['id']} - {producto['nombre']} precio: {producto['precio']}$')

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

        for articulo in productos:
            if articulo['nombre'] == producto:
                print(producto)
                cuenta.append(articulo['precio'])
                break
        inventario['productos'].append(producto)
        print(f'Producto agregado:{producto}\n')

    print('Carrito Completo')
    

def mostrar_producto():
    print(f'Productos en el carrito:', len(inventario['productos']),'\r\n')
    

    for producto in inventario['productos']:
        print(producto)
    print(f'Total: {sum(cuenta)}$ a pagar') 
app() 

