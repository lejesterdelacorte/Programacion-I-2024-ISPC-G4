from modules import (createBook, registerForm, createContact, 
                     deleteBook, deleteContact, 
                     getContacts, getBooks, 
                     updateBook, updateContact, createMeetingPoint, getMeetingPoints, updateMeetingPoint)

def main():
    while True:
        print('MENU PRINCIPAL')
        print('1. Crear Usuario')
        print('2. Crear Contacto')
        print('3. Crear Libro')
        print('4. Eliminar Contacto')
        print('5. Eliminar Libro' )
        print('6. Obtener Contactos')
        print('7. Obtener Libros')
        print('8. Actualizar Contacto')
        print('9. Actualizar Libro')
        print('10. Crear Punto de Encuentro')
        print('11. Obtener Punto de Encuentro')
        print('12. Actualizar Punto de Encuentro')
        print('13. Salir del Menu')

        choice = input("Selecciona una opción: ")

        if choice == '1':
            registerForm()
        elif choice == '2':
            createContact()
        elif choice == '3':
            createBook()
        elif choice == '4':
            deleteContact()
        elif choice == '5':
            deleteBook()
        elif choice == '6':
            print(getContacts())
        elif choice == '7':
            print(getBooks())
        elif choice == '8':
            updateContact()
        elif choice == '9':
            updateBook()
        elif choice == '10':
            createMeetingPoint()
        elif choice == '11':
            getMeetingPoints()
        elif choice == '12':
            updateMeetingPoint()
        elif choice == '13':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

if __name__ == "__main__":
    main()
