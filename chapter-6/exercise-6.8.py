#!/usr/bin/env python
# encoding: utf-8
"""
exercise-6.8.py

Greatest commond divisor with Euclid's algorithm. PITA to realize that we must return the function vaule, not simply invoke the gcd function via recursion.

Created by Terry Bates on 2012-08-19.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved."""


def gcd(a,b):
    # catch base case from the door
    if b == 0:
        return a
    # otherwise, do the other steps
    else:
        # compute remainder
        remainder = a % b
        # If we have base case, no need to
        # call again
        if remainder == 0:
            return b
        # otherwise, we recurse and grab the return value
        else:
            return gcd(b, remainder)


if __name__ == '__main__':
    print  gcd(9, 3)
    print gcd(15, 12)
    print gcd(24,8)