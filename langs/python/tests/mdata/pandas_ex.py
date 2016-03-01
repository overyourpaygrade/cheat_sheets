#!/usr/bin/env python
#https://www.reddit.com/r/Python/comments/481qpl/easy_way_to_extract_data_from_spreadsheet_using/

import pandas as pd

# Read in data using one of many methods
# Makes student the unique id
marks = pd.read_csv('marks.csv', index_col='student')

# Get the first question column, if no spaces, 
# you can use dot for lookup
# Ex: print marks.question1
print "\nExample 1"
print marks['question 1']

# Returns a series of bools where students answered 'y'
# for question 1
print "\nExample 2"
print marks['question 1'] == 'y'

# Combine bools into a single series, where true is where
# students answered 'y' for question 1 and 'n' for 
# question 2 (and: &) (or: |) parentheses matter
print "\nExample 3"
print (marks['question 1'] == 'y') & (marks['question 2'] == 'n')

# Using a series of booleans as a look-up, create a new
# dataframe with just the matches, therefore this filters all the 
# data to just those students who answer 'y' for question 1 and 
# 'n' for question 2
print "\nExample 4"
print marks[(marks['question 1'] == 'y') & \
    (marks['question 2'] == 'n')]

# You can the lookup what you want from the result, in this case
# look up the answers students gave for question 4, if they 
# answered 'y' for question 1 and 'n' for question 2
print "\nExample 5"
print marks[(marks['question 1'] == 'y') & \
    (marks['question 2'] == 'n')]['question 4']
