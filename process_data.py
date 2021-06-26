import pandas as pd


def list_to_data_frame(_data_list, key_name='name', value_name='value') -> pd.DataFrame:
    return pd.DataFrame({
        f"{key_name}": list(_data_list.keys()),
        f"{value_name}": list(_data_list.values())}
    )
