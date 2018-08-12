#!/usr/bin/python

'''
This file implements an example of decorator
'''

# example of a decorator
def my_decorator(func):
    print ("This is functionality decorator adds")

    def internal_function():
        print ("This is some wrapper code")

        # call the original function here
        func()

    return internal_function

@my_decorator
def my_function():
    print ("This is original function")


# call the function
my_function()


# decorator with arguments
def another_decorator(some_parameter = 'dummy value'):
    def the_decorator(func):
        print "some_parameter = {}".format(some_parameter)
        def wrapped_function():
            func()
        return wrapped_function
    return the_decorator

@another_decorator()
def some_function_1():
    print ("Some function 1")

some_function_1()

@another_decorator(some_parameter = 'specific value')
def some_function_2():
    print ("Some function 2")

some_function_2()

# decorator class
class decorator(object):
    def __init__(self, some_parameter = 'dummy value'):
        self.some_parameter = some_parameter

    def __call__(self, func):
        print ("This is decorator: some_parameter = {}".format(self.some_parameter))

        func()
        self.notify()

    def notify(self):
        print ("Decorator Notified")

@decorator()
def yet_another_function():
    print ("Yet another function")

@decorator(some_parameter = 'specific value')
def yet_another_function_2():
    print ("Yet another function 2")