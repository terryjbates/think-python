#!/usr/bin/env python
# encoding: utf-8
"""
execrise-8.5.py

Created by Terry Bates on 2012-09-05.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com. All rights reserved.
"""

import sys
import os


def count(word, letter):
    count = 0
    for char in word:
        if char == letter:
            count = count + 1
    print count


if __name__ == '__main__':
    count('foo fighters rule', 'e')

