#!/usr/bin/env python
# encoding: utf-8
"""
exercise-6.1.py

Write a compare function.
Return 1 if x > y
Return 0 if x == y
Return -1 if x < y

Created by Terry Bates on 2012-08-14.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved."""

import sys
import os


def compare(x,y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else: # Implicit
        return -1
        

if __name__ == '__main__':
    print compare(5,6)
    print compare(3,2)
    print compare(2,2)
