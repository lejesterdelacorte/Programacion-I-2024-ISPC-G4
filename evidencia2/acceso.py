from modules.utils.dBConnection import DatabaseConnection

class Acceso:
    def __init__(self, fechaIngreso, fechaSalida, usuarioLogueado):
        self.fechaIngreso = fechaIngreso
        self.fechaSalida = fechaSalida
        self.usuarioLogueado = usuarioLogueado 

    def createAccess(self):
        idUsuario = self.usuarioLogueado
        fechaIngreso = self.fechaIngreso
        fechaSalida = self.fechaSalida

        db_instance = DatabaseConnection()
        connection = db_instance.get_connection()
        cursor = connection.cursor()

        print(idUsuario, fechaIngreso, fechaSalida)

        cursor.execute('''INSERT INTO acceso(usuarioLogueado, fechaIngreso, fechaSalida)
                          VALUES(%s, %s, %s);''', (idUsuario, fechaIngreso, fechaSalida))
        connection.commit()

    def __str__(self):
        return (f"Acceso(fechaIngreso={self.fechaIngreso}, "
                f"fechaSalida={self.fechaSalida}, usuario={self.usuarioLogueado})")
