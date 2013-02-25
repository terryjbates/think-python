#!/usr/bin/env python
# encoding: utf-8
"""
exercise-7.3.py

Created by Terry Bates on 2012-08-29.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved."""
import math



def square_root(a):
    # we will guess that x will be 1/2 of a, to start
    x =  0.75 * float(a)
    epsilon = 0.000001
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        x = y
    return x
    

if __name__ == '__main__':

    for n in range(1, 10):
        print n, "\t",
        print square_root(n),"\t",
        print math.sqrt(n),"\t",

        print abs(square_root(n) - math.sqrt(n))

