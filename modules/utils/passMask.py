import re
from prompt_toolkit import prompt

def pass_validation(password):
    if len(password) < 8:
        return False, "La contraseña debe tener al menos 8 caracteres."
    
    lowercase = re.search(r'[a-z]', password) is not None
    upercase = re.search(r'[A-Z]', password) is not None
    number = re.search(r'[0-9]', password) is not None
    special = re.search(r'[^a-zA-Z0-9]', password) is not None
    
    conditions = sum([lowercase, upercase, number, special])
    
    if conditions >= 2:
        return True, "Contraseña válida."
    else: 
        return False, "La contraseña debe cumplir al menos dos de las siguientes condiciones: minúscula, mayúscula, número o carácter especial."

def input_password():
    while True:
        password = prompt("Ingrese su contraseña, al menos dos de: mayuscula, minuscula, especial o numero: ", is_password=True)
        is_valid, message = pass_validation(password)
        print(message)
        if is_valid:
            return password