from ..utils.dBConnection import DatabaseConnection
from ..address.createAddress import createAddress


def updateMeetingPoint():
    print("Actualizar Punto de Encuentro")

    db_instance = DatabaseConnection()
    connection = db_instance.get_connection()

    print("--------NUEVO DOMICILIO DEL PUNTO DE ENCUENTRO-------")
    street = input("Ingrese la Calle: ")
    street_number = input("Ingrese la Altura: ")
    city = input("Ingrese la Ciudad: ")
    country = input("Ingrese el País: ")
    address_id = createAddress(street, street_number, city, country)

    meetingId = input("Ingrese el ID del punto de encuentro a actualizar: ")
    newName = input("Ingrese el nuevo nombre del punto de encuentro: ")
    newDescription = input("Ingrese la nueva descripción del punto de encuentro: ")

    cursor = connection.cursor()
    cursor.execute('''
        UPDATE punto_encuentro
        SET nombre = %s, ID_domicilio = %s, descripcion = %s
        WHERE ID_punto_encuentro = %s;
        ''', (newName, address_id, newDescription, meetingId))
    connection.commit()

    print("Punto de encuentro actualizado.")