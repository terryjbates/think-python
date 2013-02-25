#!/usr/bin/env python
# encoding: utf-8
"""
exercise-10.4.py

Write a function 'is_anagram' that takes two strings and returns true if they are anagrams

Created by Terry Bates on 2012-11-19.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved."""

import sys
import os

def is_anagram(first_string, second_string):
    # Create lists from the strings passed in as params
    first_list  = list(first_string)
    second_list = list(second_string)

    # Sort the lists. These are mutable, so list contents will be altered.
    first_list.sort()
    second_list.sort()
    if first_list == second_list:
        return True
    else:
        return False

def main():
    string_a ='foobar'
    string_b ='roobfa'
    print is_anagram(string_a, string_b)
    
if __name__ == '__main__':
    main()

