import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def display_image_from_file(_target_file, _title=""):
  img = mpimg.imread(_target_file)
  plt.imshow(img)
  plt.title(_title)
  plt.axis("off");
  print(f"Image shape:{img.shape}")
  return img

def show_images_comparator(img_array_1, img_array_2):
  """
    Display array of pictures side by side to compare.
    Lenght must be equal of the 2 arrays.

  """
  if (len(img_array_1)!= len(img_array_2)):
    raise Exception("Length of array 1 and 2 not equal")

  fig = plt.figure(figsize=(18, 9))
  rows = len(img_array_1)
  gs = gridspec.GridSpec(nrows=rows, ncols=2)
  for  i  in range(len(img_array_1)):
    print(f"index: {i}")
