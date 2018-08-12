#!/usr/bin/python

'''
This file implements an example of generators
'''

# example generator
def fibon(n):
    a = b = 1

    for i in range(n):
        yield a
        a, b = b, a + b

def main():
    for x in fibon(1000):
        print (x)

main()