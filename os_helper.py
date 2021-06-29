import os
import sys
import subprocess
import pkg_resources

from urllib.request import urlopen
import subprocess
import sys
import re
from io import StringIO
from bs4 import BeautifulSoup
import pandas as pd
import warnings


def clean_gpu_name(_gpu_result_str):
    name_regex_extract = re.compile("^(.*?)(?=-)")
    name = re.match(name_regex_extract, _gpu_result_str).group(0)
    return name


def check_hw():
    gpu_params = ["name"]
    command_out = subprocess.run(["nvidia-smi",
      f"--query-gpu={','.join(gpu_params)}", "--format=csv"],
      stdout=subprocess.PIPE,
      text=True, input="")

    if "NVIDIA-SMI has failed because it couldn't communicate with the NVIDIA driver" in command_out.stdout:
      print ("NVIDIA-SMI has failed because it couldn't communicate with the NVIDIA driver")
      return

    command_str_io = StringIO(command_out.stdout)
    # print(command_out.stdout)
    command_out_results = pd.read_csv(command_str_io, sep=",")
    # print(command_out_results.head())
   
    gpu_name = clean_gpu_name(command_out_results['name'].iloc[0])

    url = "https://developer.nvidia.com/cuda-gpus#compute"
    cuda_page = urlopen(url)
    bs = BeautifulSoup(cuda_page, "html.parser")
    a_element = bs.body.find('a', text=f"{gpu_name}")
    row = a_element.parent.parent
    compute_value = float(row.findChildren('td')[1].text)

    print("\n\t***GPU values***")
    print(f"GPU Name: [{gpu_name}] compute value :[{compute_value}] \n")

    if compute_value < 7:
        warnings.warn("Compute capability under 7.0 and is not expected to show a significant speedup")


def delete_file(_file_path):
    try:
        os.remove(_file_path)
    except OSError:
        pass


def clean_files_filter(files_array):
    r = list(filter(lambda x: x.find("DS") < 0, files_array))
    return r


def info_dir(_dir_path="./"):
    files_array = []
    for dir_path, dir_names, filenames in os.walk(_dir_path):
        print(f"""There are {len(dir_names)} directories and \
        {len(clean_files_filter(filenames))} files in '{dir_path}'""")
        files_array.extend(os.path.join(dir_path, x) for x in clean_files_filter(filenames))
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
