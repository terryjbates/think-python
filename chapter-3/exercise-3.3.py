#!/usr/bin/env python
# encoding: utf-8
"""
exercise-3.3.py

Created by Terry Bates on 2012-07-14.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved.
"""

import sys
import os

# Right justify a string so that last letter is in column 70 of display
# Could be done with a one-liner, but be nice.


def right_justify(s):
    # figure out how much space to offset
    offset = 70 - len(s)
    # print out leading spaces then original parameter value
    print ' '*offset + s


def main():
    right_justify('allen')


if __name__ == '__main__':
    main()
