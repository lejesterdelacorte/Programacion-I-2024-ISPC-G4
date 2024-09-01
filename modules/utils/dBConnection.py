import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()  # take environment variables from .env.

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class DatabaseConnection(metaclass=SingletonMeta):
    connection = None
    def __init__(self):
        if self.connection is None:
            try:
                self.connection = mysql.connector.connect(
                    host=os.getenv("DB_HOST"),
                    user=os.getenv("DB_USER"),
                    password=os.getenv("DB_PASS"),
                    database=os.getenv("DB_NAME")
                )
            except mysql.connector.Error as error:
                print("Error while connecting to MySQL", error)

    def get_connection(self):
        return self.connection