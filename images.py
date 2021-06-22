import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.gridspec as gridspec


def display_image_from_file(_target_file, _title=""):
    img = mpimg.imread(_target_file)
    plt.imshow(img)
    plt.title(_title)
    plt.axis("off");
    print(f"Image shape:{img.shape}")
    return img


def show_images_comparator(img_array_1, img_array_2, img_scale=4):
    """
    Display array of pictures side by side to compare.
    Lenght must be equal of the 2 arrays.

  """
    if (len(img_array_1) != len(img_array_2)):
        raise Exception("Length of array 1 and 2 not equal")

    rows = len(img_array_1)

    fig = plt.figure(figsize=(2 * img_scale, img_scale * rows))
    plt.axis('off')

    for img_index in range(len(img_array_1)):
        ax = fig.add_subplot(rows, 2, 2 * img_index + 1)
        ax.imshow(img_array_1[img_index])
        ax.axis('off')
        ax.set_title(f"index: {img_index}")
        ax2 = fig.add_subplot(rows, 2, 2 * img_index + 2)
        ax2.imshow(img_array_2[img_index])
        ax2.axis('off')
