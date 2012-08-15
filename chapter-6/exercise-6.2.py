#!/usr/bin/env python
# encoding: utf-8
"""
exercise-6.2.py

Script to incrementally develop 'hypotenuse' function. Return length of hypotenuse of right triangle,
give length of two legs as an argument. Record each step as you go.


Created by Terry Bates on 2012-08-14.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com. All rights reserved.
"""

import sys
import os
import math

def hypotenuse(x,y):
    # hypotenuse  x**2 + y**2 = z**2
    # so, compute squares of arguments, add together    
    legs_squared = x**2 + y**2

    # then take square root of them, return that value
    # to do that we need the math module
    hypotenuse_value = math.sqrt(legs_squared)
    print hypotenuse_value
    return hypotenuse_value

if __name__ == '__main__':
    hypotenuse(3,4)

