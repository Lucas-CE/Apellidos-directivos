import pandas as pd
from wordcloud import WordCloud

# Cargamos los datos
path_data = "data/surname_with_relevant_companies_count.csv"
df = pd.read_csv(path_data)

relevant_surnames = ["LARRAIN", "VIAL", "ERRAZURIZ", "ECHEVERRIA"]

for surname in relevant_surnames:
    companies = df[df["Apellido"] == surname]
    companies_dict = dict(zip(companies["Nombre_empresa"], companies["conteo"]))
    wordcloud = WordCloud(
        width=800, height=340, background_color="white"
    ).generate_from_frequencies(companies_dict)

    wordcloud.to_file(f"visualization/{surname}_wordcloud.png")
