import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def display_horizontal_bars(data: pd.DataFrame, name_column, value_column, fig_size=(10, 10), title="Title"):
    plt.rcdefaults()
    fig, ax = plt.subplots(figsize=fig_size)

    # Example data
    y_pos = np.arange(len(data))

    ax.barh(y_pos, data[f"{value_column}"], align='center')
    ax.set_yticks(y_pos)

    ax.set_yticklabels(data[f"{name_column}"])
    ax.invert_yaxis()  # labels read top-to-bottom

    ax.set_ylabel(f"{name_column}", weight='bold', size=12)
    ax.set_xlabel(f"{value_column}", weight='bold', size=12)
    ax.set_title(f"{title}", weight='bold', size=20)

    plt.show()
