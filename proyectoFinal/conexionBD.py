import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

load_dotenv()

def connectDb():
    try:
        conexion = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            database=os.getenv("DB_NAME")
        )
        return conexion
    except Error as e:
        print(f"Error al conectarse a MySQL: {e}")
        print("Por favor, configure los datos de conexión en el archivo .env y pruebe nuevamente o vuelva al menú principal.")
        return None
