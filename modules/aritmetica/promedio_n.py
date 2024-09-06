def promedio_n(num_list):
    counter = 0 
    result = 0 
    if num_list == None:    
        while True:
            user_num = input("ingreso de número o 'n' para salir:").lower()
            if user_num == 'n':
                try:                
                    result= result / counter
                    print(f'El promedio es: {result}')
                    return round(result, 2)
                except ZeroDivisionError as error: 
                    print(f'No hay números a promediar. {error}')
            try: 
                result= result + float(user_num)
                counter += 1
            except ValueError as error:
                print(f'Ingresó un caracter inválido. {error}')
    for i in num_list:
        result += i
        counter += 1
    final_result = round(result / counter, 2)
    print(final_result)
    return final_result
