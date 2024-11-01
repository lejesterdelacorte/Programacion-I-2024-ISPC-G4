import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 
                 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

# Configuración del directorio para guardar los archivos de datos
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "datosAnalizados")
os.makedirs(path, exist_ok=True)

def cargar_datos_pluviales(ano):
    archivo = f"{path}/registroPluvial{ano}.csv"
    if os.path.isfile(archivo):
        print(f"Archivo encontrado para el año {ano}.")
        df = pd.read_csv(archivo)
    else:
        print(f"No se encontró archivo para el año {ano}. Creando datos aleatorios.")
        np.random.seed(42)  # Asegura reproducibilidad
        
        # Días por mes (considerando un año no bisiesto)
        dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Generar precipitaciones aleatorias para cada mes
        precipitaciones = []
        for dias in dias_por_mes:
            precipitaciones.append(np.round(np.random.rand(dias) * 100, 2))
        
        # Asegurarte de que todos los datos están en la misma lista
        precipitaciones = [item for sublist in precipitaciones for item in sublist]
        
        # Convertir en DataFrame
        df = pd.DataFrame({
            'Día': np.arange(1, len(precipitaciones) + 1),
            'Precipitación': precipitaciones
        })
        
        # Guardar en CSV
        df.to_csv(archivo, index=False)
        print(f"Datos de {ano} guardados en {archivo}.")
    
    return df

def analizar_ano(df):
    max_lluvia = df.values.max()
    min_lluvia = df.values.min()
    promedio_lluvia = df.values.mean()
    print(f"Máxima precipitación anual: {max_lluvia} mm")
    print(f"Mínima precipitación anual: {min_lluvia} mm")
    print(f"Promedio de precipitación anual: {promedio_lluvia:.2f} mm")

def graficar_ano(df, año):
    # Crear una nueva columna de mes
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    df['Mes'] = np.repeat(np.arange(1, 13), dias_por_mes)[:len(df)]
    
    # Agrupar los datos por mes y sumar precipitaciones
    mensual = df.groupby('Mes')['Precipitación'].sum()
    
    # Gráfico de barras
    plt.figure(figsize=(10, 6))
    mensual.plot(kind='bar', color='skyblue')
    plt.title(f'Precipitación Total Mensual en {año}')
    plt.xlabel('Mes')
    plt.ylabel('Precipitación (mm)')
    plt.xticks(ticks=range(12), labels=meses, rotation=45)
    plt.savefig(f"{path}/barras_mensuales_{año}.png")
    plt.show()

    # Gráfico de dispersión
    plt.figure(figsize=(10, 6))
    plt.scatter(mensual.index, mensual.values)
    plt.title('Gráfico de Dispersión de Precipitación Mensual')
    plt.xlabel('Mes')
    plt.ylabel('Precipitación Total (mm)')
    plt.xticks(ticks=range(1, 13), labels=meses, rotation=45)
    plt.grid()
    plt.savefig(f"{path}/dispersión_mensual_{año}.png")
    plt.show()
    
    # Gráfico circular de precipitación total
    plt.figure(figsize=(8, 8))
    plt.pie(mensual, labels=meses, autopct='%1.1f%%', startangle=140)
    plt.title(f'Proporción de Precipitación por Mes en {año}')
    plt.savefig(f"{path}/circular_mensual_{año}.png")
    plt.show()

def analizar_mes(df, mes):
    if isinstance(mes, str):
        mes_index = meses.index(mes) + 1  # Convertir el mes a índice
    else:
        mes_index = mes  # Ya es un índice

    # Filtrar los días que corresponden al mes
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    inicio = sum(dias_por_mes[:mes_index - 1])  # Calcular el índice de inicio para el mes
    fin = inicio + dias_por_mes[mes_index - 1]  # Calcular el índice de fin para el mes

    # Asegurarte de que no excedas los límites del DataFrame
    datos_mes = df['Precipitación'].iloc[inicio:fin]

    max_mes = datos_mes.max()
    min_mes = datos_mes.min()
    promedio_mes = datos_mes.mean()
    print(f"Datos para {mes}:")
    print(f"Máxima precipitación: {max_mes} mm")
    print(f"Mínima precipitación: {min_mes} mm")
    print(f"Promedio de precipitación: {promedio_mes:.2f} mm")
    print(f"Datos completos:\n{datos_mes}")
    
def graficar_mes(df, mes, año):
    # Convertir el mes a número si se pasa como nombre
    print(mes);
    if isinstance(mes, str):
        mes = meses.index(mes) + 1  # +1 porque los índices son de 0 a 11

    # Filtrar los días que corresponden al mes
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    inicio = sum(dias_por_mes[:mes - 1])  # Calcular el índice de inicio para el mes
    fin = inicio + dias_por_mes[mes - 1]  # Calcular el índice de fin para el mes

    # Asegurarte de que no excedas los límites del DataFrame
    datos_mes = df['Precipitación'].iloc[inicio:fin]

    # Gráfico circular: Precipitación diaria en el mes
    plt.figure(figsize=(8, 8))
    plt.pie(datos_mes, labels=np.arange(1, len(datos_mes) + 1), autopct='%1.1f%%', startangle=140)
    plt.title(f'Precipitación en {meses[mes-1]} de {año}')
    plt.savefig(f"{path}/circular_{meses[mes-1]}_{año}.png")
    plt.show()
