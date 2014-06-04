#!/usr/bin/env python
# encoding: utf-8
"""
exercise-15.2.py

Created by Terry Bates on 2014-02-19.
Copyright (c) 2014 http://the-awesome-python-blog.posterous.com.
All rights reserved.
"""

import sys
import os
import math

class Point(object):
    """Represent point in 2-D space"""


class Rectangle(object):
    """Represents a rectangle.

    attributes: width, height, corner.
    """

def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2.0
    p.y = rect.corner.y + rect.height/2.0
    return p


def distance_between_points(p,q):
    y_diff = p.y - q.y
    x_diff = p.x = q.x
    y_sqr = math.pow(y_diff,2)
    x_sqr = math.pow(x_diff,2)
    x_y_sum = y_sqr + x_sqr
    return math.sqrt(x_y_sum)


def print_point(p):
    print '(%g, %g)' % (p.x, p.y)

def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy
    return rect

def main():
    # Create first Point object
    first = Point()
    first.x = 5
    first.y = 6
    # Create second Point object
    second = Point()
    second.x = 10
    second.y = 15
    
    print distance_between_points(first, second)
    
    # Create rectangle object
    my_rect = Rectangle()

    # Add a point as an attribute
    my_rect.corner = Point()
    my_rect.width = 10.0
    my_rect.height = 20.0

    # Create the Point's values
    my_rect.corner.x = 15
    my_rect.corner.y = 10
    print_point(my_rect.corner)

    # Move the rectangle around
    moved_rect = move_rectangle(my_rect, 5, 8)
    print_point(moved_rect.corner)


if __name__ == '__main__':
    main()
