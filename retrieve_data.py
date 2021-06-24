import shutil
import requests
import zipfile
import io


def __complete_path(path):
    if not path.endswith("/"):
        return f"{path}/"
    else:
        return path


def get_zip_url(_zip_url, _destiny_path):
    _destiny_path = __complete_path(_destiny_path)
    r = requests.get(_zip_url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(_destiny_path)
    z.close()
    macosx = f"{_destiny_path}__MACOSX"
    shutil.rmtree(f"{_destiny_path}__MACOSX")

