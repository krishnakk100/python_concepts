#!/usr/bin/python

"""
This file is to be used for python console and function based debugging
"""
import pdb

def main():
    a = 'some value'
    b = 'some other value'
    pdb.set_trace()
    print 'This is a dummy print statement'

main()