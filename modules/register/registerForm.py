import pymysql
from ..utils.dBConnection import DatabaseConnection
from ..utils.dateMask import input_birthdate
from ..utils.passMask import input_password
from ..address.createAddress import createAddress

'''
Esta función se encargará del registro de los usuarios.
'''
def registerForm():
    db_instance = DatabaseConnection()
    connection = db_instance.get_connection()
    
    print("------------- CREACION DEL USUARIO -------------")
    username = input("Ingrese su nombre de Usuario: ")
    ced_id = input("Ingrese su DNI: ")
    
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM usuario WHERE nombre_usuario = %s OR DNI = %s", (username, ced_id))
    result = cursor.fetchone()
    
    if result[0] > 0:
        print("Error: El nombre de usuario o DNI ya existen en la base de datos.")
        return

    firstname = input("Ingrese su Nombre: ")
    lastname = input("Ingrese su Apellido: ")
    phone = input("Ingrese su Teléfono: ")
    password = input_password()
    email = input("Ingrese su email: ")
    birthdate = input_birthdate()
    
    print("--------CREACION DEL DOMICILIO-------")   
    street = input("Ingrese la Calle: ")
    street_number = input("Ingrese la Altura: ")
    city = input("Ingrese la Ciudad: ")
    country = input("Ingrese el País: ")
    address_id = createAddress(street, street_number, city, country)
    
    try:
        cursor.execute('''
            INSERT INTO usuario(nombre_usuario, nombre, apellido, fecha_nacimiento, telefono, e_mail, password, ID_domicilio, DNI)
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);
            ''', (username, firstname, lastname, birthdate, phone, email, password, address_id, ced_id))
        connection.commit()
        print("Usuario registrado correctamente.")
    except pymysql.IntegrityError as e:
        connection.rollback()
        if e.args[0] == 1062:
            print("Error: El nombre de usuario o DNI ya existen en la base de datos.")
        else:
            print(f"Error en la base de datos: {e}")
