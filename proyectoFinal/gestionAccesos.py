import pickle
from datetime import datetime
from claseAcceso import Acceso

class gestionAccesos:
    def __init__(self):
        self.accesos = self.loadAccess()

    def loadAccess(self):
        try:
            with open('accesos.ispc', 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            return []

    def saveAccess(self):
        with open('accesos.ispc', 'wb') as file:
            pickle.dump(self.accesos, file)

    def registerAccess(self, usuario, success, password=None):
        fecha_ingreso = datetime.now()
        username = usuario.username if hasattr(usuario, 'username') else usuario
        acceso = Acceso(len(self.accesos) + 1, fecha_ingreso, None, username)
        self.accesos.append(acceso)
        self.saveAccess()  
        if success:
            print(f"Acceso registrado para {username}.")
        else:
            with open('logs.txt', 'a') as log_file:
                log_file.write(f"Intento fallido - username: {username} - {datetime.now()} - Clave: {password}\n")

