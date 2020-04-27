import numpy as np
import pandas as pd


class Analyzer():
    def __init__(self,filename):
        self.data=pd.read_csv(filename, sep=',')
        self.products = self.data['product'].unique()
        self.outcome = self.data['title'].unique()
        self.site_version = self.data['site_version'].unique()
        self.columns = [['order_id', 'user_id', 'page_id', 'product', 'site_version', 'time','title', 'target']]

    def analyze_categories(self):
        for category in self.products:
            c = self.data[self.data['product'].str.match(category)]
            for outcome in self.outcome:
                outcome_result = c[c['title'].str.match(outcome)]
                print("Probabilty of",outcome,"given the category",category,"is",outcome_result.shape[0]/c.shape[0])
if __name__ == "__main__":
    analyzer = Analyzer('../data/product_sample.csv')
    analyzer.analyze_categories()
    
        
