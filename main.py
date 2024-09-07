from modules import (createBook, deleteBook, createContact, 
                     deleteContact,
                     getContacts, getBooks,
                     updateBook, updateContact,
                     createMeetingPoint, getMeetingPoints, updateMeetingPoint,
                     login, resetPassword, registerForm)

def main():

    isUserLogged = False
    isMenuLogin = True
    showResetPassword = False

    while isMenuLogin:
        print('--- SHARING BOOKS - LOGIN USUARIO ---')
        print('1. Ingresar usuario')
        print('2. Crear Usuario')
        if showResetPassword:
            print('3. Resetear contraseña')
        print('0. Salir')
        
        choice = input("Selecciona una opción: ")
        if choice == '1':
            fails, logged = login()
            if logged:
                print("Usuario logueado correctamente")
                isUserLogged = True
                isMenuLogin = False
            else:
                print("Usuario o contraseña incorrectos")
                print(f"Usted lleva {fails} intentos fallidos de ingreso.\n Recuerde que al cuarto intento se bloquea...")
                showResetPassword = True
        elif choice == '2':
            registerForm()
        
        elif choice == '3' and showResetPassword:
            resetPassword()
            showResetPassword = False
        elif choice == '0':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

    while isUserLogged:
        print('--- SHARING BOOKS - MENU PRINCIPAL ---')
        print('1. Crear Contacto')
        print('2. Crear Libro')
        print('3. Eliminar Contacto')
        print('4. Eliminar Libro' )
        print('5. Obtener Contactos')
        print('6. Obtener Libros')
        print('7. Actualizar Contacto')
        print('8. Actualizar Libro')
        print('9. Crear Punto de Encuentro')
        print('10. Obtener Punto de Encuentro')
        print('11. Actualizar Punto de Encuentro')
        print('12. Salir del Menu')

        MenuChoice = input("Selecciona una opción: ")

        if MenuChoice == '1':
            createContact()
        elif MenuChoice == '2':
            createBook()
        elif MenuChoice == '3':
            deleteContact()
        elif MenuChoice == '4':
            deleteBook()
        elif MenuChoice == '5':
            print(getContacts())
        elif MenuChoice == '6':
            print(getBooks())
        elif MenuChoice == '7':
            updateContact()
        elif MenuChoice == '8':
            updateBook()
        elif MenuChoice == '9':
            createMeetingPoint()
        elif MenuChoice == '10':
            getMeetingPoints()
        elif MenuChoice == '11':
            updateMeetingPoint()
        elif MenuChoice == '12':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

if __name__ == "__main__":
    main()
