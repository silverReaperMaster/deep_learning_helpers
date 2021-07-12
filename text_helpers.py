import pandas as pd

def words_count(panda_data, column_name='text'):
  return panda_data[column_name].apply(lambda x: len(x.split()))

