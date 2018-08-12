#!/usr/bin/python

# This file implements examples of *args and **kwargs

def args_function(*args):
    for value in args:
        print value

def kwargs_function(**kwargs):
    for key, value in kwargs.items():
        print ("Key: {}, Value: {}".format(key, value))

# using the above functions
args_function("1", "2", "3")
kwargs_function(one=1, two=2, three=3)
