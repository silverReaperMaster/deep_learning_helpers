import numpy
import matplotlib.pyplot as plt
import matplotlib.ticker as tic
import math
import matplotlib.image as mpimg
import numpy


def get_title(title, index=None):
    if isinstance(title, numpy.ndarray):
        return (f"{title[index]}")

    if isinstance(title, list):
        return (f"{title[index]}")

    if isinstance(title, str):
        return (f"{title}")

    return "Missing"


def display_image(_target_image, _title="", _y_title="", _fig_size=(10, 10), _columns=1):
    if isinstance(_target_image, tf.data.Dataset):
        fig = plt.figure(figsize=_fig_size, constrained_layout=True)
        gs = fig.add_gridspec(ncols=_columns, nrows=math.ceil(len(_target_image) / _columns), hspace=0, wspace=0)

        for i, (image, label) in enumerate(_target_image):
            ax = fig.add_subplot(gs[math.floor(i / _columns), i % _columns])
            ax.imshow(image)
            ax.set_title(f"{get_title(_title, i)}")
            plt.setp(ax.get_xticklabels(), visible=False)
            plt.setp(ax.get_yticklabels(), visible=False)
        plt.show()

    if isinstance(_target_image, numpy.ndarray):
        fig = plt.figure(figsize=_fig_size, constrained_layout=True)
        gs = fig.add_gridspec(ncols=_columns, nrows=math.ceil(len(_target_image) / _columns), hspace=0, wspace=0)
        for i in range(len(_target_image)):
            ax = fig.add_subplot(gs[math.floor(i / _columns), i % _columns])
            v = _target_image[i]
            ax.imshow(v)
            set_title(ax, _title, i)
            plt.setp(ax.get_xticklabels(), visible=False)
            plt.setp(ax.get_yticklabels(), visible=False)
        plt.show()


def display_image_from_file(_target_files, _title="", _y_title="", _fig_size=(10, 10), _columns=1):
    if isinstance(_target_files, str):
        img = mpimg.imread(_target_files)
        plt.imshow(img)
        plt.title(_title)
        plt.axis("off")
        return img

    if isinstance(_target_files, numpy.ndarray):
        print("Array")
        fig = plt.figure(figsize=_fig_size, constrained_layout=True)
        gs = fig.add_gridspec(ncols=_columns, nrows=math.ceil(len(_target_files) / _columns), hspace=0, wspace=0)
        for i in range(len(_target_files)):
            img = mpimg.imread(_target_files[i])
            ax = fig.add_subplot(gs[math.floor(i / _columns), i % _columns])
            ax.imshow(img)
            ax.set(title=f"{_title[i]}", ylabel=f"{_y_title[i]}")
            plt.setp(ax.get_xticklabels(), visible=False)
            plt.setp(ax.get_yticklabels(), visible=False)

        plt.show()


def show_images_comparator(img_array_1, img_array_2, img_scale=4):
    """
    Display array of pictures side by side to compare.
    Lenght must be equal of the 2 arrays.

  """
    if len(img_array_1) != len(img_array_2):
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
