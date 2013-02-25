#!/usr/bin/env python
# encoding: utf-8
"""
exercise-9.5.py

Write program with a function that will accept user-entered list of required letters and a word, and return True if the word uses all of the , and False if it does not.

Created by Terry Bates on 2012-09-16.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved.
We found 598 words with 'aeiou' and 42 with 'aeiouy'
"""

import swampy

# Neat trick learned from 
from os import path
#swampy_dir = path.join(path.dirname(__file__), 'swampy')
swampy_dir = "/Library/Python/2.7/site-packages/swampy-2.1.1-py2.7.egg/swampy/"


def uses_all(word, uses_all_list):
    # iterate over the letters in word
    for required_letter in uses_all_list:
        # we want to be case insensitive.
        required_letter = required_letter.lower()
        if required_letter not in word and required_letter != " ":
            #print "Letter %s  is not in %s " % (required_letter, uses_all_list)
            return False
    #print "We found the letters required in ", word
    return True

    
    
def letters_list():
    my_string = raw_input("Please enter a list of letters to use : ").strip()
    # Create an empty list
    letters_list = []

    # Run through the string we are given
    for char in my_string:
        letters_list.append(char)
    return letters_list

def main():
    print
    my_word = raw_input("Please enter the word of your choice: ").strip()
    print
    print "my word is: ", my_word
    print
    uses_all_string = letters_list()
    print
    print "You wish to use : ", uses_all_string
    print
    print uses_all(my_word, uses_all_string)
    
    # Now, we try running through words.txt with the avoid list
    #create a variable called 'words_txt', make it have path of words.txt
    words_txt = swampy_dir + '/words.txt'
    # # open a filehandle
    f = open(words_txt)
    uses_all_count = 0
    # # Excluding the least == Including the most
    for line in f:
        line = line.strip()
        if uses_all( line, uses_all_string ):
            #print "line : %s only uses %s" % (line, uses_all_string)
            uses_all_count = uses_all_count + 1
    print uses_all_count
if __name__ == '__main__':
    main()

