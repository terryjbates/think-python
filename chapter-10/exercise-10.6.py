#!/usr/bin/env python
# encoding: utf-8
"""
exercise-10.6.py

Write a function called 'remove_duplicates.' Takes a list and returns a new list with only the unique elements from the original 

Created by Terry Bates on 2012-11-20.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved."""

import random

def remove_duplicates(input_list):
    '''For each item in the list see if there is a duplicate.'''
    # create empty dictionary to store key/value pairs
    unique_item_dict = {}
    removed_duplicates_list = []
    for item in input_list:
        # if already existing, pass
        if unique_item_dict.has_key(item):
            pass
        # otherwise, add to dict
        else:
            unique_item_dict[item] = 1

    # create new list based on dict key values
    for dict_item in unique_item_dict.iterkeys():
        removed_duplicates_list.append(dict_item)

    return removed_duplicates_list


def main():
    # We will be running 100 times, so start our count
    # of instances where a sample has duplicates to 0
    dup_list = "first second first first third".split()
    new_list = remove_duplicates(dup_list)
    print "%s %s" % (dup_list, new_list)

if __name__ == '__main__':
    main()

