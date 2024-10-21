from ..utils.dBConnection import DatabaseConnection
from datetime import datetime
import mysql.connector

def deleteUser():
    db_instance = DatabaseConnection()
    connection = db_instance.get_connection()
    try:
        deleted_user = input("Ingrese el nickname del usuario que quiere eliminar: ")
        
        cursor = connection.cursor()
        cursor.execute('''
            SELECT ID_usuario FROM usuario
            WHERE nombre_usuario = %s
            ''', (deleted_user,))
        user_id = cursor.fetchone()
        
        if user_id:
            user_id = user_id[0]
            date_now = datetime.now().strftime('%Y-%m-%d')
            cursor.execute('''
                UPDATE usuario SET deleted_at = %s
                WHERE ID_usuario = %s;
                ''', (date_now, user_id))
            connection.commit()
            print(cursor.rowcount, "registro actualizado.")
        else:
            print("Usuario no encontrado")
    except mysql.connector.Error as error:
        print("ERROR en la operacion MySQL: ", error)
        connection.rollback()