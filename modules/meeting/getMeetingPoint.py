from ..utils.dBConnection import DatabaseConnection

def getMeetingPoints():
    db_instance = DatabaseConnection()
    connection = db_instance.get_connection()

    cursor = connection.cursor()
    cursor.execute('''
        SELECT * FROM punto_encuentro
        LIMIT 5;
        ''')
    results = cursor.fetchall()

    if results:
        print("Primeros 5 puntos de encuentro:")
        for result in results:
            print("ID: ", result[0])
            print("Nombre: ", result[1])
            print("ID_domicilio: ", result[2])
            print("Descripcion: ", result[3])
            print("-----")
    else:
        print("No se encontraron puntos de encuentro.")

