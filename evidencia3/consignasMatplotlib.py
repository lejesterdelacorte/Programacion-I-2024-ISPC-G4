import matplotlib.pyplot as plt
import pandas as pd

fileRoute = 'registrosPluviales2023.csv'

try:
    df = pd.read_csv(fileRoute)

    #Gráfico de barras
     
    totalMonthly = df.sum()

    plt.figure(figsize=(10, 6))
    plt.bar(totalMonthly.index, totalMonthly.values, color='skyblue')
    plt.title('Total de mm por mes año 2023')
    plt.xlabel('Meses')
    plt.ylabel('Milímetros caidos')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('graficoBarras.png')
    plt.show()

    #Gráfico de dispersión
     
    plt.figure(figsize=(10, 6))
    for month in range(1, 13):
        days = df[f'Mes {month}'].dropna()
        plt.scatter([month] * len(days), range(1, len(days) + 1), c=days, cmap='Blues', label=f'Mes {month}')
    
    plt.title('mm por día y mes')
    plt.xlabel('Meses')
    plt.ylabel('Días')
    plt.xticks(range(1, 13), [f'Mes {i}' for i in range(1, 13)])
    plt.colorbar(label='Milímetros caidos')
    plt.tight_layout()
    plt.savefig('graficoDispersión.png')
    plt.show()

    #Gráfico circular

    plt.figure(figsize=(8, 8))
    plt.pie(totalMonthly.values, labels=totalMonthly.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    plt.title('Porcentaje de lluvias por mes, año 2023')
    plt.tight_layout()
    plt.savefig('graficoCircular.png')
    plt.show()

except FileNotFoundError:
    print(f'Archivo {fileRoute} no encontrado')
except Exception as e:
    print(f'Ocurrió un error: {e}')
