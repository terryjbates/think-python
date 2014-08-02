#!/usr/bin/env python
# encoding: utf-8
"""
exercise-17.5.py

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
            other_x = other[0]
            other_y = other[1]
            # Add the values to the self Point and return new point
            return Point(self.x + other_x, self.x + other_y)


def main():
    p1 = Point(5, 3)
    p2 = Point(-2, 8)
    point_tuple = (3, 5)

    print "Result of p1 + p2", p1 + p2
    print "Result of p1 + point tuple", p1 + point_tuple

if __name__ == "__main__":
    main()