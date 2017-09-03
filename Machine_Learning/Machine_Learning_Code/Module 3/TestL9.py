#!/usr/bin/env python

import unittest

class TestL9(unittest.TestCase):

    def test_OneHotEncoding(self):

        import numpy as np
        import pandas as pd

        X = pd.read_csv(r'./_data/titanic_data.csv')
        print(X.head())
        print('-' * 80)
        X = X.select_dtypes(include=[object])
        print(X.head())
        print(X.)

        from sklearn.preprocessing import LabelEncoder
        from sklearn.preprocessing import OneHotEncoder

        le = LabelEncoder()
        for feature in X:
            le.fit()