#!/usr/bin/env python
# encoding: utf-8
"""
exercise-17.4.py

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
        return self.x + other.x, self.y + other.y


p1 = Point(5, 3)
p2 = Point(-3, 4)

print p1 + p2