def menu():
    print("==== Menú de opciones ====")
    print("1 -  Agregar producto")
    print("2 - Mostrar productos")
    print("3 - Buscar producto")
    print("4 - Eliminar producto")
    print("5 - Salir")

#def agregar_producto():


while True:
    menu()
    operacion = input("Seleccione una operación:")

    if operacion.isdigit():
        print("Error: la operación debe ser un número entre 1 y 5.")
        continue

    operacion_int = int(operacion)

    if operacion_int == 1:
        agregar_producto()

