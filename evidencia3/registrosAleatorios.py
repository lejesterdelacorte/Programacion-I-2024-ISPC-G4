import random
import pandas as pd

daysPerMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

registrosPluviales = {f'Mes {i+1}': [] for i in range(12)}

for mes, dias in enumerate(daysPerMonth, start=1):
    for dia in range(1, dias + 1):
        registrosPluviales[f"Mes {mes}"].append(random.randint(0, 100))

df = pd.DataFrame(dict([(k, pd.Series(v)) for k,v in registrosPluviales.items()]))

df.to_csv('registrosPluviales2023.csv', index=False)



