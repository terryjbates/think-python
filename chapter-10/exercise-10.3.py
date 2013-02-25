#!/usr/bin/env python
# encoding: utf-8
"""
exercise-10-3.py

Write a function called 'is_sorted'. List as parameter. Return 'True' if elements are sorted, 'False' otherwise. You can use "<,> operates"

Created by Terry Bates on 2012-11-19.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved."""


def is_sorted(my_list):
    index = 0 
    list_length = len(my_list)
    
    while index < list_length-1 :
        current = my_list[index]
        next = my_list[index+1]
        if next >= current:
            print "%s is bigger than %s" % (next, current)
            index += 1
        else: 
            return False
    return True

def main():
    test_list = [1, 2, 2, 3, 4]
    print is_sorted(test_list)
    bad_list = [4, 2, 2, 3, 4]
    print is_sorted(bad_list)

if __name__ == '__main__':
    main()

