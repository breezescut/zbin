#! /usr/bin/env python
# coding-utf-8

# python 3

import numpy as np
from sklearn.naive_bayes import GaussianNB

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2], [-1, 1], [-2, 2], [1, -1], [5, 5], [5, 6]])
Y = np.array([1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 5])

clf = GaussianNB()
clf.fit(X, Y)

print(clf.predict([[-0.8, -1]]))
print(clf.predict([[0.8, 1]]))
print(clf.predict([[-0.8, 1]]))
print(clf.predict([[0.8, -1]]))
print(clf.predict([[3, 7]]))
