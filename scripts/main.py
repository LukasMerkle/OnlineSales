import numpy as np
import pandas as pd
import datetime

class Analyzer():
    def __init__(self,filename):
        self.data=pd.read_csv(filename, sep=',')
        self.products = self.data['product'].unique()
        self.outcome = self.data['title'].unique()
        self.site_version = self.data['site_version'].unique()
        self.columns = [['order_id', 'user_id', 'page_id', 'product', 'site_version', 'time','title', 'target']]
        self.convert_to_timeofday()

    def analyze_categories(self):
        for category in self.products:
            c = self.data[self.data['product'].str.match(category)]
            for outcome in self.outcome:
                outcome_result = c[c['title'].str.match(outcome)]
                print("Probabilty of",outcome,"given the category",category,"is",outcome_result.shape[0]/c.shape[0])

    def analyze_site_version(self):
        for category in self.site_version:
            c = self.data[self.data['site_version'].str.match(category)]
            for outcome in self.outcome:
                outcome_result = c[c['title'].str.match(outcome)]
                print("Probabilty of",outcome,"given the category",category,"is",outcome_result.shape[0]/c.shape[0])
    
    def convert_to_timeofday(self):
        time_morning_start = datetime.time(5,0,0)
        time_morning_end = datetime.time(11,0,0)
        time_afternoon_end = datetime.time(16,0,0)
        time_evening_end = datetime.time(20,0,0)
        time_of_day = []
        for time in self.data['time']:
            time = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S').time()
            if (time > time_morning_start and time <= time_morning_end):
                time_of_day.append("Day")
            elif (time > time_morning_end and time <= time_afternoon_end):
                time_of_day.append("Afternoon")
            elif (time > time_afternoon_end and time <= time_evening_end):
                time_of_day.append("Evening")
            else:
                time_of_day.append("Night")
        self.data['time_of_day'] = time_of_day

if __name__ == "__main__":
    analyzer = Analyzer('../data/product_sample.csv')
    print("Categories")
    analyzer.analyze_categories()
    print("Site Version")
    analyzer.analyze_site_version()