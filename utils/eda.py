import numpy as np
import pandas as pd
from IPython.display import display, clear_output
import ipywidgets as widgets
        
        
class Eda:
    
    def __init__(self, df=None):
        #https://stackoverflow.com/questions/11707586/how-do-i-expand-the-output-display-to-see-more-columns
        #pd.set_option('display.expand_frame_repr', False)
        #pd.set_option('display.max_rows', 50)
        #pd.set_option('display.max_columns', 50)
        pd.set_option('display.width', 0)
        if df is not None:
            self.df = df

    def load_data(self, csv_file_path_name: str):
        #head_csv = !head -n3 "{csv_file_path_name}"
        #print(head_csv)
        df = pd.read_csv(csv_file_path_name, parse_dates=True, infer_datetime_format=True)
        df.columns = [col_name.lower().strip() for col_name in df.columns]
        self.df = df
        
    def view_data_details(self):
        #df = pd.read_csv(csv_file_path_name)
        
        print('*'*10 + ' info ' + '*'*10)
        print(self.df.info())
        print('*'*10 + ' columns ' + '*'*10)
        print(self.df.columns)
        print('*'*10 + ' number of duplicated rows ' + '*'*10)
        print(self.df.duplicated().sum())
        print('*'*10 + ' number of nulls in columns ' + '*'*10 )
        print(self.df.isnull().sum())
        print('*'*10 + ' describe ' + '*'*10)
        print(self.df.describe())
        print('*'*10 + ' df.head ' + '*'*10)
        print(self.df.head(2).T)
        #return df
        #self.df = df

    def check_for_constant_columns(self):
        columns_with_one_unique_val = []
        for col in self.df.columns:
            if self.df[col].nunique() == 1:
                #print(df[col].nunique())
                #print(col)
                columns_with_one_unique_val.append(col)
        return columns_with_one_unique_val

    def view_column_value_counts(self):
        def print_value_counts(df, column_name):
            print(df[column_name].value_counts())

        #https://stackoverflow.com/questions/53791590/jupyter-ipywidgets-how-to-refresh-plot-using-dropdown-menu
        w_val_counts = widgets.Dropdown(
            options=self.df.columns,
            value=self.df.columns[0],
            description='Columns',
        )
        display(w_val_counts)
        print_value_counts(self.df, w_val_counts.value)
        def on_change(change):
            if change['name'] == 'value' and (change['new'] != change['old']):
                clear_output()
                display(w_val_counts)
                print_value_counts(self.df, change['new'])

        w_val_counts.observe(on_change)

    def view_cardinality_of_data(self):
        print("Cardinality of data")
        for col in self.df.columns:
            print(f"{col} : {self.df[col].nunique()}")
