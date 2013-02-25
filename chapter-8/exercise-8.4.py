#!/usr/bin/env python
# encoding: utf-8
"""
execrise-8.3.py

Created by Terry Bates on 2012-09-05.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved."""

import sys
import os


def find(word,letter,start):
    if start:
        index = start
    else:
        index = 0
    while index < len(word):
        if word[index] == letter:
            print "our index : ", index
            return index
        index = index + 1
    return -1
    


if __name__ == '__main__':
    my_string ='foo fighters rock'
    print my_string
    print my_string[0]
    print "we found 'o' at ", find(my_string, 'o', 6)
    print "we found 'f' at", find(my_string, 'f', 0)
    print "we found 'h' at", find(my_string, 'h', 0)
