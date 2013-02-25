#!/usr/bin/env python
# encoding: utf-8
"""
exercise-7.4.py

Created by Terry Bates on 2012-08-29.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved."""

import sys
import os

def eval_loop():
    while True:
        user_string = raw_input('>>> ')
        if user_string == 'done':
            break
        else:
            print user_string
            result = eval(user_string)
            print result

if __name__ == '__main__':
    eval_loop()