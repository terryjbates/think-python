#!/usr/bin/env python
# encoding: utf-8
"""
exercise-17.2.py

Created by Terry Bates on 2014-02-19.
Copyright (c) 2014 http://the-awesome-python-blog.posterous.com.
All rights reserved.
"""


class Point(object):
    """Represent point in 2-D space"""
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __str__(self):
        return '{0}, {1}'.format(self.x, self.y)

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        if isinstance(other, tuple):
            # We get first and second items of tuple
            other_x = tuple[0]
            other_y = tuple[1]
            # Add the values to the self Point and return new point
            return Point(self.x + other_x, self.x + other_y)
