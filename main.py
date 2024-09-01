from modules import (createBook, createUser, createContact, 
                     deleteBook, deleteContact, deleteUser, 
                     getContacts, getBooks, getUsers,
                     updateBook, updateContact, updateUser, createMeetingPoint, getMeetingPoints, updateMeetingPoint)

def main():
    while True:
        print('MENU PRINCIPAL')
        print('1. Crear Usuario')
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

        choice = input("Selecciona una opción: ")

        if choice == '1':
            if createUser():
                print("------------------------------------------")
                print("-----Se creó el usuario correctamente-----")
                print("------------------------------------------")
        elif choice == '2':
            createContact()
        elif choice == '3':
            createBook()
        elif choice == '4':
            deleteUser()
        elif choice == '5':
            deleteContact()
        elif choice == '6':
            deleteBook()
        elif choice == '7':
            getUsers()
        elif choice == '8':
            print(getContacts())
        elif choice == '9':
            print(getBooks())
        elif choice == '10':
            updateUser()
        elif choice == '11':
            updateContact()
        elif choice == '12':
            updateBook()
        elif choice == '13':
            createMeetingPoint()
        elif choice == '14':
            getMeetingPoints()
        elif choice == '15':
            updateMeetingPoint()
        elif choice == '16':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

if __name__ == "__main__":
    main()
