#!/usr/bin/env python
# encoding: utf-8
"""
exercise-3.4.py

Created by Terry Bates on 2012-07-14.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved.
"""

import sys
import os


def print_twice(my_string):
    print my_string
    print my_string


def do_twice(f, num):
    f(num)
    f(num)


def do_four(f, num):
    do_twice(f, num)
    do_twice(f, num)


def main():
    do_four(print_twice, 'spam')


if __name__ == '__main__':
    main()
