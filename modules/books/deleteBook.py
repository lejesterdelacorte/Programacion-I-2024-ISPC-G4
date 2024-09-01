from ..utils.dBConnection import DatabaseConnection

def deleteBook():
    print("--------ELIMINACION DE LIBROS-------") 
    ID_libro = input("Ingrese el ID del libro a eliminar: ")
    db_instance = DatabaseConnection()
    connection = db_instance.get_connection()
    cursor = connection.cursor()
    sql = "DELETE FROM libro WHERE ID_libro=%s;"
    values = (ID_libro,)
    cursor.execute(sql, values)
    connection.commit()
    print("---EL LIBRO SE ELIMINÓ EXITOSAMENTE---") 