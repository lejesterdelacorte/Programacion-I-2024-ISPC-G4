from modules import (createBook, createUser, createContact, 
                     deleteBook, deleteContact, deleteUser, 
                     getContacts, getBooks, getUsers,
                     updateBook, updateContact, updateUser,
                     createMeetingPoint, getMeetingPoints, updateMeetingPoint,
                     generate_captcha, login, resetPassword)

def main():

    isUserLogged = False
    isMenuLogin = True
    showResetPassword = False

    while isMenuLogin:
        print('LOGIN USUARIO')
        print('0. Ingresar usuario')
        print('1. Crear Usuario')
        if showResetPassword:
            print('2. Resetear contraseña')

        choice = input("Selecciona una opción: ")
        if choice == '0':
            print("Ingresar capcha")
            generate_captcha()
            if login():
                print("Usuario logueado correctamente")
                isUserLogged = True
                isMenuLogin = False
            else:
                print("Usuario o contraseña incorrectos")
                showResetPassword = True
            

        elif choice == '1':
            if createUser():
                print("------------------------------------------")
                print("-----Se creó el usuario correctamente-----")
                print("------------------------------------------")
        
        elif choice == '2' and showResetPassword:
            resetPassword()
            showResetPassword = False

        else:
            print("Opción no válida, por favor intenta de nuevo.")
            
        
            

    while isUserLogged:
        print('MENU PRINCIPAL')
        
        print('2. Crear Contacto')
        print('3. Crear Libro')
        print('4. Eliminar Usuario')
        print('5. Eliminar Contacto')
        print('6. Eliminar Libro')
        print('7. Obtener Usuarios')
        print('8. Obtener Contactos')
        print('9. Obtener Libros')
        print('10. Actualizar Usuario')
        print('11. Actualizar Contacto')
        print('12. Actualizar Libro')
        print('13. Crear Punto de Encuentro')
        print('14. Obtener Punto de Encuentro')
        print('15. Actualizar Punto de Encuentro')
        print('16. Salir del Menu')

        MenuChoice = input("Selecciona una opción: ")

        
        if MenuChoice == '3':
            createBook()
        elif MenuChoice == '4':
            deleteUser()
        elif MenuChoice == '5':
            deleteContact()
        elif MenuChoice == '6':
            deleteBook()
        elif MenuChoice == '7':
            getUsers()
        elif MenuChoice == '8':
            print(getContacts())
        elif MenuChoice == '9':
            print(getBooks())
        elif MenuChoice == '10':
            updateUser()
        elif MenuChoice == '11':
            updateContact()
        elif MenuChoice == '12':
            updateBook()
        elif MenuChoice == '13':
            createMeetingPoint()
        elif MenuChoice == '14':
            getMeetingPoints()
        elif MenuChoice == '15':
            updateMeetingPoint()
        elif MenuChoice == '16':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

if __name__ == "__main__":
    main()
