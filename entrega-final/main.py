def menu():
    print("\033[1;36m==== Menú de opciones ====\033[0m")
    print("1 - Agregar producto")
    print("2 - Mostrar productos")
    print("3 - Buscar producto")
    print("4 - Salir")

def agregar_producto():
    print("==== Agregar nuevo producto ====")

    nombre = input("Ingrese el nombre del producto: ")
    if nombre.strip() == "":
        print("Error: El nombre del producto no puede estar vacío.")
        return
    categoria = input("Ingrese la categoría del producto: ")
    if categoria.strip() == "":
        print("Error: La categoría del producto no puede estar vacía.")
        return
    precio = input("Ingrese el precio del producto: ")
    if precio.strip() == "":
        print("Error: El precio del producto no puede estar vacío.")
        return

    with open("productos.txt", "a") as productos:
        productos.write(f"{nombre},{categoria},{precio}\n")

def mostrar_productos():
    try:
        with open("productos.txt","r") as productos:
            print("==== Mostrar productos ====")
            for producto in productos:
                nombre, categoria, precio = producto.strip().split(",")
                print(f"Nombre: {nombre}, Categoría: {categoria}, Precio: {precio}")

    except FileNotFoundError:
        print("No hay productos registrados.")


def buscar_producto():
    print("==== Buscar producto ====")
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
    if nombre_buscar.strip() == "":
        print("Error: El nombre del producto no puede estar vacío.")
        return

    try:
        with open("productos.txt","r") as productos:
            encontrado = False
            for producto in productos:
                nombre, categoria, precio = producto.strip().split(",")
                if nombre.lower() == nombre_buscar.lower():
                    print(f"Producto encontrado: Nombre: {nombre}, Categoría: {categoria}, Precio: {precio}")
                    encontrado = True
                    break
            if not encontrado:
                print("Producto no encontrado.")

    except FileNotFoundError:
        print("No hay productos registrados.")

while True:
    menu()
    operacion = input("Seleccione una operación: ")

    if not operacion.isdigit():
        print("Error: la operación debe ser un número entre 1 y 5.")
        continue

    operacion_int = int(operacion)

    if operacion_int == 1:
        agregar_producto()
    elif operacion_int == 2:
        mostrar_productos()
    elif operacion_int == 3:
        buscar_producto()
    elif operacion_int == 4:
        print("==== Saliendo del programa. Vuelva prontos. ====")
        break