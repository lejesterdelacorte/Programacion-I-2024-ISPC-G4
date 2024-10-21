import pickle
from claseUsuario import Usuario

class crudUsuarios:
    def __init__(self):
        self.usuarios = self.loadUser()
        self.contador_id = len(self.usuarios) + 1

    def loadUser(self):
        try:
            with open('usuarios.ispc', 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            return {}

    def saveUser(self):
        with open('usuarios.ispc', 'wb') as file:
            pickle.dump(self.usuarios, file)

    def addUser(self, username, password, email):
        if username in self.usuarios or email in [user.email for user in self.usuarios.values()]:
            print("El usuario o el email ya existen.")
            return False
        id = self.contador_id
        self.usuarios[id] = Usuario(id, username, password, email)
        self.contador_id += 1
        self.saveUser()
        print("Usuario agregado exitosamente.")
        return True

    def modifyUser(self, id, username, password, email):
        if id not in self.usuarios:
            print("Usuario no encontrado.")
            return False
        
        usuario = self.usuarios[id]
        if username:
            usuario.username = username
        if password:
            usuario.password = password
        if email:
            usuario.email = email
        self.saveUser()
        print("Usuario modificado exitosamente.")
        return True

    def deleteUser(self, identifier):
        for id, user in list(self.usuarios.items()):
            if user.username == identifier or user.email == identifier:
                del self.usuarios[id]
                self.saveUser()
                print("Usuario eliminado exitosamente.")
                return True
        print("Usuario no encontrado.")
        return False

    def findUser(self, identifier):
        for user in self.usuarios.values():
            if user.username == identifier or user.email == identifier:
                return user
        return None

    def showUser(self):
        if not self.usuarios:
            print("No hay usuarios registrados.")
        else:
            for user in self.usuarios.values():
                print(user)
