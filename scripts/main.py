import numpy as np
import pandas as pd

if __name__ == "__main__":
    df=pd.read_csv('../data/product_sample.csv', sep=',',header=None)
    print(df)