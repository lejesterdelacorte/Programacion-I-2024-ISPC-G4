def restar (num1, num2):
    try:
        return round(num1 - num2, 2)
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')