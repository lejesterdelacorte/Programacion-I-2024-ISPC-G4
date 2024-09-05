import random
from aritmetica import sumar, restar, multiplicar, dividir

'''
Captcha: para terminar el proceso de registro se debe ingresar un captcha
que utilice el módulo aritmética, donde la aplicación le muestre al usuario
los datos de una operación de manera aleatoria (usando valores aleatorios)
y el usuario deba ingresar el resultado de dicha operación (aclarar que la
respuesta debe contener dos números decimales): si la ingresa correctamente
se crea el usuario, sino ofrece otro captcha (junto a la opción de salir del
registro).
'''

def generate_captcha():
    num1 = generate_values()
    num2 = generate_values()
    operator = randomize_operation()
    if operator == 1:
        operator_symbol = '+'
    if operator == 2:
        operator_symbol = '-'
    if operator == 3:
        operator_symbol = '*'
    else:
        operator_symbol = '/'
    result = generate_result (num1, num2, operator)
    try:
        user_result = float(input(f'Debes realizar la siguiente operación cuyo resultado debe tener dos decimales:\n {num1} {operator_symbol} {num2} ='))
    except ValueError as error:
        print(f'{error}')
    compare_result(user_result, result)

def generate_values():
    num = round(random.uniform(-100, 100), 2)
    if num == 0.00:
        generate_values()
    return num 

def randomize_operation ():
    return random.randint(1, 4) 

def generate_result(num1, num2, operator):
    if operator == 1:
        result = sumar(num1, num2)
    elif operator == 2:
        result= restar(num1, num2)
    elif operator == 3:
        result= multiplicar(num1, num2)
    else:
        result= dividir(num1, num2)
    print(result)
    return result

def compare_result(user_result, result):
    if user_result == result:
        print('El resultado es correcto, puedes registrarte como usuario.')
        return
    user_choice = input('El resultado es incorrecto. Si deseas cancelar el registro ingresa: "n" de lo contrario te daremos otro captcha').lower()
    if user_choice == 'n':
        print('Hasta la próxima.')
        return
    generate_captcha()