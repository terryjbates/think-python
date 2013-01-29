#!/usr/bin/env python
# encoding: utf-8
"""
exercise-12.1.py

A script to create a function called "sumall" that will take any number of arguments and return their sum.


Created by Terry Bates on 2012-07-13.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

def sumall(*args):
    t = tuple(args)
    return sum(t)

def main():
    print sumall(1,2,34,5)

if __name__ == '__main__':
    main()
