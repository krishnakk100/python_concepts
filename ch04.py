#!/usr/bin/python

'''
This file implements an example of set data structure and difference
'''

# example of set formation
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = set([x for x in some_list if some_list.count(x) > 1])
print ("Duplicate Entries: {}".format(duplicates))

# example of difference
valid = set([1, 2, 3, 4])
input_set = set([3, 10])
print ("Difference: {}".format(input_set.difference(valid)))