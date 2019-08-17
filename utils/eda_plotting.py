from . import eda #https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html#targetText=In%20order%20to%20import%20a,py%20is%20a%20Python%20package.
import seaborn as sns
import matplotlib.pyplot as plt
from .eda import Eda

class Eda_Plotting(Eda):
    
    def __init__(self, df=None):
        super().__init__(df)
        
    def plot_value_counts(self, column_name: str, filter_condition=None, figsize=(12,10)):
        #https://datascience.stackexchange.com/questions/17540/make-seaborn-heatmap-bigger
        plt.subplots(figsize=figsize)
        if filter_condition is None:
            _=sns.countplot(x=self.df[column_name])
        else:
            _=sns.countplot(x=self.df.loc[filter_condition, column_name])
    
