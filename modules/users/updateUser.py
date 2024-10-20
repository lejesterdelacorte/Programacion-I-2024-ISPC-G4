from ..utils.dBConnection import DatabaseConnection
from ..utils.dateMask import input_birthdate
from ..address.updateAddress import updateAddress
import mysql.connector

def updateUser():
    db_instance = DatabaseConnection()
    connection = db_instance.get_connection()
    try:
        update_user = input("Ingrese el nickname del usuario que quiere modificar: ")
        
        
        cursor = connection.cursor()
        cursor.execute('''
            SELECT ID_usuario, ID_domicilio FROM usuario
            WHERE nombre_usuario = %s
            ''', (update_user,))
        user_data = cursor.fetchone()
        
        if user_data:
            user_id, address_id = user_data
            print("-------CREACION DEL USUARIO---------")
            nickname = input("Ingrese su Nickname: ")
            firstname = input("Ingrese su Nombre: ")
            lastname = input("Ingrese su Apellido: ")
            phone = input("Ingrese su Telefono: ")
            password = input("Ingrese su contraseña: ")
            email = input("Ingrese su email: ")
            birthdate = input_birthdate()
            
            update_query = 'UPDATE usuario SET '
            params = []
            
            if nickname:
                update_query += 'nombre_usuario = %s, '
                params.append(nickname)
            if firstname:
                update_query += 'nombre = %s, '
                params.append(firstname)
            if lastname:
                update_query += 'apellido = %s, '
                params.append(lastname)
            if phone:
                update_query += 'telefono = %s, '
                params.append(phone)
            if email:
                update_query += 'e_mail = %s, '
                params.append(email)
            if password:
                update_query += 'password = %s, '
                params.append(password)
            if birthdate:
                update_query += 'fecha_nacimiento = %s '
                params.append(birthdate)
            update_query += ' WHERE ID_usuario = %s'
            params.append(user_id)
            
            updateAddress(address_id)
            
            cursor.execute(update_query, tuple(params))
            connection.commit()
            print(cursor.rowcount, "registro actualizado.")
        else:
            print("Usuario no encontrado")
    except mysql.connector.Error as error:
        print("ERROR en la operacion MySQL: ", error)
        connection.rollback()