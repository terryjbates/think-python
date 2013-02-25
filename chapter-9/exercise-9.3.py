#!/usr/bin/env python
# encoding: utf-8
"""
exercise-9.3.py

Write program with a function that will accept user-entered list of forbidden letters and a word, and return True if the word doesn't use any of forbidden letters, and False if it does.

Created by Terry Bates on 2012-09-16.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved."""

import swampy

# Neat trick learned from 
from os import path
#swampy_dir = path.join(path.dirname(__file__), 'swampy')
swampy_dir = "/Library/Python/2.7/site-packages/swampy-2.1.1-py2.7.egg/swampy/"


def avoids(word, avoid_list):
    # iterate over the letters in word
    for char in word:
        if char in avoid_list:
            # if the word has a char in avoid_list, return False
            return False
    # Otherwise, return true, since it "avoids"        
    return True


    
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
    
    # Now, we try running through words.txt with the avoid list
    #create a variable called 'words_txt', make it have path of words.txt
    words_txt = swampy_dir + '/words.txt'
    # open a filehandle
    f = open(words_txt)
    # Excluding the least == Including the most
    avoided = 0
    non_avoided = 0
    
    for line in f:
        line = line.strip()        
        # use avoids with our previously set list_to_avoid
        if avoids(line, list_to_avoid):
            avoided = avoided + 1
        else:
            non_avoided = non_avoided + 1
    total = avoided + non_avoided

    # Suspicion that the sequence that excludes the least is 
    # vwxqz
    print "Percentage avoided: ",  (float(avoided) / total) * 100
        
if __name__ == '__main__':
    main()

