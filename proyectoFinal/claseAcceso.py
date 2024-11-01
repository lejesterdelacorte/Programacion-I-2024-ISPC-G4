from datetime import datetime

class Acceso:
    def __init__(self, id, fechaIngreso, fechaSalida, usuarioLogueado):
        self.__id = id
        self.__fechaIngreso = fechaIngreso
        self.__fechaSalida = fechaSalida
        self.__usuarioLogueado = usuarioLogueado

    def __str__(self):
        return f'Access ID: {self.id}, Login Date: {self.fechaIngreso}, Logout Date: {self.fechaSalida}, User: {self.usuarioLogueado}.'

    @property
    def id(self):
        return self.__id

    @property
    def fechaIngreso(self):
        return self.__fechaIngreso

    @property
    def fechaSalida(self):
        return self.__fechaSalida

    @property
    def usuarioLogueado(self):
        return self.__usuarioLogueado

    @id.setter
    def id(self, nuevoId):
        self.__id = nuevoId
        
    @fechaIngreso.setter
    def fechaIngreso(self, nuevaFechaIngreso):
        self.__fechaIngreso = nuevaFechaIngreso

    @fechaSalida.setter
    def fechaSalida(self, nuevaFechaSalida):
        self.__fechaSalida = nuevaFechaSalida

    @usuarioLogueado.setter
    def usuarioLogueado(self, nuevoUsuarioLogueado):
        self.__usuarioLogueado = nuevoUsuarioLogueado