from ..utils.dBConnection import DatabaseConnection

def getBooks():
    print("--------CONSULTA DE LIBROS-------") 
    db_instance = DatabaseConnection()
    connection = db_instance.get_connection()
    cursor = connection.cursor() 
    cursor.execute("SELECT * FROM libro;")
    result = cursor.fetchall()
    for i in result:
        print(i) 
    print("--------GRACIAS POR CONSULTAR-------")  