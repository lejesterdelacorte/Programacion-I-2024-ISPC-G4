class Usuario:
    def __init__(self, id, DNI, username, password, email):
        self.__id = id
        self.__DNI = DNI
        self.__username = username
        self.__password = password
        self.__email = email
    def __str__(self):
        return f'User ID: {self.id}, Username: {self.username}, Email: {self.email}'

    @property
    def id(self):
        return self.__id
    
    @property
    def DNI(self):
        return self.__DNI
    
    @property
    def username(self):
        return self.__username
    
    @property
    def password(self):
        return self.__password
    
    @property
    def email(self):
        return self.__email

    @id.setter
    def id(self, newId):
        self.__id = newId

    @username.setter
    def username(self, newUsername):
        self.__username = newUsername

    @password.setter
    def password(self, newPassword):
        self.__password = newPassword

    @email.setter
    def email(self, newEmail):
        self.__email = newEmail