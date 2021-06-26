import os
import sys
import subprocess
import pkg_resources


def delete_file(_file_path):
    try:
        os.remove(_file_path)
    except OSError:
        pass


def clean_files_filter(files_array):
    r = list(filter(lambda x: x.find("DS") < 0, files_array))
    return r


# def full_path_array(_dir_path, _dir_name, _file_names_array):
#     # files = list(map(lambda: file_name: f"{_dir_path}/{_dir_name}/{file_name}",_file_names_array))
#     return files


def info_dir(_dir_path="./"):
    files_array = []
    for dir_path, dir_names, filenames in os.walk(_dir_path):
        print(f"""There are {len(dir_names)} directories and \
        {len(clean_files_filter(filenames))} files in '{dir_path}'""")
        files_array.extend(os.path.join(dir_path, x) for x in clean_files(filenames))
    print("\n\n")
    return files_array


def required_packages(required={}):
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed
    if missing:
        python = sys.executable
        subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)


if __name__ == '__main__':
    print("main")
