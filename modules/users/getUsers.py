from ..utils.dBConnection import DatabaseConnection

def getUsers():
    db_conn = DatabaseConnection()
    connection = db_conn.get_connection()
    
    cursor = connection.cursor()
    cursor.execute('''
        SELECT u.nombre_usuario, u.nombre, e_mail, telefono, l.titulo, l.genero
        FROM usuario u        
        JOIN libro l ON u.ID_usuario = l.ID_usuario
        ''')
    user_data = cursor.fetchall()
    
    if user_data:
        output_table = ""
        for user in user_data:
            output_table += f" --------------------- \n"
            output_table += f"Nickname: {user[0]}\n"
            output_table += f"Nombre: {user[1]}\n"
            output_table += f"EMail: {user[2]}\n"
            output_table += f"Telefono: {user[3]}\n"
            output_table += f"Titulo Libro: {user[4]}\n"
            output_table += f"Genero Libro: {user[5]}\n"
            output_table += f" --------------------- \n"
            print(output_table)
    else:
        print("NO HAY USER DATA")