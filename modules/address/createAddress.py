from ..utils.dBConnection import DatabaseConnection

# Entidad independiente Address: Solo se accede mediante meeting_point o user
def createAddress(street, street_number, city, country):
    db_instance = DatabaseConnection()
    connection = db_instance.get_connection()

    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO domicilio(calle, altura, ciudad, pais)
        VALUES(%s, %s, %s, %s);           
        ''', (street, street_number, city, country))
    address_id = cursor.lastrowid
    connection.commit()

    return address_id