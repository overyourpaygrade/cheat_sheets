#!/usr/bin/env python

# Loop over something and have an automatic counter. 
my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 1):
    print c, value

# The optional argument allows us to tell enumerate from where 
# to start the index. You can also create tuples containing the 
# index and list item using a list.
counter_list = list(enumerate(my_list, 1))
print counter_list
