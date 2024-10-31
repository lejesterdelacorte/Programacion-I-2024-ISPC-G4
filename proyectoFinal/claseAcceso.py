from datetime import datetime

class Acceso:
    def __init__(self, id, fechaIngreso, fechaSalida, usuarioLogueado):
        self.id = id
        self.fechaIngreso = fechaIngreso
        self.fechaSalida = fechaSalida
        self.usuarioLogueado = usuarioLogueado
    def __str__(self):
        return f'Access ID: {self.id}, LoguinDate: {self.fechaIngreso}, logoutDate: {self.fechaSalida}, User: {self.usuarioLogueado}.'