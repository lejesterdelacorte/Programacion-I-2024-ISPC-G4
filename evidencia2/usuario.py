from datetime import datetime
import mysql.connector
from modules.utils.dateMask import input_birthdate
import mysql.connector

from modules.utils.dBConnection import DatabaseConnection
from modules.address.updateAddress import updateAddress
from modules.register.registerForm import registerForm

class Usuario:
    def __init__(self, username=None, password=None, email=None):
        self.username = username
        self.password = password
        self.email = email
        self.accesos = []

    def agregar_acceso(self, acceso):
        self.accesos.append(acceso)

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

    def createUser(self):
        registerForm()
        
    def getUsers():
        db_conn = DatabaseConnection()
        connection = db_conn.get_connection()
        
        cursor = connection.cursor()
        cursor.execute('''
            SELECT u.nombre_usuario, u.nombre, e_mail, telefono, l.titulo, l.genero
            FROM usuario u        
            JOIN libro l ON u.ID_usuario = l.ID_usuario
            ''')
        user_data = cursor.fetchall()
        
        if user_data:
            output_table = ""
            for user in user_data:
                output_table += f" --------------------- \n"
                output_table += f"Nickname: {user[0]}\n"
                output_table += f"Nombre: {user[1]}\n"
                output_table += f"EMail: {user[2]}\n"
                output_table += f"Telefono: {user[3]}\n"
                output_table += f"Titulo Libro: {user[4]}\n"
                output_table += f"Genero Libro: {user[5]}\n"
                output_table += f" --------------------- \n"
                print(output_table)
        else:
            print("NO HAY USER DATA")

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
                password = input("Ingrese su contraseÃ±a: ")
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

    def __str__(self):
        return f"Usuario(id={self.id}, username={self.username}, email={self.email})"