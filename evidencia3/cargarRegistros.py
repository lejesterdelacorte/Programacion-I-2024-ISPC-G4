import pandas as pd

fileRoute = 'registrosPluviales2023.csv'

try:
    df = pd.read_csv(fileRoute)
    print('Registros pluviales cargados correctamente:')
        
    month = int(input("Ingresar el numero del mes (1-12) para visualizar los registros: "))
    
    if 1 <= month <= 12:
        print(f'Registros de lluvia para el Mes {month}:')
        print(df[f'Mes {month}'])
    else:
        print('Seleccion no valida, debe ser un numero entre 1 y 12.')
        
except FileNotFoundError:
    print(f'No se encontro el archivo {fileRoute}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
