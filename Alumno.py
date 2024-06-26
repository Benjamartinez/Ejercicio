def menu():
    print("1.- Ingresar Alumno: ")
    print("2.- Eliminar Alumno: ")
    print("3.- Ver listado de Alumno")
    print("4.- Salir y Guardar")

menu()

alumnos = {
    "Nombre": "Pepe",
    "Rut": "12345678",
    "Nota": [7.0,4.0,6.5]
}
opcion = 0
while True:
    opcion = int(input("Ingrese Opción: "))
    if opcion == 1:
        print("Ingresando Alumno: ")   
    elif opcion == 2:
        print("Prueba Eliminar Alumno")
    elif opcion == 3:
        print("Verlistado de Alumno")
        print(alumnos)
    elif opcion == 4:
        print("Saliendo del programa...")
        break
    else:
        print("Opcion errónea.")

