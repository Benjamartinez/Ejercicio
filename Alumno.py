def menu():
    print("1.- Ingresar Alumno: ")
    print("2.- Eliminar Alumno: ")
    print("3.- Ver listado de Alumno")
    print("4.- Salir y Guardar")


menu()
opcion = 0
while True:
    opcion = int(input("Ingrese Opción: "))
    if opcion == 1:
        print("Prueba opcion Ingreso")
    elif opcion == 2:
        print("Prueba Eliminar Alumno")
    elif opcion == 3:
        print("Prueba Listado de Alumno")
    elif opcion == 4:
        print("Saliendo del programa...")
        break
    else:
        print("Opcion errónea.")