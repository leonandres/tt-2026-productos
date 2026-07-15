def menu():
    print("==== Menú de opciones ====")
    print("1 - Agregar producto")
    print("2 - Mostrar productos")
    print("3 - Buscar producto")
    print("4 - Eliminar producto")
    print("5 - Salir")

def agregar_producto():
    print("==== Agregar nuevo producto ====")

    nombre = input("Ingrese el nombre del producto:")
    if nombre.strip() == "":
        print("Error: El nombre del producto no puede estar vacío.")
        return
    categoria = input("Ingrese la categoría del producto:")
    if categoria.strip() == "":
        print("Error: La categoría del producto no puede estar vacía.")
        return
    precio = input("Ingrese el precio del producto:")
    if precio.strip() == "":
        print("Error: El precio del producto no puede estar vacío.")
        return
    else:
        with open("productos.txt", "a") as productos:
            productos.write(f"{nombre},{categoria},{precio}\n")

while True:
    menu()
    operacion = input("Seleccione una operación:")

    if not operacion.isdigit():
        print("Error: la operación debe ser un número entre 1 y 5.")
        continue

    operacion_int = int(operacion)

    if operacion_int == 1:
        agregar_producto()

