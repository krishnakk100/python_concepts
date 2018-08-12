#!/usr/bin/python

'''
This file implements an example of ternary operators
'''

# example of ternary operator
is_fat = True

state = 'Yes!' if is_fat else 'No!'
print ("Is fat? : {}".format(state))

# another example
state = ("No!","Yes!")[is_fat]
print ("Is fat? : {}".format(state))