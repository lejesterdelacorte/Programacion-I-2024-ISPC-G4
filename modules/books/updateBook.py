from ..utils.dBConnection import DatabaseConnection

def updateBook():
    print("--------MODIFICACION DE LIBRO EXISTENTE-------") 
    ID_libro = input("Ingrese el ID del libro a modificar: ")
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    editorial = input("Ingrese la editorial del libro: ")
    fecha_publicacion =	input("Ingrese la fecha en la que fue publicado el libro: ")
    genero = input("Ingrese el género al que pertenece el libro: ")
    ID_usuario = input("Ingrese el id de usuario al que pertenece el libro: ")	
    db_instance = DatabaseConnection()
    connection = db_instance.get_connection()
    cursor = connection.cursor()
    sql = "UPDATE libro SET titulo=%s, autor=%s, editorial=%s, fecha_publicacion=%s, genero=%s, ID_usuario=%s WHERE ID_libro = %s;"
    values = (titulo, autor, editorial, fecha_publicacion, genero, ID_usuario, ID_libro)
    cursor.execute(sql, values)
    connection.commit()
    print("--------EL LIBRO SE MODIFICÓ CON ÉXITO-------") 