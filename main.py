productos = []

def menu():
    print("1 - Agregar producto")
    print("2 - Mostrar productos")
    print("3 - Buscar producto")
    print("4 - Eliminar producto")
    print("5 - Salir")

def agregar_producto():
    print ("Agregar nuevo producto.")

def mostrar_productos():
    print("Mostrar productos.")

def buscar_producto():
    print("Buscar producto")

def eliminar_producto():
    print("Eliminar producto")

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
        break



