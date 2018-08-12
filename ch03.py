#!/usr/bin/python

'''
This file implements an example of map, filter and reduce
'''

# example of map
items = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, items))
print ("Example of Map.\n Converted {}\n to {}\n".format(items, squared))


# example of filters
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x<0, number_list))
print ("Filtered everything less that zero: {}".format(less_than_zero))

# example of reduce
from functools import reduce
product = reduce((lambda x,y:x*y), [1, 2, 3, 4])
print ("Reduced result: {}".format(product))