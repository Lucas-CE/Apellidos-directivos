import pandas as pd
import json


def generate_bar_plot_data(
    df: pd.DataFrame, count_column: str, label_column: str, path_to_save: str
):
    """
    Generate data for bar plot visualization

    Args
    ----
    df : pd.DataFrame
        Dataframe containing the data
    count_column : str
        Column name containing the count values
    label_column : str
        Column name containing the labels
    path_to_save : str
        Path to save the generated data
    """
    bar_height_values = df[count_column].values.tolist()
    bar_labels = df[label_column].values.tolist()
    bar_data = {"y": bar_height_values, "x": bar_labels}
    with open(path_to_save, "w") as f:
        json.dump(bar_data, f)
