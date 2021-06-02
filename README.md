
## Download and Unzip

```python
import zipfile

branch = 'main'
!rm -r -f deep_lerning_helpers-{branch}
!rm -r -f dl_helpers
!wget https://github.com/silverReaperMaster/deep_learning_helpers/archive/refs/heads/{branch}.zip -O deep_learning_helpers.zip

zip_ref = zipfile.ZipFile("deep_learning_helpers.zip")

zip_ref.extractall()
zip_ref.close()
!mv -f deep_learning_helpers-{branch} dl_helpers
!rm -f deep_learning_helpers.zip
```

If all went ok you should see a folder called "dl_helpers" with python files to use.

## Add folder to reference
```python
import sys 
sys.path.append('/content/dl_helpers')
%load_ext autoreload
```

## Import and use 
```python
%autoreload 2
from  history import display_history

display_history(history_1)
```
