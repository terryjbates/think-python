#!/usr/bin/env python
# encoding: utf-8
"""
exercise-15.1.py

Created by Terry Bates on 2014-02-19.
Copyright (c) 2014 http://the-awesome-python-blog.posterous.com.
All rights reserved.
"""

import sys
import os
import math

class Point(object):
    """Represent point in 2-D space"""

def distance_between_points(p,q):
    y_diff = p.y - q.y
    x_diff = p.x = q.x
    y_sqr = math.pow(y_diff,2)
    x_sqr = math.pow(x_diff,2)
    x_y_sum = y_sqr + x_sqr
    return math.sqrt(x_y_sum)


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

    
if __name__ == '__main__':
    main()
