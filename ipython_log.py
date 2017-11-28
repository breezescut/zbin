# IPython log file

from pandas import Series, DataFrame
import pandas as pd
obj = Series([4, 7, -5, 3])
obj
obj.values
obj.index
obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
obj2
obj2.index
obj2[obj2> 0]
sdata = {'Ohio':3500, 'Texas':710000, 'Oregon': 16000, 'Utah': 5000}
obj3 = Series(sdata)
obj3
get_ipython().magic('logstart')
# for DataFrame Study
data = {'state':['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada']},
data = {'state':['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'], 
'year': [2000, 2001, 2002, 2001, 2002],
'pop': [1.5, 1.7, 3.6, 2.4 2.9]}
data = {'state':['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'], 
'year': [2000, 2001, 2002, 2001, 2002],
'pop': [1.5, 1.7, 3.6, 2.4 2.9] }
data = {'state':['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'], 
'year': [2000, 2001, 2002, 2001, 2002],
'pop': [1.5, 1.7, 3.6, 2.4, 2.9] }
data
frame = DataFrame(data)
frame
frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
index=['one', 'two', 'three', 'four', 'five'])
frame2
frame2.abs
frame2.all
frame2.columns
frame2.index
