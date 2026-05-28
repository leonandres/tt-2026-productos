productos = []

def menu():
    print("1 - Agregar producto")
    print("2 - Mostrar productos")
    print("3 - Buscar producto")
    print("4 - Eliminar producto")
    print("5 - Salir")

def agregar_producto():
    print ("==== Agregar nuevo producto ====")
    print("Ingrese el nombre del producto: ")
    nombre = input()
    print("Ingrese el precio del producto: ")
    precio = float(input())

    producto = {
        "nombre": nombre,
        "precio": precio
    }
    productos.append(producto)

def mostrar_productos():
    print("==== Mostrar productos ====")
    for producto in productos:
        print (f"Nombre: {producto['nombre']}, Precio: {producto['precio']}")

def buscar_producto():
    print("==== Buscar producto ====")
    print("Ingrese el nombre del producto a buscar: ")
    nombre = input()
    for producto in productos:
        if producto["nombre"] == nombre:
            print (f"Nombre: {producto['nombre']}, Precio: {producto['precio']}")
            return
    print("Producto no encontrado.")

def eliminar_producto():
    print("==== Eliminar producto ====")
    print("Ingrese el nombre del producto a eliminar: ")
    nombre_producto_a_eliminar = input()
    for producto in productos:
        if producto ["nombre"] == nombre_producto_a_eliminar:
            productos.remove(producto)
            print("Producto eliminado.")
            return
    print("Producto no encontrado.")

while True:
    menu()
    operacion = input ("Seleccione una opción: ")

    if operacion == "1":
        agregar_producto()
    elif operacion == "2":
        mostrar_productos()
    elif operacion == "3":
        buscar_producto()
    elif operacion == "4":
        eliminar_producto()
    elif operacion == "5":
        print("Saliendo del programa.")
        break
    else:
        print("Operación no válida. Intente nuevamente.")



