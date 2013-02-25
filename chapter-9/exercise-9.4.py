#!/usr/bin/env python
# encoding: utf-8
"""
exercise-9.4.py

Write program with a function that will accept user-entered list of required letters and a word, and return True if the word doesn't use only the required letters, and False if it does.

Created by Terry Bates on 2012-09-16.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved."""

import swampy

# Neat trick learned from 
from os import path
#swampy_dir = path.join(path.dirname(__file__), 'swampy')
swampy_dir = "/Library/Python/2.7/site-packages/swampy-2.1.1-py2.7.egg/swampy/"


def uses_only(word, uses_only_list):
    # iterate over the letters in word
    for letter in word:
        # we want to be case insensitive.
        letter = letter.lower()
        if letter not in uses_only_list and letter != " ":
            print "Letter %s  is not in %s " % (letter, uses_only_list)
            return False
    return True

    
    
def letters_list():
    my_string = raw_input("Please enter a list of letters to use only: ").strip()
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
    use_only_string = letters_list()
    print
    print "You wish to use only: ", use_only_string
    print
    print uses_only(my_word, use_only_string)
    
    # Now, we try running through words.txt with the avoid list
    #create a variable called 'words_txt', make it have path of words.txt
    words_txt = swampy_dir + '/words.txt'
    # # open a filehandle
    f = open(words_txt)
    # # Excluding the least == Including the most
    # for line in f:
    #     line = line.strip()
    #     if uses_only( line, use_only_string ):
    #         print "line : %s only uses %s" % (line, use_only_string)
            
        
if __name__ == '__main__':
    main()

