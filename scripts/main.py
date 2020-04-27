import numpy as np
import pandas as pd


class Analyzer():
    def __init__(self,filename):
        self.data=pd.read_csv(filename, sep=',')
        self.products = self.data['product'].unique()
        self.outcome = self.data['title'].unique()
        self.site_version = self.data['site_version'].unique()

    def analyze_categories(self):
        for category in self.products:
            c = data[data['product'].str.match(category)]
            # for criteria in ['']

if __name__ == "__main__":
    analyzer = Analyzer('../data/product_sample.csv')
    
        
