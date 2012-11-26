#!/usr/bin/env python
# encoding: utf-8
"""
exercise-10.8.py


Binary search function

Created by Terry Bates on 2012-11-25.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com. All rights reserved.
"""

import sys
import os

def bisect(search_term, my_list ):
    
    # Shamelessly stolen from bisect.py
    lo = 0
    hi = len(my_list)
    while lo < hi:
        print "hi: %s lo: %s" % (hi, lo)
        mid = (lo+hi)//2
        if search_term == my_list[mid]:
            return mid - 1 
        elif search_term < my_list[mid]: 
            hi = mid
        else: 
            lo = mid+1
        
    return None



def main():
    test_list = "abba bobby crooklyn david edward franklin giovanni".split()
    print bisect('foo', test_list)

if __name__ == '__main__':
    main()

