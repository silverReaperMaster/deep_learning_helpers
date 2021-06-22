import os


def clean_files(files_array):
    r = list(filter(lambda x: x.find("DS") < 0, files_array))
    return r


# def full_path_array(_dir_path, _dir_name, _file_names_array):
#     # files = list(map(lambda: file_name: f"{_dir_path}/{_dir_name}/{file_name}",_file_names_array))
#     return files


def info_dir(_dir_path="./"):
    files_array = []
    for dir_path, dir_names, filenames in os.walk(_dir_path):
        print(f"""There are {len(dir_names)} directories and \
        {len(clean_files(filenames))} files in '{dir_path}'""")
        files_array.extend(os.path.join(dir_path, x) for x in clean_files(filenames))
    print("\n\n")
    return files_array


if __name__ == '__main__':
    print("main")


    # _food_classes_10_percent.zip
    #
    # unzip_data("101_food_classes_10_percent.zip")
    #
    # train_dir = "101_food_classes_10_percent/train/"
    # test_dir = "101_food_classes_10_percent/test/"