from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt
import itertools

def normalization_confusion_matrix(cm_data):
  return cm_data.astype("float")/ cm_data.sum(axis=1)[:,np.newaxis]

def pretty_confusion_matrix_display(test_data, pred_data, classes=None,  figsize = (10,10),text_size=20 ):
  print("pcmd")

  cm = confusion_matrix(test_data, pred_data)
  cm_norm = normalization_confusion_matrix(cm)
  
  num_classes = cm.shape[0]

  fig, ax = plt.subplots(figsize=figsize)
  cax = ax.matshow(cm,cmap= plt.cm.Blues)
  fig.colorbar(cax)
  
  if classes:
    labels = classes
  else:
    labels = np.arange(cm.shape[0])

  # Set Figure values
  ax.set(
    title="Confusion Matrix",
    xlabel="Predicticted", 
    ylabel="True",
    xticks=np.arange(num_classes),
    yticks=np.arange(num_classes),
    xticklabels=labels,
    yticklabels=labels)
  
  # X axis
  ax.xaxis.set_label_position("bottom")
  ax.xaxis.tick_bottom()
  ax.xaxis.label.set_size(text_size*2)

  # Y axis
  ax.yaxis.label.set_size(text_size*2)

  threshold = (cm.max()+cm.min())/2.

  for i,j in itertools.product(range(cm.shape[0]),range(cm.shape[1])):
    plt.text(j,i,f"{cm[i,j]} ({cm_norm[i,j]*100:.1f}%)",
              horizontalalignment ="center", 
              color="white" if cm[i,j] > threshold else "black",
              size = text_size )

