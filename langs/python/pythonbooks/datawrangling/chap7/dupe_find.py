#!/usr/bin/env python

list_with_dupes = [1,5,6,2,5,6,8,3,8,3,3,7,9]

set_without_dupes = set(list_with_dupes)

print("Dupe Free: ",set_without_dupes)
print


'''

'''

first_set =  set([1,5,6,2,6,3,6,7,3,7,9,10,321,54,654,432])

second_set = set([4,6,7,432,6,7,4,9,0])

# Print all the ones that are the same
print("Intersection: ", first_set.intersection(second_set))
print

# Print
print("Union: ", first_set.union(second_set))
print

#
print("Difference: ", first_set.difference(second_set))
print
