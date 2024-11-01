from claseUsuario import Usuario
from gestionUsuarios import load_user, save_user

class crudUsuarios:
    def __init__(self):
        self.usuarios = load_user('usuarios.ispc')
        self.contador_id = len(self.usuarios) + 1

    def addUser(self, username, password, email, DNI):
        if username in self.usuarios or email in [user.email for user in self.usuarios.values()]:
            print("El usuario o el email ya existen.")
            return False
        id = self.contador_id
        self.usuarios[id] = Usuario(id, DNI, username, password, email)
        self.contador_id += 1
        save_user('usuarios.ispc', self.usuarios)
        print("Usuario agregado exitosamente.")
        return True

    def modifyUser(self, id, username=None, password=None, email=None, DNI=None):
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
        if DNI:
            usuario.DNI = DNI 
        
        save_user('usuarios.ispc', self.usuarios)
        print("Usuario modificado exitosamente.")
        return True

    def deleteUser(self, identifier):
        for id, user in list(self.usuarios.items()):
            if user.username == identifier or user.email == identifier:
                del self.usuarios[id]
                save_user('usuarios.ispc', self.usuarios)
                print("Usuario eliminado exitosamente.")
                return True
        print("Usuario no encontrado.")
        return False

    def findUser(self, identifier):
        for user in self.usuarios.values():
            print(user)
            if user.username == identifier or user.email == identifier:
                return user
        return None

    def showUser(self):
        if not self.usuarios:
            print("No hay usuarios registrados.")
        else:
            for user in self.usuarios.values():
                print(user)