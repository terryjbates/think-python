#!/usr/bin/env python
# encoding: utf-8
"""
exercise-8.5.py

Created by Terry Bates on 2012-09-05.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved."""

import sys
import os


def find(word,letter,start):
    if start:
        index = start
    else:
        index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1


def count(word, letter):
    count = 0
    index = 0
    while True:
        index = find(word,letter,index)
        # if the new index we have is -1 break loop
        if index == -1:
            return count
            break
        # Otherwise, continue processing
        # using index of found character as new start point
        else:
            count = count + 1
            index = index +1



if __name__ == '__main__':
    my_string = 'foo fighters rule'
    i = 0
    # for char in my_string:
    #     print "Char: %s  Index: %s" % (char, i)
    #     i = i +1
    print "Character  : Num. Times Found"
    print "----------|------------------"
    print "Found 'f' :", count(my_string, 'f')
    print "Found 'e' :", count(my_string, 'e')
    print "Found 'i' :", count(my_string, 'g')

