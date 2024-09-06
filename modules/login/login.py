from ..utils.dBConnection import DatabaseConnection
from datetime import datetime

def leer_contador():
    try:
        with open("contador_fallos.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0

def escribir_contador(contador):
    with open("contador_fallos.txt", "w") as file:
        file.write(str(contador))

def login(user, password):
    db_instance = DatabaseConnection()
    connection = db_instance.get_connection()

    cursor = connection.cursor()
    cursor.execute('''
        SELECT id_usuario, nombre, apellido, email, password, id_domicilio
        FROM usuario
        WHERE email = %s AND password = %s;
        ''', (user, password))
    user_data = cursor.fetchone()
    connection.commit()

    if user_data:
        nombre_usuario = user_data[1]
        fecha_ingreso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("ingresos.txt", "a") as file:
            file.write(f"{nombre_usuario} - {fecha_ingreso}\n")
        return "Usuario ingreso correcto"
    else:
        contador_fallos = leer_contador()
        contador_fallos += 1
        escribir_contador(contador_fallos)
        return f"Usuario o contraseña incorrecta. Intentos fallidos: {contador_fallos}"