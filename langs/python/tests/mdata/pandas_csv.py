#!/usr/bin/env python
# http://chrisalbon.com/python/pandas_dataframe_importing_csv.html

import pandas as pd
import numpy as np

raw_data = {'first_name':['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
    'last_name':['Miller', 'Jacobson', '.', 'Milner', 'Cooze'],
    'age': [42, 52, 36, 24, 73],
    'preTestScore': [4, 24, 31, '.', '.'],
    'postTestScore': ['25,000', '94,000', 57, 62, 70]}

df = pd.DataFrame(raw_data, columns = ['first_name','last_name','age',
    'preTestScore', 'postTestScore'])

print df

# Save to csv file
df.to_csv('example.csv')

# Load a csv file
fh = pd.read_csv('example.csv')
print fh

# Load with no headers
fh = pd.read_csv('example.csv', header=None)
print fh

# Load specific column names
df = pd.read_csv('example.csv', header=True, names=['UID','First Name',
    'Last Name', 'Age', 'Pre-Test Score', 'Post-Test Score'])
print df

#Load a csv with setting the index column to UID
df = pd.read_csv('example.csv', index_col='UID', header=True, names=['UID',
    'First Name', 'Last Name', 'Age', 'Pre-Test Score', 'Post-Test Score'])
print df

# Load a csv while specifying "." as missing values
df = pd.read_csv('example.csv', na_values=['.'])
print pd.isnull(df)
