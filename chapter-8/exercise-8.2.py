#!/usr/bin/env python
# encoding: utf-8
"""
execrise-8.2.py

Created by Terry Bates on 2012-09-05.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved."""



if __name__ == '__main__':
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'

    for letter in prefixes:
        if (letter in 'O') or (letter in 'Q'):
            letter = letter + 'u'
        print letter + suffix
    
