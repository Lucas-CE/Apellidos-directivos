import pandas as pd
import json

# Cargamos los datos
path_data = "data/company_surname_count.csv"
df = pd.read_csv(path_data)

df.sort_values(by="conteo", ascending=False, inplace=True)
importantes = df.head(10).copy()


def function_to_abreviate(text: str):
    # Si el texto tiene largo menor a 10, lo dejamos igual
    if len(text) < 20:
        return text
    # Primero separamos las palabras
    words = text.split(" ")
    # Sacamos las palabras con 2 o menos letras
    words = [word for word in words if len(word) > 2]
    # Finalmente, tomamos la primera letra de cada palabra y las dejamos
    # separadas con un punto
    return ".".join([word[0] for word in words])


# Le aplicamos la función a la columna de Nombre_empresa
importantes["Nombre_empresa"] = importantes["Nombre_empresa"].apply(
    function_to_abreviate
)

# Creamos una columna que diga: Apellido {apellido} en {Nombre_empresa}
importantes["Apellido_empresa"] = (
    "Apellido " + importantes["Apellido"] + " en " + importantes["Nombre_empresa"]
)
importantes.drop(columns=["Nombre_empresa", "Apellido"], inplace=True)


# Preparar datos para el front-end
bar_data = {
    "x": importantes["conteo"].tolist(),
    "y": importantes["Apellido_empresa"].tolist(),
}

# Guardar en un archivo JSON
with open("visualization/bar_dominant_surname_data.json", "w") as f:
    json.dump(bar_data, f)
