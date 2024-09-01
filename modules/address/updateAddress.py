from ..utils.dBConnection import DatabaseConnection
import mysql.connector

def updateAddress(address_id):
    db_instance = DatabaseConnection()
    connection = db_instance.get_connection()
    try:
        if address_id:
            print("--------CREACION DEL DOMICILIO-------")   
            street = input("Ingrese la Calle: ")
            street_number = input("Ingrese la Altura: ")
            city = input("Ingrese la Ciudad: ")
            country = input("Ingrese el País: ")
            
            update_query = 'UPDATE domicilio SET '
            params = []
            
            if street:
                update_query += 'calle = %s, '
                params.append(street)
            if street_number:
                update_query += 'altura = %s, '
                params.append(street_number)
            if city:
                update_query += 'ciudad = %s, '
                params.append(city)
            if country:
                update_query += 'pais = %s '
                params.append(country)
            
            update_query += ' WHERE ID_domicilio = %s'
            params.append(address_id)
            
            cursor = connection.cursor()
            cursor.execute(update_query, tuple(params))
            connection.commit()
            print(cursor.rowcount, "registro actualizado.")
        else:
            print("Usuario no encontrado")
    except mysql.connector.Error as error:
        print("ERROR en la operacion MySQL: ", error)
        connection.rollback()