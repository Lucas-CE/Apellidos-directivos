import pandas as pd
import json

# Cargamos los datos
path_data = "data/most_relevant_directors_surnames.csv"
df = pd.read_csv(path_data)

column = "conteo"

# Obtenemos los valores únicos de la columna de interés
col_unique_values = df[column].unique()

# Creamos una lista con la cantidad de cada valor único
values_count = [len(df[df['conteo'] == value]) for value in col_unique_values]


# Preparar datos para el front-end
bar_data = {
    "x": col_unique_values.tolist(),  # Valores únicos
    "y": values_count,  # Cantidad de valores únicos
}

# Guardar en un archivo JSON
with open("visualization/bar_data.json", "w") as f:
    json.dump(bar_data, f)

print("Datos del bara guardados en 'bar_data.json'")
