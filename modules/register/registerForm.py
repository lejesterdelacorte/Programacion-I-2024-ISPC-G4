import pymysql
from ..utils.dBConnection import DatabaseConnection
from ..utils.dateMask import input_birthdate
from ..utils.passMask import input_password
from ..address.createAddress import createAddress
from ..captcha.generate_captcha import generate_captcha
import pickle

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
    
    captcha = generate_captcha()
    print("CAPTCHA: ", captcha)
    
    if captcha:
        print("ENTRE AL IF")
        try:
            cursor.execute('''
                INSERT INTO usuario(nombre_usuario, nombre, apellido, fecha_nacimiento, telefono, e_mail, password, ID_domicilio, DNI)
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);
                ''', (username, firstname, lastname, birthdate, phone, email, password, address_id, ced_id))
            connection.commit()
            
            # Serializar los datos del usuario en un archivo binario
            usuario_data = {
                'username': username,
                'firstname': firstname,
                'lastname': lastname,
                'birthdate': birthdate,
                'phone': phone,
                'email': email,
                'password': password,
                'address_id': address_id,
                'ced_id': ced_id
            }
            with open("usuario.ispc", 'wb') as file:
                pickle.dump(usuario_data, file)
            
            # Guardar los datos del usuario en un archivo de texto
            with open('usuariosCreados.txt', 'a') as file:
                file.write(f'Usuario creado:\n'
                           f'Nickname: {username}\n'
                           f'Cedula: {ced_id}\n'  
                           f'Nombre: {firstname}\n'
                           f'Apellido: {lastname}\n'
                           f'Telefono: {phone}\n'
                           f'Email: {email}\n'
                           f'Fecha de Nacimiento: {birthdate}\n'
                           f'Domicilio: Calle {street}, Altura {street_number}, Ciudad {city}, País {country}\n'
                           f'Creado correctamente.\n\n')
            print("Usuario registrado correctamente.")
            
        except pymysql.IntegrityError as e:
            connection.rollback()
            if e.args[0] == 1062:
                print("Error: El nombre de usuario o DNI ya existen en la base de datos.")
            else:
                print(f"Error en la base de datos: {e}")