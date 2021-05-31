import os

def clean_files(files_array):
  r = list(filter(lambda x: x.find("DS") < 0, files_array))
  return r



def full_path_array(_dirpath, _dirname, _file_names_array):
  #files = list(map(lambda: file_name: f"{_dirpath}/{_dirname}/{file_name}",_file_names_array))
  return files
 
def info_dir(_dir_path="./"):
  files_array = []
  for dirpath, dirnames, filenames in os.walk(_dir_path):
    print(f"""There are {len(dirnames)} directories and \
        {len(clean_files(filenames))} files in '{dirpath}'""")
    files_array.extend(os.path.join(dirpath, x) for x in clean_files(filenames))
  print("\n\n")
  return files_array