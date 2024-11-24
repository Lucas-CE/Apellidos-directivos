import pandas as pd
import networkx as nx
from pathlib import Path


def generate_graph(
    df: pd.DataFrame,
    source_col_name: str,
    target_col_name: str,
    edge_weight: str,
    group_colors: dict,
    report_path: Path,
    gexf_file_name: str = "graph",
):
    # Crear el grafo dirigido desde el DataFrame
    G = nx.from_pandas_edgelist(
        df,
        source=source_col_name,
        target=target_col_name,
        edge_attr=edge_weight,
        create_using=nx.DiGraph(),
    )

    # Crear grupo dinámicamente (ejemplo: diferenciar empresas y apellidos)
    group_membership = {
        node: "Empresa" if node in df[source_col_name].values else "Apellido"
        for node in G.nodes
    }

    # Asignar colores según grupo
    node_color = {
        node: group_colors.get(group, "#ffffff")
        for node, group in group_membership.items()
    }

    # Asignar formas según grupo
    node_shape = {
        node: "circle" if group == "Empresa" else "square"
        for node, group in group_membership.items()
    }

    # Asignar atributos a los nodos
    nx.set_node_attributes(G, group_membership, name="group")
    nx.set_node_attributes(G, node_color, name="color")
    nx.set_node_attributes(G, node_shape, name="shape")

    # Exportar el grafo a un archivo .gexf
    nx.write_gexf(G, report_path / f"{gexf_file_name}.gexf")

    print(f"Grafo generado y guardado en {report_path / f'{gexf_file_name}.gexf'}")
    return G


# Configuración para generar el grafo
if __name__ == "__main__":
    # Ruta al archivo CSV
    input_csv = "data/surname_relevant_in_some_company.csv"
    input_csv = "data/surname_with_relevant_companies_count.csv"
    input_csv = "data/most_relevant_directors_surnames.csv"

    # Leer el CSV
    df = pd.read_csv(input_csv)

    # Configuración del grafo
    group_colors = {
        "Empresa": "#FF0000",  # Rojo para empresas
        "Apellido": "#00FF00",  # Verde para apellidos
    }

    report_path = Path("visualization")
    report_path.mkdir(exist_ok=True)

    # Generar el grafo
    generate_graph(
        df=df,
        source_col_name="Nombre_empresa",
        target_col_name="Apellido",
        edge_weight="conteo",
        group_colors=group_colors,
        report_path=report_path,
    )
