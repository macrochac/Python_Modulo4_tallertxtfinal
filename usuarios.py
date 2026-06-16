from datetime import datetime
import os.path

ARCHIVO = "usuarios.txt"
ARCHIVO_VALIDAR = "usuarios.txt"

def agregar_usuario():
    try:
        nombre = input("\nIngrese el nombre del usuario: ").strip().lower()
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if nombre == "":
            print("\nEl nombre no puede estar vacio.\n")
            return
        if os.path.exists(ARCHIVO):
            with open(ARCHIVO, "r", encoding="utf-8") as archivo:
                lineas = archivo.readlines()
                if lineas:
                    for fila in lineas:
                            nombre1, edad1, fecha1 = fila.strip().split(",")
                            if nombre == nombre1:
                                print("\nUsuario ya esta registrado.")
                                return

        edad = int(input("Ingrese la edad del usuario: ").strip())
        if edad < 0:
            print("\nLa edad no puede ser negativa.\n")
            return
        with open(ARCHIVO, "a", encoding="utf-8") as archivo:
            archivo.write(f"{nombre},{edad},{fecha}\n")
        print("\nUsuario registrado exitosamente.\n")

    except ValueError:
        print("\nLa edad debe de ser numerica.\n")
    except PermissionError:
        print("\nNo se tienen permisos para escribir en el archivo.\n")
    except Exception as e:
        print(f"\nOcurrio un error inesperado: {e}\n")

def mostrar_usuarios():
        try:
            with open(ARCHIVO, "r", encoding="utf-8") as archivo:
                lineas = archivo.readlines()
                if not lineas:
                    print("\nNo hay usuarios registrados.\n")
                    return
                
                print("\nUsuarios Registrados:")

                for linea in lineas:
                    nombre, edad, fecha = linea.strip().split(",")
                    print(f"Nombre: {nombre}| Edad: {edad}|Fecha: {fecha}")
        except FileNotFoundError:
            print("\nNo se encontro el archivo de usuarios.\n")
        except PermissionError:
            print("\nNo se tienen permisos para leer en el archivo.\n")
        except Exception as e:
            print(f"\nOcurrio un error inesperado: {e}\n")
    
def buscar_usuario():
        nombre_a_buscar = input("\nIngrese nombre a buscar: ").strip().lower()
        if nombre_a_buscar=="":
            print("\nEl nombre a buscar debe ser diferente a vacio.\n")
            return
        try:
            with open(ARCHIVO, "r", encoding="utf-8") as archivo:
                lineas = archivo.readlines()
                if not lineas:
                    print("\nNo hay usuarios registrados.\n")
                    return
                print("\nBuscando Usuarios:")
                ok = False
                for fila in lineas:
                    nombre, edad, fecha = fila.strip().split(",")
                    encontrado = nombre.find(nombre_a_buscar)
                    if encontrado!=-1:
                        print(f"Nombre: {nombre}| Edad: {edad}|Fecha: {fecha}")
                        ok = True
                if ok==False:        
                    print("\nUsuario no enontrado.\n")

        except FileNotFoundError:
            print("\nNo se encontro el archivo de usuarios.\n")
        except PermissionError:
            print("\nNo se tienen permisos para leer en el archivo\n")
        except Exception as e:
            print(f"\nOcurrio un error inesperado: {e}\n")

def validar_archivo():
        errores = 0
        try:
            with open(ARCHIVO_VALIDAR, "r", encoding="utf-8") as archivo:
                lineas = archivo.readlines()
                if not lineas:
                    print("\nNo hay usuarios registrados.\n")
                    return

                for i, fila in enumerate(lineas, start=1):
                    variable = fila.strip().split(",")
                    nombre = variable[0]
                    edad1 = variable[1]
                    fecha = variable[2]
                    if nombre == '':
                        print(f"Registro: {i} -> Nombre: {nombre}| Edad: {edad1}|Fecha: {fecha}, Error: Nombre esta vacio")
                        errores += 1
                    if not edad1.isdigit():
                        print(f"Registro: {i} -> Nombre: {nombre}| Edad: {edad1}|Fecha: {fecha}, Error: la edad debe ser numeros enteros")
                        errores += 1
                    else:
                        edad = int(variable[1])
                        if edad == '':
                            print(f"Registro: {i} -> Nombre: {nombre}| Edad: {edad}|Fecha: {fecha}, Error: La edad esta vacia")
                            errores += 1
                        elif edad < 0:
                            print(f"Registro: {i} -> Nombre: {nombre}| Edad: {edad}|Fecha: {fecha}, Error: la edad no puede ser negativa")
                            errores += 1
                        elif edad > 120:
                            print(f"Registro: {i} -> Nombre: {nombre}| Edad: {edad}|Fecha: {fecha}, Error: Edad fuera de contexto, mayor de 120 años")
                            errores += 1
                    
                    
                if errores > 0:
                    print(f"\nErrores encontrados: {errores}")
                else:
                    print("\nNo se encontraron errores.")

        except FileNotFoundError:
            print("\nNo se encontro el archivo de usuarios.\n")
        except PermissionError:
            print("\nNo se tienen permisos para leer en el archivo\n")
        except Exception as e:
            print(f"\nOcurrio un error inesperado: {e}\n")

def crear_archivo_bueno(nombre, edad, fecha):
     with open("archivo_bueno.txt", "a", encoding="utf-8") as file:
            linea = f"{nombre},{edad},{fecha}\n"
            file.write(linea)

def crear_archivo_errores(nombre, edad, fecha, error):
     with open("archivo_con_errores.txt", "a", encoding="utf-8") as file:
            linea = linea = f"{nombre},{edad},{fecha},{error}\n"
            file.write(linea)

def crear_logs():
        try:
            with open(ARCHIVO_VALIDAR, "r", encoding="utf-8") as archivo:
                lineas = archivo.readlines()
                if not lineas:
                    print("\nNo hay usuarios registrados.\n")
                    return

                for fila in lineas:
                    ok = True
                    variable = fila.strip().split(",")
                    nombre = variable[0]
                    edad1 = variable[1]
                    fecha = variable[2]
                    if nombre == "":
                        crear_archivo_errores(nombre,edad1,fecha,"Error: Nombre esta vacio")
                        ok = False

                    if not edad1.isdigit():
                        crear_archivo_errores(nombre,edad1,fecha,"Error: la edad debe ser numeros enteros")
                        ok = False
                    else:
                        edad = int(variable[1])    
                        if edad == '':
                            crear_archivo_errores(nombre,edad,fecha,"Error: La edad esta vacia")
                            ok = False
                        elif edad < 0:
                            crear_archivo_errores(nombre,edad,fecha,"Error: la edad no puede ser negativa")
                            ok = False
                        elif edad > 120:
                            crear_archivo_errores(nombre,edad,fecha,"Error: Edad fuera de contexto, mayor de 120 años")
                            ok = False
                    if ok:
                        crear_archivo_bueno(nombre,edad,fecha)

            print("\nArchivos creados correctamente.\n")
            
        except FileNotFoundError:
            print("\nNo se encontro el archivo de usuarios.\n")
        except PermissionError:
            print("\nNo se tienen permisos para leer en el archivo\n")
        except Exception as e:
            print(f"\nOcurrio un error inesperado: {e}\n")     

def mostrar_menu():
    print("")
    print("=" * 26)
    print("----- MENU PRINCIPAL -----")
    print("=" * 26)
    print("1. Agregar usuarios.")
    print("2. Mostrar usuarios.")
    print("3. Buscar usuarios.")
    print("4. Validar archivo.")
    print("5. Crear archivo de errores.")
    print("6. Terminar el programa.\n")

def iniciar_programa():
    usuarios = []
    opcion = 0
    while opcion!=6:
        mostrar_menu()
        opcion = int(input("Seleccione una opcion (1-6): ").strip())
        if opcion==1:
            agregar_usuario()
        elif opcion == 2:
            mostrar_usuarios()
        elif opcion == 3:
            buscar_usuario()
        elif opcion == 4:
            validar_archivo()
        elif opcion == 5:
            crear_logs()
        elif opcion == 6:
            print("\nPrograma Terminado.\n")
        else:
            print("\nOpcion invalidad. Intente nuevamente.\n")

if __name__ == '__main__': iniciar_programa()

"""
Modificar el programa para:

Buscar usuarios. ok
---Evitar usuarios duplicados. ok
Validar un archivo al momento de leerlo y en caso de errores mortralos ok
Crear archivo de errores. Meter los datos buenos en un archivo y los malos en otro ok
---Registrar fecha y hora de creación. ok
"""
