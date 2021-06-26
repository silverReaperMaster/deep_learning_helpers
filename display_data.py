import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

def label_end(rects, _ax):
    """
    Attach a text label end of each bar displaying its height
    """
    for rect in rects:
      x_value = rect.get_width()
      y_value = rect.get_y() + rect.get_height() / 2
      space = 5
      ha = 'left'
      if x_value < 0:
        # Invert space to place label to the left
        space *= -1
        # Horizontally align label at right
        ha = 'right'
      label = "{:.3f}".format(x_value)
      plt.annotate(
        label,                      # Use `label` as label
        (x_value, y_value),         # Place label at end of the bar
        xytext=(space, 0),          # Horizontally shift label by `space`
        textcoords="offset points", # Interpret `xytext` as offset in points
        va='center',                # Vertically center label
        ha=ha)                      # Horizontally align label differently for
                                    # positive and negative values.



def display_horizontal_bars(data: pd.DataFrame, name_column, value_column, fig_size=(10, 10), title="Title"):
    plt.rcdefaults()
    fig, ax = plt.subplots(figsize=fig_size)
    ax.set_xlim(0, 1.1)
    # Example data
    y_pos = np.arange(len(data))
    bars = ax.barh(y_pos, data[f"{value_column}"], align='center')
    ax.set_yticks(y_pos)

    ax.set_yticklabels(data[f"{name_column}"])
    ax.invert_yaxis()  # labels read top-to-bottom

    ax.set_ylabel(f"{name_column}", weight='bold', size=12)
    ax.set_xlabel(f"{value_column}", weight='bold', size=12)
    ax.set_title(f"{title}", weight='bold', size=20)
    label_end(bars, ax)

    plt.show()
