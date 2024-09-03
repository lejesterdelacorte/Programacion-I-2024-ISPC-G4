def sumar_n (num_list):
    result = 0
    if num_list == None:
        while True:
            user_num = input("Ingrese el número a sumar o 'n' para salir:").lower()
            if user_num == 'n':
                print(f'El resultado es {result}')
                return round(result, 2)
            try:
                result += float(user_num) 
            except ValueError as error:
                print(f'Ingresó un caracter inválido. {error}')
    for i in num_list:
        result += i
    print(result)
    return result
