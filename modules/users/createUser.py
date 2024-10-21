from ..utils.dBConnection import DatabaseConnection
from ..utils.dateMask import input_birthdate
from ..address.createAddress import createAddress

def createUser():
    db_instance = DatabaseConnection()
    connection = db_instance.get_connection()
    
    # Ingreso de datos
    print("-------CREACION DEL USUARIO---------")
    nickname = input("Ingrese su Nickname: ")
    firstname = input("Ingrese su Nombre: ")
    lastname = input("Ingrese su Apellido: ")
    phone = input("Ingrese su Telefono: ")
    password = input("Ingrese su contraseña: ")
    email = input("Ingrese su email: ")
    birthdate = input_birthdate()
    
    print("--------CREACION DEL DOMICILIO-------")   
    street = input("Ingrese la Calle: ")
    street_number = input("Ingrese la Altura: ")
    city = input("Ingrese la Ciudad: ")
    country = input("Ingrese el País: ")
    address_id = createAddress(street, street_number, city, country)
    
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO usuario(nombre_usuario, nombre, apellido, fecha_nacimiento, telefono, e_mail, password, ID_domicilio)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s);
        ''', (nickname, firstname, lastname, birthdate, phone, email, password, address_id))
    connection.commit()
    
    return True;
