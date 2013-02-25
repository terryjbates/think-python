#!/usr/bin/env python
# encoding: utf-8
"""
exercise-6.7.py


First, and likely last, commit of Exercise 6.7. Create an 'is_power' function such that it will return True, if given parameters (a,b), it will return True if a is divisible by b and if a/b is a power of b.


Created by Terry Bates on 2012-08-16.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved."""

import sys
import os


def is_power(a,b):
    # print "a:%s b:%s" % (a, b)
    # print "a % b " + str(a % b)
    # print "a/b " + str(a/b)
    # print "#" * 20
    if (a % b == 0):
        return True
        if (a/b == 1):
            return True
            #print "a/b %s Return TRUE" % (a/b)
        else:
            (is_power (a/b, b) )
    else:
        return False

if __name__ == '__main__':
    print is_power(64,2)
    print is_power(9,2)

