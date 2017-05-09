#!/usr/bin/env python

import unittest

from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd
import sys
import os
import matplotlib
import numpy as np
from numpy import random

#%matplotlib inline

class TestPandas(unittest.TestCase):
    def setUp(self):
        print('Python version ' + sys.version)
        print('Pandas version ' + pd.__version__)
        print('Matplotlib version ' + matplotlib.__version__)

    def n_test_L1(self):
        # create data
        names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
        births = [968, 155, 77, 578, 973]

        df = pd.DataFrame(list(zip(names, births)), columns=['Names', 'Births'], index=range(1, len(names)+1))
        #df = pd.DataFrame(list(zip(names, births)),  index=range(1, len(names)+1))
        print(df)
        print('df.dtypes:\n' + str(df.dtypes))
        print('type of df.Names', type(df.Names))
        print('-'*20)

        # just for test
        df2 = pd.DataFrame(np.random.randn(10,5), columns=['a', 'b', 'c', 'd', 'e'], index=range(1, 11))
        #print(df2)

        csv_file = 'births1880.csv'
        df.to_csv(csv_file, index=False, header=False)
        df3 = pd.read_csv(csv_file, names=['name', 'births'])
        print(df3)
        print('-'*20)
        os.remove(csv_file)
        
        Sorted = df.sort_values(['Births'], ascending=False)
        print(Sorted.head())

        df['Births'].plot()
        # Maximum value in the data set
        MaxValue = df['Births'].max()

        # Name associated with the maximum value
        MaxName = df['Names'][df['Births'] == df['Births'].max()].values
        
        # Text to display on graph
        Text = str(MaxValue) + " - " + MaxName
        
        # Add text to graph
        plt.annotate(Text, xy=(2, MaxValue), xytext=(8, 0), 
                         xycoords=('axes fraction', 'data'), textcoords='offset points')
        
        print("The most popular name")
        df[df['Births'] == df['Births'].max()]
        plt.show()
    
    def test_L2(self):
        # The inital set of baby names
        names = ['Bob','Jessica','Mary','John','Mel']
        
        random.seed(500)
        random_names = [ names[random.randint(low=0, high=len(names))] for i in range(1000)]
        print(random_names[:10])

        births = [ random.randint(low=0, high=1000) for i in range(1000)]
        print(births[:10])
        df = pd.DataFrame(list(zip(random_names, births)), columns=['Names', 'Births'])
        print(df[:10])

        csv_file = 'births1880.txt'
        df.to_csv(csv_file, index=False, header=False)
        
        df2 = pd.read_csv(csv_file, names=['Names', 'Births'])
        df2.info()
        print(df2['Names'][df2['Names'] == 'Mary'])
        os.remove(csv_file)

        arr = df2['Names'].unique()
        print(type(arr))
        for x in arr:
            print(x)
        
        print(df2['Names'].describe())

        name = df2.groupby('Names')
        print(type(name), name)


if __name__ == '__main__':
    unittest.main()