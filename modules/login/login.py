from ..utils.dBConnection import DatabaseConnection
from datetime import datetime
from prompt_toolkit import prompt
from evidencia2.acceso import Acceso
from evidencia2.usuario import Usuario
import pickle


def leer_contador():
    try:
        with open("contador_fallos.txt", "r") as file:
            content = file.read().strip()
            return int(content) if content else 0
    except (FileNotFoundError, ValueError):
        return 0

def escribir_contador(contador):
    with open("logs.txt", "w") as file:
        file.write(str(contador))

def login():
    username = input("Ingrese su nombre_usuario: ")
    password = prompt("Ingrese su contraseña: ", is_password=True)
    db_instance = DatabaseConnection()
    connection = db_instance.get_connection()

    cursor = connection.cursor()
    cursor.execute('''
        SELECT  nombre_usuario, nombre, apellido, e_mail, id_domicilio, ID_usuario
        FROM usuario
        WHERE nombre_usuario = %s AND password = %s;
        ''', (username, password))
    user_data = cursor.fetchone()
    connection.commit()

    if user_data:
        nombre_usuario = user_data[1]
        fecha_ingreso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        access = Acceso(fecha_ingreso, None, user_data[5])
        access.createAccess()
        with open("acceso.ispc", 'wb') as file:
            pickle.dump(access, file)

        
        with open("ingresos.txt", "a") as file:
            file.write(f"{nombre_usuario} - {fecha_ingreso}\n")
        login = True

        return 0, login
    else:
        contador_fallos = leer_contador()
        contador_fallos += 1
        login = False
        logs = {
            "Intentos fallidos": contador_fallos,
            "Usuario": username,
            "Fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "password": password
        }
        escribir_contador(logs)
        return contador_fallos, login