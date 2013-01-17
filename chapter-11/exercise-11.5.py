#!/usr/bin/env python
# encoding: utf-8
"""
exercise-11.5.py

Use the documentation of the 'setdefault' method to write a more concise version of invert_dict.

Created by Terry Bates on 2013-01-08.
Copyright (c) 2013 http://the-awesome-python-blog.posterous.com. All rights reserved.
"""

import sys
import os

def invert_dict(d):
    inv = dict()
    for key in d:
        val = d[key]
        inv.setdefault(val,[]).append(key)
    return inv
    
def histogram(s):
    d = dict()
    for c in s:
        dict_value = d.get(c,0)
        d[c] = dict_value + 1 
    return d

def main():
    h = histogram('parrot')
    k = invert_dict(h)
    print k


if __name__ == '__main__':
    main()

