#!/usr/bin/env python
# encoding: utf-8
"""
exercise-11.6.py

Created by Terry Bates on 2013-01-08.
Copyright (c) 2013 http://the-awesome-python-blog.posterous.com. All rights reserved.
"""

import sys
import os
import time

known = {0:0, 1:1}

def fibonacci_slow(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_slow(n-1) + fibonacci_slow(n-2)


def fibonacci_fast(n):
    if n in known:
        return known[n]
        
    res = fibonacci_fast(n-1) + fibonacci_fast(n-2)
    known[n] = res
    return res
    
def main():

    time_start = time.time()
    print fibonacci_slow(20)
    time_end = time.time()
    print "Time for slow fibonacci to complete ", time_end - time_start

    time_start = time.time()
    print fibonacci_fast(20)
    time_end = time.time()
    print "Time for fast fibonacci to complete ", time_end - time_start



if __name__ == '__main__':
	main()

