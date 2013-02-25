#!/usr/bin/env python
# encoding: utf-8
"""
exercise-10-2.py

Write a function function called "chop" that takes a list and modifies it, removing the first and last elements, and returns "None."

Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

Created by Terry Bates on 2012-11-19.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved."""

def chop(list_to_chop):
    # remove the leading element
    del list_to_chop[0]
    # remove trailing element
    del list_to_chop[-1]
    

def middle(list_to_middle):
    # call the chop function
    chop(list_to_middle)
    # list are passed by reference
    return list_to_middle

def main():
    my_list = "a b c d".split()
    middle(my_list)
    print my_list

if __name__ == '__main__':
    main()

