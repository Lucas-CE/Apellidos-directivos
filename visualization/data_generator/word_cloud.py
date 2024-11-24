from wordcloud import WordCloud
import pandas as pd

# Cargar los datos
data = pd.read_csv("data/most_relevant_directors_surnames.csv")

# Crear un texto con los apellidos repetidos según el conteo
text_data = " ".join(data["Apellido"].repeat(data["conteo"]))

# Generar la nube de palabras
wordcloud = WordCloud(
    width=800, height=400,
    background_color='white',
    colormap='viridis',
    collocations=False,
).generate(text_data)

# Guardar la imagen
wordcloud.to_file("visualization/wordcloud.png")

print("Nube de palabras guardada como 'wordcloud.png'")
