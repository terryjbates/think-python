#!/usr/bin/env python
# encoding: utf-8
"""
exercise-6.5.py

Implementation of the Ackermann function.

Appears that ack(3,4) ends easily at 125, going to (4,4) seems to run endlessly. We *definitely* hit recursion depth:

import cProfile
s = 'ack(3,4)'
cProfile.run(s)
...
Runtime Error Maximum recursion depth exceeded.

Created by Terry Bates on 2012-08-15.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved."""

import sys
import os


def ack(m,n):
    if m == 0:
        return n + 1
    elif m > 0: # we use DRY
        if n == 0:
            return ack(m-1,1) 
        elif n > 0:
            return ack(m-1, ack(m,n-1))



if __name__ == '__main__':
    print ack(3,4)
    print ack(4,4)

