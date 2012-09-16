#!/usr/bin/env python
# encoding: utf-8
"""
exercise-9.3.py

Write program with a function that will accept user-entered list of forbidden letters and a word, and return True if the word doesn't use any of forbidden letters, and False if it does.

Created by Terry Bates on 2012-09-16.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com. All rights reserved.
"""

import sys
import os

def avoids(word, avoid_list):
    # iterate over the letters in word
    for char in word:
        if char in avoid_list:
            return False
    return True

    # if you find a letter in word, that is in our list to avoid
    # return False immediately
    # if you made it through word unscathed
    # return true
    
def chars_to_avoid():
    my_string = raw_input("Please enter a list of letters to avoid: ").strip()
    # Create an empty list
    chars_to_avoid = []

    # Run through the string we are given
    for char in my_string:
        # If the char is not in our list append it
        if char not in chars_to_avoid:
            chars_to_avoid.append(char)
    return chars_to_avoid

def main():
    my_word = raw_input("Please enter the word of your choice: ").strip()
    print "my word is ", my_word
    list_to_avoid = chars_to_avoid()
    print "You wish to avoid", list_to_avoid
    print avoids(my_word, list_to_avoid)
if __name__ == '__main__':
    main()

