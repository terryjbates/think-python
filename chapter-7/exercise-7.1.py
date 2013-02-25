#!/usr/bin/env python
# encoding: utf-8
"""
exercise-7.1.py

Rewrite program from section 5.8 using iteration instead of recursion.

Created by Terry Bates on 2012-08-21.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved."""

def print_n(s,n):
    while n > 0:
        print s
        n = n -1
    return

if __name__ == '__main__':
    print_n("hello", 5)

