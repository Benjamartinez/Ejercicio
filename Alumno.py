import csv

filename = 'Alumnos.csv'

def menu():
    print("")
    print("")
    print("1.- Ingresar Alumno ")
    print("2.- Eliminar Alumno ")
    print("3.- Ver listado de Alumno")
    print("4.- Salir y Guardar")
    print("")
    print("")

def agregar_alumno():
    nombre = input("Ingrese el NOMBRE del alumno: ")
    print("")
    rut = input("Ingrese el RUT del alumno: ")
    print("")
    if any(alumno[1] == rut for alumno in alumnos):
        print(f"El RUT {rut} ya existe. Intente con un RUT diferente.")
    else:
         nota = input("Ingrese la NOTA del alumno: ")
         return[nombre, rut,nota]

def eliminar_alumno(rut, alumnos):
    for i in range(len(alumnos)):
        if alumnos[i][1] == rut:
            del alumnos[i]
            return True
    return False

def leer_csv(filename):
    with open(filename,mode='r', newline='') as file:
        reader = csv.reader(file)
        data = [row for row in reader if row and len(row) == 3]
    return data

alumnos = leer_csv(filename)


while True:
    menu()
    opcion = int(input("Ingrese Opción: "))
    if opcion == 1:
        while True:
            Alumno = agregar_alumno()
            alumnos.append(Alumno)
            continuar = input("Desea agregar otro alumno?\n1.- Si\n2. No\n")
            if continuar != '1':
                break
    elif opcion == 2:
         rut = input("\nIngrese el RUT del Alumno que desea eliminar: \n")
         if eliminar_alumno(rut, alumnos):
             print(f"El Alumno {rut} ha sido eliminado.")
         else:
             print(f"El Alumno {rut} no se encuentra ingresado.")  
    elif opcion == 3:
        print("\nListado de Alumnos: ")
        for alumno in alumnos:
            print(alumno)
    elif opcion == 4:
        print("Saliendo del programa...")
        break
    else:
        print("Opcion errónea.")



with open(filename, mode='w',newline='')as file:
    writer = csv.writer(file)
    writer.writerows(alumnos)