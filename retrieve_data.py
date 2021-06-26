import os.path
import shutil
import requests
import zipfile
import io
from tqdm import tqdm
import re
from os_helper import delete_file


def __complete_path(path):
    if not path.endswith("/"):
        return f"{path}/"
    else:
        return path


def get_zipped_content_url(_zip_url, _destiny_path, force_update=False):
    _destiny_path = __complete_path(_destiny_path)

    zip_str = download(_zip_url, _destiny_path, force_update)

    with zipfile.ZipFile(zip_str) as zf:
        for member in tqdm(zf.infolist(), desc='Extracting '):
            try:
                zf.extract(member, _destiny_path)
            except zipfile.error as e:
                pass
    zf.close()
    macosx = f"{_destiny_path}__MACOSX"
    shutil.rmtree(f"{macosx}")


def download(_url, _destiny_folder, force_update=False):
    _file_name = _url.split("/")[-1]
    full_path = f"{__complete_path(_destiny_folder)}{_file_name}"

    if force_update:
        delete_file(full_path)

    if os.path.isfile(full_path):
        return full_path

    resp = requests.get(_url, stream=True)
    total = int(resp.headers.get('content-length', 0))

    with open(full_path, 'wb') as file, tqdm(
            desc=full_path,
            total=total,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
    ) as bar:
        for data in resp.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)

    return full_path
