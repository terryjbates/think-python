#!/usr/bin/env python
# encoding: utf-8
"""
exercise-7.5.py

Created by Terry Bates on 2012-08-30.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved."""

import math


def estimate_pi():
    coefficient = 2 * math.sqrt(2) / 9801
    k = 0
    total = 0
    while True:
        den = math.factorial(k)**4.0 * (394.0**(4.0*k))
        num = math.factorial(4.0*k) * (1103.0 + (26390.0*k))
        interim_sum =  coefficient * (num/den) 
        total = total + interim_sum
        if abs(interim_sum) < 1e-15:
            break
        k = k + 1
    return 1 / total


if __name__ == '__main__':
    print estimate_pi()

