#!/usr/bin/env python
# encoding: utf-8
"""
exercise-6.3.py

Implement 'is_between' funciton to return True if x <= y <= z, False otherwise

Created by Terry Bates on 2012-08-15.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved."""


def is_between(x, y, z):
    if x <= y <=z:
        return True
    else:
        return False

if __name__ == '__main__':
    print is_between(3, 4, 5)
    print is_between(2, 0, 7)