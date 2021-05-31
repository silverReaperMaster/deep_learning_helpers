import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def display_image_from_file(_target_file, _title=""):
  img = mpimg.imread(_target_file)
  plt.imshow(img)
  plt.title(_title)
  plt.axis("off");
  print(f"Image shape:{img.shape}")
  return img