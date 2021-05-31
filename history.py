import matplotlib.pyplot as plt
import pandas as pd
from mlxtend.plotting import plot_decision_regions
import matplotlib.gridspec as gridspec
import warnings

def plot_decision_bound(_model, _X_train, _y_train, _X_test, _y_test):
  warnings.filterwarnings('ignore')
  fig = plt.figure(figsize=(18, 9))
  gs = gridspec.GridSpec(nrows=1, ncols=2, height_ratios=[1])
  
  ax1 = fig.add_subplot(gs[0, 0])
  ax1.set_title('Train',fontsize = 50)
  ax1 = plot_decision_regions(X=_X_train,y=_y_train,clf=_model)
  
  ax2 = fig.add_subplot(gs[0, 1])
  ax2.set_title('Test',fontsize = 50)
  ax2 = plot_decision_regions(X=_X_test,y=_y_test,clf=_model)

  plt.show(block=False)
  warnings.filterwarnings('default')


def display_history(_history):
  """
    Display historical grafics and information
  """
  loss = _history.history["loss"]
  if "val_loss" in _history.history:
    val_loss = _history.history["val_loss"]

  accuracy = _history.history["accuracy"]
  if "val_accuracy" in _history.history:
    val_accuracy = _history.history["val_accuracy"]
   
  epochs = range(len(loss))

  fig = plt.figure(figsize=(18, 9))
  gs = gridspec.GridSpec(nrows=1, ncols=2, height_ratios=[1])
  
  # Plot loss
  ax1 = fig.add_subplot(gs[0, 0])
  ax1.set_title("Loss",fontsize=30)
  ax1 = plt.plot(epochs,loss,label="loss")
  if "val_loss" in _history.history:
    ax1 = plt.plot(epochs,val_loss,label="validation loss")
  
  # Notes
  plt.annotate('- Overfiting if validation_loss does not decrease and loss does', (0,0), (0, -60), xycoords='axes fraction', textcoords='offset points', va='top')
  ax1 = plt.xlabel("epochs",fontsize=15)
  ax1= plt.legend()

  # Plot accuracy
  ax2 = fig.add_subplot(gs[0,1])
  ax2.set_title("Accuracy", fontsize=30)
  ax2 = plt.plot(epochs,accuracy,label="accuracy")
  if "val_accuracy" in _history.history:
    ax2 = plt.plot(epochs,val_accuracy,label="validation accuracy")
   
  ax2 = plt.xlabel("epochs",fontsize=15)
  ax2= plt.legend()




def eval_details(_model,_X_eval,_y_eval):
  loss, accu = _model.evaluate(_X_eval,_y_eval, )
  print(f"Model loss eval: {loss}")
  print(f"Model loss accu: {(accu*100):.2f}%")




if __name__ == "__main__":
  print("Everything passed")
