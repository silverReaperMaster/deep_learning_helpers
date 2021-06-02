import zipfile
import shutil

def get_zip_url(_zip_url, _dest_path):
  import requests, zipfile, io
  r = requests.get(_zip_url)
  z = zipfile.ZipFile(io.BytesIO(r.content))
  z.extractall(_dest_path)
  z.close()
  macosx = f"{_dest_path}__MACOSX"
  shutil.rmtree(f"{_dest_path}__MACOSX")
 
