import numpy as np
import pandas as pd
from IPython.display import display, clear_output
import ipywidgets as widgets

def load_and_describe_data(csv_file_path_name):
    """Function to load data into a Pandas DataFrame and
       describe the data"""
    df = pd.read_csv(csv_file_path_name)
    df.columns = [col_name.lower() for col_name in df.columns]
    print('*'*10 + ' info ' + '*'*10)
    print(df.info())
    print('*'*10 + ' columns ' + '*'*10)
    print(df.columns)
    print('*'*10 + ' number of duplicated rows ' + '*'*10)
    print(df.duplicated().sum())
    print('*'*10 + ' number of nulls in columns ' + '*'*10 )
    print(df.isnull().sum())
    print('*'*10 + ' describe ' + '*'*10)
    print(df.describe())
    return df


def check_for_constant_columns(df):
    columns_with_one_unique_val = []
    for col in df.columns:
        if df[col].nunique() == 1:
            #print(df[col].nunique())
            #print(col)
            columns_with_one_unique_val.append(col)
    return columns_with_one_unique_val


def view_column_value_counts(df):
    def print_value_counts(df, column_name):
        print(df[column_name].value_counts())
    
    #https://stackoverflow.com/questions/53791590/jupyter-ipywidgets-how-to-refresh-plot-using-dropdown-menu
    w_val_counts = widgets.Dropdown(
        options=df.columns,
        value=df.columns[0],
        description='Columns',
    )
    display(w_val_counts)

    def on_change(change):
        if change['name'] == 'value' and (change['new'] != change['old']):
            clear_output()
            display(w_val_counts)
            print_value_counts(df, change['new'])

    w_val_counts.observe(on_change)
    

def check_cardinality_of_data(df):
    print("Cardinality of data")
    for col in df.columns:
        print(f"{col} : {df[col].nunique()}")