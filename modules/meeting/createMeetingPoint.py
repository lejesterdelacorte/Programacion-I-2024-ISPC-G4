from ..utils.dBConnection import DatabaseConnection
from ..address.createAddress import createAddress

def createMeetingPoint():
    db_instance = DatabaseConnection()
    connection = db_instance.get_connection()

    print("--------CREACION DEL PUNTO DE ENCUENTRO-------")
    name = input("Ingrese el nombre del punto de encuentro: ")
    description = input("Ingrese la descripción del punto de encuentro: ")
    street = input("Ingrese la Calle: ")
    street_number = input("Ingrese la Altura: ")
    city = input("Ingrese la Ciudad: ")
    country = input("Ingrese el País: ")
    address_id = createAddress(street, street_number, city, country)

    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO punto_encuentro(nombre, ID_domicilio, descripcion)
        VALUES(%s, %s, %s);
        ''', (name, address_id, description))
    connection.commit()

    return True