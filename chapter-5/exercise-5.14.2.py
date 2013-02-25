#!/usr/bin/env python
# encoding: utf-8
"""
exercise-5.14.2.py

Created by Terry Bates on 2012-08-01.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved."""

import sys
import os

def is_triangle(a,b,c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        print "Yes"
    else:
        print "No"

def prompt_user():
    prompt = "Please enter side "
    for value in ['a', 'b', 'c']:
        new_prompt = prompt + value +': ' # modify prompt for value in loop
        my_input = raw_input(new_prompt)   # get input
        float_input = float(my_input)      # convert the entered value to float
        exec ("%s=%f" % (value, float_input))
    a = int(a)
    b = int(b)
    c = int(c)
    is_triangle(a,b,c)

def main():
    # is_triangle(5,3,4)
    # is_triangle(5,3,12)
    prompt_user()

if __name__ == '__main__':
    main()

