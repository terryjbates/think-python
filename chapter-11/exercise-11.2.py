#!/usr/bin/env python
# encoding: utf-8
"""
exercise-11.2.py

Write a more concise version of histogram function.

Created by Terry Bates on 2012-10-31.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved."""

def histogram(s):
    d = dict()
    for c in s:
        dict_value = d.get(c,0)
        d[c] = dict_value + 1 
    return d

def main():
    histogram('h')

if __name__ =='__main__':
    main()