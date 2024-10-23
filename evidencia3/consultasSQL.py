import mysql.connector
from conexionBD import connectDb

def mostrar_libros_por_genero(genero):
    conexion = connectDb()
    cursor = conexion.cursor()
    consulta = "SELECT id_libro, titulo, autor FROM libro WHERE genero = %s"
    cursor.execute(consulta, (genero,))
    resultados = cursor.fetchall()
    for libro in resultados:
        print(f"ID: {libro[0]}, Titulo: {libro[1]}, Autor: {libro[2]}")
    cursor.close()
    conexion.close()

def insertar_usuario():
    conexion = connectDb()
    cursor = conexion.cursor()
    consulta = """
    INSERT INTO usuario (nombre_usuario, nombre, apellido, fecha_nacimiento, telefono, e_mail, password, ID_domicilio)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    valores = ('aperez', 'Alejandro', 'Perez', '1998-04-01', '3513333333', 'mail6@mail6.com', 'passusuario6', 4)
    cursor.execute(consulta, valores)
    conexion.commit()
    print(f"Usuario {valores[0]} insertado con éxito.")
    cursor.close()
    conexion.close()

def actualizar_telefono_usuario(id_usuario, nuevo_telefono):
    conexion = connectDb()
    cursor = conexion.cursor()
    consulta = "UPDATE usuario SET telefono = %s WHERE ID_usuario = %s"
    cursor.execute(consulta, (nuevo_telefono, id_usuario))
    conexion.commit()
    print(f"Teléfono del usuario con ID {id_usuario} actualizado a {nuevo_telefono}.")
    cursor.close()
    conexion.close()

def eliminar_libro(id_libro):
    conexion = connectDb()
    cursor = conexion.cursor()
    consulta = "DELETE FROM libro WHERE ID_libro = %s"
    cursor.execute(consulta, (id_libro,))
    conexion.commit()
    print(f"Libro con ID {id_libro} eliminado con éxito.")
    cursor.close()
    conexion.close()

def consultar_join_usuario_libro():
    conexion = connectDb()
    cursor = conexion.cursor()
    consulta = """
    SELECT u.ID_usuario, u.nombre_usuario, l.ID_libro, l.titulo, l.autor, l.genero
    FROM usuario u
    INNER JOIN libro l ON u.ID_usuario = l.ID_usuario
    """
    cursor.execute(consulta)
    resultados = cursor.fetchall()
    for resultado in resultados:
        print(f"Usuario ID: {resultado[0]}, Nombre Usuario: {resultado[1]}, Libro ID: {resultado[2]}, Titulo: {resultado[3]}, Autor: {resultado[4]}, Género: {resultado[5]}")
    cursor.close()
    conexion.close()

def consultar_join_punto_encuentro():
    conexion = connectDb()
    cursor = conexion.cursor()
    consulta = """
    SELECT d.*, p.nombre AS nombre_punto_encuentro, p.descripcion
    FROM domicilio d
    INNER JOIN punto_encuentro p ON d.ID_domicilio = p.ID_domicilio
    WHERE p.descripcion LIKE %s
    """
    cursor.execute(consulta, ("%centro%",))
    resultados = cursor.fetchall()
    for resultado in resultados:
        print(f"Domicilio ID: {resultado[0]}, Punto Encuentro: {resultado[-2]}, Descripción: {resultado[-1]}")
    cursor.close()
    conexion.close()
