#!/usr/bin/env python
# encoding: utf-8
"""
exercise-10.6.py

Write a function called 'remove_duplicates.' Take a list and return a new list with only the unique elements from the original. (Not necessarily in same order).

Created by Terry Bates on 2012-11-25.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com. All rights reserved.
"""

import sys
import os

def remove_duplicates(input_list):
    '''For each item in the list see if there is a duplicate.'''
    # create empty dictionary to store key/value pairs
    check_duplicate_dict = {}
    dups_removed_list = []
    for item in input_list:
        if check_duplicate_dict.has_key(item):
            pass
            #print "dup item is: ", item
            #return True
        else:
            check_duplicate_dict[item] = 1
            dups_removed_list.append(item)    
    return dups_removed_list

    

def main():
    list_1 = [1, 2, 3]
    list_2 = [1, 1, 2, 3]
    print "original list_1", list_1
    print "original list_2", list_2
    print
    print "dup removed list 1:", remove_duplicates(list_1)    
    print "dup removed list 2:", remove_duplicates(list_2)

if __name__ == '__main__':
    main()

