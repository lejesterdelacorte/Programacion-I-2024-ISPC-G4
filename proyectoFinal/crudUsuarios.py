from claseUsuario import Usuario
from gestionUsuarios import load_user, save_user
import datetime
import os

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

    def findUserByDni(self, dni):
        sorted_users = sorted(self.usuarios.values(), key=lambda user: user.DNI)

        log_dir = 'búsquedasYordenamientos'
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        
        fecha = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        log_filename = os.path.join(log_dir, f"buscandoUsuarioPorDNI-{fecha}.txt")
        with open(log_filename, 'w') as log_file:
            log_file.write(f"Búsqueda Binaria por DNI: buscando el DNI {dni} en el archivo usuarios.ispc que contiene {len(sorted_users)} usuarios.\n")
            
            if sorted_users == []:
                log_file.write(f"No se encontró ningún usuario registrado.\n")
                return None
            if dni < sorted_users[0].DNI or dni > sorted_users[-1].DNI:
                log_file.write(f"No se encuentra registrado el usuario con ese DNI debido a que el DNI a buscar es más chico que el más chico de los registrados o más grande que el más grande de los registrados.\n")
                return None
            
            left, right = 0, len(sorted_users) - 1
            attempts = 0
            while left <= right:
                attempts += 1
                mid = (left + right) // 2
                log_file.write(f"Intento {attempts}: DNI del usuario de la posición {mid} es {sorted_users[mid].DNI} ")
                if sorted_users[mid].DNI == dni:
                    log_file.write(f"por lo tanto se encontró el usuario en {attempts} intentos.\n")
                    return sorted_users[mid]
                elif sorted_users[mid].DNI < dni:
                    log_file.write(f"por lo tanto se buscará en la subsecuencia de la derecha (DNI más grandes) (posición {mid + 1} a {right}).\n")
                    left = mid + 1
                else:
                    log_file.write(f"por lo tanto se buscará en la subsecuencia de la izquierda (DNI más chicos) (posición {left} a {mid - 1}).\n")
                    right = mid - 1
            
            log_file.write(f"No se encontró el usuario con DNI {dni} después de {attempts} intentos.\n")
        return None