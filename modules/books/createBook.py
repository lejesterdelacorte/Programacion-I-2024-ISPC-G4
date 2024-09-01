from ..utils.dBConnection import DatabaseConnection

def createBook():
    print("----------CREAR UN NUEVO LIBRO----------") 
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    editorial = input("Ingrese la editorial del libro: ")
    fecha_publicacion =	input("Ingrese la fecha en la que fue publicado el libro: ")
    genero = input("Ingrese el género al que pertenece el libro: ")
    ID_usuario = input("Ingrese el id de usuario al que pertenece el libro: ")	
    db_instance = DatabaseConnection()
    connection = db_instance.get_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO libro (titulo, autor, editorial, fecha_publicacion, genero, ID_usuario) VALUES (%s, %s, %s, %s, %s, %s);"
    values = (titulo, autor, editorial, fecha_publicacion, genero, ID_usuario)
    cursor.execute(sql, values)
    connection.commit()
    print("--------EL LIBRO SE CREÓ CON ÉXITO-------") 
