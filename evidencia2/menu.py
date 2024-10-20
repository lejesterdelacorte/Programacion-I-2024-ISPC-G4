from crudUsuarios import crudUsuarios
from gestionAccesos import gestionAccesos

def mainMenu():
    sistema_usuarios = crudUsuarios()
    sistema_accesos = gestionAccesos()

    while True:
        print("\n--- Opciones del menu principal ---")
        print("1. Agregar Usuario")
        print("2. Modificar Usuario")
        print("3. Eliminar Usuario")
        print("4. Buscar Usuario")
        print("5. Mostrar todos los Usuarios")
        print("6. Ingresar al Sistema")
        print("7. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            username = input("Ingrese el username: ")
            password = input("Ingrese la password: ")
            email = input("Ingrese el E-mail: ")
            sistema_usuarios.addUser(username, password, email)

        elif opcion == '2':
            id_input = input("Ingrese el ID del usuario a modificar: ")
            try:
                id = int(id_input)
                username = input("Ingrese el nuevo username: ")
                password = input("Ingrese la nueva Password: ")
                email = input("Ingrese el nuevo E-mail: ")
                sistema_usuarios.modifyUser(id, username, password, email)
            except ValueError:
                print("ID inválido.")

        elif opcion == '3':
            identifier = input("Ingrese el username o E-mail del usuario a eliminar: ")
            sistema_usuarios.deleteUser(identifier)

        elif opcion == '4':
            identifier = input("Ingrese el Username o E-mail a buscar: ")
            usuario = sistema_usuarios.findUser(identifier)
            if usuario:
                print(usuario)
            else:
                print("Usuario no encontrado.")

        elif opcion == '5':
            sistema_usuarios.showUser()

        elif opcion == '6':
            username = input("Ingrese el username: ")
            usuario = sistema_usuarios.findUser(username)
            if usuario:
                password = input("Ingrese la password: ")
                if usuario.password == password:
                    print(f"Ingreso exitoso como {usuario.username}.")
                    sistema_accesos.registerAccess(usuario, True)
                else:
                    print("Clave incorrecta.")
                    sistema_accesos.registerAccess(usuario, False, password)
            else:
                print("Usuario no encontrado.")

        elif opcion == '7':
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intente nuevamente por favor.")
