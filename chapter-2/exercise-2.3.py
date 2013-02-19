#!/usr/bin/env python
# encoding: utf-8
"""
exercise-2.3.py

A script to print values of expressions.

Created by Terry Bates on 2012-07-13.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved.
"""

import sys
import os


def main():
    width = 17
    height = 12.0
    delimiter = '.'

    # type should be int
    print width/2
    # type should be float
    print width/2.0

    # type should be float
    print height/3

    # type should be int
    print 1 + 2 * 5

    # type should be string
    print delimiter * 5


if __name__ == '__main__':
    main()
