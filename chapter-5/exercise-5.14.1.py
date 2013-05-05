#!/usr/bin/env python
# encoding: utf-8
"""
exercise-5.14.1.py

Created by Terry Bates on 2012-08-01.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved."""

import sys
import os
import math


def check_fermat(a, b, c, n):
    '''This function does the actual checking of Fermat's last theorem.
    There should be no such integers such that
    a^n + b^n = c^n
    for n values greater than 2.
    '''
    left_side = pow(a, n) + pow(b, n)
    right_side = pow(c, n)
    if (n > 2) and (left_side == right_side):
        print "Holy Smokes, Fermat was wrong!"
    else:
        print "No, that doesn't work."


def prompt_user():
    '''Prompt the user to input the required values
    for Fermat's last theorem
    Use a for loop to avoid repeated prompts
    '''
    # create general prompt
    prompt = "Please enter "
    for value in ['a', 'b', 'c', 'n']:
        new_prompt = prompt + value + '\n'  # modify prompt for value in loop
        my_input = raw_input(new_prompt)  # get input
        float_input = float(my_input)  # convert the entered value to float
        exec ("%s=%f" % (value, float_input))
    # call check_fermat function
    check_fermat(a, b, c, n)


def main():
    prompt_user()


if __name__ == '__main__':
    main()
