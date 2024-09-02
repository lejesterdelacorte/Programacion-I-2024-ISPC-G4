from ..utils.dBConnection import DatabaseConnection
from ..utils.dateMask import input_birthdate
from ..address.createAddress import createAddress

'''
Esta funcion se encargará del registro de los usuarios.
'''
def registerForm():
    db_instance = DatabaseConnection()
    
    print("------------- CREACION DEL USUARIO -------------")
    username = input("Ingrese su nombre de Usuario: ")
    firstname = input("Ingrese su Nombre: ")
    lastname = input("ingrese su Apellido: ")
    phone = input("Ingrese su Teléfono: ")
    password = input("Ingrese su contraseña: ")
    email = input("Ingrese su email: ")
    birthdate = input_birthdate()
    
    print("--------CREACION DEL DOMICILIO-------")   
    street = input("Ingrese la Calle: ")
    street_number = input("Ingrese la Altura: ")
    city = input("Ingrese la Ciudad: ")
    country = input("Ingrese el País: ")
    address_id = createAddress(street, street_number, city, country)