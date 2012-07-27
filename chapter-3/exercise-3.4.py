#!/usr/bin/env python
# encoding: utf-8
"""
exercise-3.4.py

Created by Terry Bates on 2012-07-14.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com. All rights reserved.
"""

import sys
import os

# 3. Takes string param, prints twice
def print_twice(my_string):
    print my_string
    print my_string

# 2. passing value as an argument
# def print_spam(num):
#     print 'spam'*num

# 1. script and test 
# def do_twice(f): # this takes function object as an argument
#     f()
#     f()

def do_twice(f,num): # this takes function object as an argument
    f(num)
    f(num)

# 5. define new function, takes a function object and param
# no need to have four statements, by re-using code
def do_four(f,num): # this takes function object as an argument
    do_twice(f,num)
    do_twice(f,num)

# 4. implicitly do "print_twice" passing 'spam' as an argument

def main():
    do_four(print_twice,'spam') 

if __name__ == '__main__':
    main()

