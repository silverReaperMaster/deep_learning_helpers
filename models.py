import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

def display_model_details(_model, level=0):
    """
    Display information for model Layers.

  """
    for layer_number, layer in enumerate(_model.layers):
        extra = ' ' * level * 2
        print(f"{extra} {layer_number} {layer.name.ljust(35)} \t{layer.trainable}\t{layer.dtype}")
        if hasattr(layer, 'layers'):
            if level < 10:
                display_model_details(layer, level + 1)
                print("\n")



def add_model_to_compare(orig , name, add):
  """
    Adds more to complete dictionary of results.
  """
  orig[f"{name}"] = add 

  


def graf_models_comparer(complete_results = {}):
  fig = plt.figure(figsize=(8, 4))

  ax = fig.add_subplot(111)

  models = complete_results.items()
  ind = np.arange(len(models))
  accurs = []
  f1 = []
  precision = []
  rect_recall = []
  names = []
  width = 0.15
  

  for index,(name,values) in enumerate(complete_results.items()):
    print(f"{index} {name}  -> {values['accurasy']}")
    names.append(name)
    accurs.append(values["accurasy"])
    f1.append(values["f1"]*100)
    precision.append(values["precision"]*100)
    rect_recall.append(values["recall"]*100)

  rects_acc = ax.bar(ind, accurs, width, color='r',label='accuracy')
  rects_f1 = ax.bar(ind+width, f1, width, color='b',label='f1')
  rect_precission = ax.bar(ind+width*2, precision, width, color='g',label='precission')
  rect_recall = ax.bar(ind+width*3, rect_recall, width, color='m',label='recall')
  
  ax.set_ylabel('Scores')
  ax.set_title('Scores models')

  fmt = '%.0f%%' # Format you want the ticks, e.g. '40%'
  yticks = mtick.FormatStrFormatter(fmt)
  ax.yaxis.set_major_formatter(yticks)
  ax.set_ylim([0, 130])
  ax.set_xticks(ind)
  ax.set_xticklabels(names)
  ax.legend()


  autolabel(rects_acc,ax)
  autolabel(rects_f1,ax)
  autolabel(rect_precission,ax)
  autolabel(rect_recall,ax)
  plt.tight_layout()
  plt.show()

def autolabel(rects,ax):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%.02f'%h,
                ha='center', va='bottom', fontsize=7)

 

  
