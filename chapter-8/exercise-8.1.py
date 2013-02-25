#!/usr/bin/env python
# encoding: utf-8
"""
execrise-8.1.py

Created by Terry Bates on 2012-09-05.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved."""

import sys
import os


def backward_with_lines(word):
    index = len(word)
    while index > 0:
        print word[index-1]
        index = index -1

if __name__ == '__main__':
	backward_with_lines('foo')

