from crudUsuarios import crudUsuarios
from gestionAccesos import gestionAccesos
from DataScience import cargar_datos_pluviales, analizar_ano, analizar_mes, graficar_ano, graficar_mes
from ordenamiento import bubbleSort, sortUsersPy
from consultasSQL import mostrar_libros_por_genero, insertar_usuario, actualizar_telefono_usuario, eliminar_libro, consultar_join_usuario_libro, consultar_join_punto_encuentro

def mainMenu():
    userManager = crudUsuarios() 
    accessManager = gestionAccesos()
    sortedList = False

    while True:
        print("\n--- Opciones del menu principal ---")
        print("1. Agregar Usuario")
        print("2. Modificar Usuario")
        print("3. Eliminar Usuario")
        print("4. Buscar Usuario por username")
        print("5. Mostrar todos los Usuarios")
        print("6. Ingresar al Sistema")
        print("7. Ordenamiento de usuarios")
        print("8. Conexión con base de datos de 'Sharing books'")
        print("9. Analisis de datos")
        print("10. Buscar usuario por dni")
        print("11. Salir")

        userChoise1 = input("Seleccione una opcion: ")

        if userChoise1 == '1':
            username = input("Ingrese el username: ")
            password = input("Ingrese la password: ")
            email = input("Ingrese el E-mail: ")
            DNI = input("Ingrese el DNI: ")
            userManager.addUser(username, password, email, DNI)
            sortedList = False  

        elif userChoise1 == '2':
            id_input = input("Ingrese el ID del usuario a modificar: ")
            try:
                id = int(id_input)
                username = input("Ingrese el nuevo username: ")
                password = input("Ingrese la nueva Password: ")
                email = input("Ingrese el nuevo E-mail: ")
                userManager.modifyUser(id, username, password, email)
                sortedList = False 
            except ValueError:
                print("ID inválido.")

        elif userChoise1 == '3':
            identifier = input("Ingrese el username o E-mail del usuario a eliminar: ")
            userManager.deleteUser(identifier)
            sortedList = False

        elif userChoise1 == '4':
            identifier = input("Ingrese el Username o E-mail a buscar: ")

            
            if not sortedList:
                usuario = userManager.findUser(identifier)
                if usuario:
                    print(f'{usuario} - Busqueda realizada por técnica secuencial.')
                else:
                    print('Usuario no encontrado.')
            else:
                usuarios_ordenados = list(userManager.usuarios.values())
                usuario = busqueda_binaria(usuarios_ordenados, identifier)
                if usuario:
                    print(f'{usuario} - Busqueda realizada por técnica binaria.')
                else:
                    print('Usuario no encontrado.')

        elif userChoise1 == '5':
            userManager.showUser()

        elif userChoise1 == '6':
            username = input("Ingrese el username: ")
            usuario = userManager.findUser(username)
            if usuario:
                password = input("Ingrese la password: ")
                if usuario.password == password:
                    print(f"Ingreso exitoso como {usuario.username}.")
                    accessManager.registerAccess(usuario, True)
                else:
                    print("Clave incorrecta.")
                    accessManager.registerAccess(usuario, False, password)
            else:
                print("Usuario no encontrado.")
                accessManager.registerAccess(username, False)

        elif userChoise1 == '7':
            while True:
                print("\n--- Submenú de Ordenamiento ---")
                print("1. Ordenar usuarios por algoritmo bubbleSort")
                print("2. Ordenar usuarios por método sort()")
                print("3. Regresar al menú principal")
                userChoise2 = input("Seleccione una opción: ")

                if userChoise2 == '1':
                    usuarios_ordenados = userManager.usuarios.values()
                    usuarios_ordenados = bubbleSort(list(usuarios_ordenados))
                    userManager.usuarios = {user.id: user for user in usuarios_ordenados}
                    sortedList = True
                    print("Usuarios ordenados por el algoritmo bubbleSort y guardados exitosamente.")

                elif userChoise2 == '2':
                    usuarios_ordenados = userManager.usuarios.values()
                    usuarios_ordenados = list(usuarios_ordenados)
                    sortUsersPy(usuarios_ordenados)
                    userManager.usuarios = {user.id: user for user in usuarios_ordenados}
                    sortedList = True
                    print("Usuarios ordenados por método sort() y guardados con éxito.")

                elif userChoise2 == '3':
                    break

                else:
                    print("Opción no válida. Intente nuevamente.")
        
        elif userChoise1 == '8':
            
            while True:
                print("\n--- Submenu Sharing Books ---")
                print("1. Ver libros por genero")
                print("2. Insertar nuevo usuario")
                print("3. Actualizar telefono de usuario")
                print("4. Eliminar un libro")
                print("5. Consultar JOIN de usuarios y libros")
                print("6. Consultar JOIN de domicilio y punto de encuentro")
                print("7. Regresar al menú principal")

                userChoise3 = input("Seleccione una opción: ")

                if userChoise3 == '1':
                    genero = input("Ingrese el género de libros a consultar (por ejemplo: 'ciencia ficcion'): ")
                    mostrar_libros_por_genero(genero)
                
                elif userChoise3 == '2':
                    insertar_usuario()

                elif userChoise3 == '3':
                    id_usuario = int(input("Ingrese el ID del usuario a actualizar: "))
                    nuevo_telefono = input("Ingrese el nuevo teléfono: ")
                    actualizar_telefono_usuario(id_usuario, nuevo_telefono)

                elif userChoise3 == '4':
                    id_libro = int(input("Ingrese el ID del libro a eliminar: "))
                    eliminar_libro(id_libro)

                elif userChoise3 == '5':
                    consultar_join_usuario_libro()

                elif userChoise3 == '6':
                    consultar_join_punto_encuentro()

                elif userChoise3 == '7':
                    break
                else:
                    print("Opción no válida. Intente nuevamente.")
        
        elif userChoise1 == '9':
            ano = int(input("Ingrese el año que desea analizar: "))
            df = cargar_datos_pluviales(ano)
            
            print("\nAnalisis del año completo: ")
            analizar_ano(df)
            graficar_ano(df, ano)
            
            mes = input("\nIngrese el mes que desea analizar (Ejemplo: Enero): ")
            print(f"\nAnálisis del mes de {mes}:")
            analizar_mes(df, mes)
            graficar_mes(df, mes, ano)
        
        elif userChoise1 == '10':
            dni = input("Ingrese el DNI a buscar: ")
            usuario = userManager.findUserByDni(dni)
            if usuario:
                print(usuario, "se encontró el usuario por DNI, usando búsqueda binaria.")
            else:
                print("Usuario no encontrado.")
        
        elif userChoise1 == '11':
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intente nuevamente por favor.")



def busqueda_binaria(usuarios_list, username):
    low = 0
    high = len(usuarios_list) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_username = usuarios_list[mid].username

        if mid_username == username:
            return usuarios_list[mid]
        elif mid_username < username:
            low = mid + 1
        else:
            high = mid - 1

    return None


if __name__ == "__main__":
    mainMenu()