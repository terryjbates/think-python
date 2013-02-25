#!/usr/bin/env python
# encoding: utf-8
"""
exercise-9.1.py

Program to read in the swampy module's 'words.txt' and only print words that are greater than 20 chars.

Created by Terry Bates on 2012-09-15.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved."""

import swampy

# Neat trick learned from 
from os import path
#swampy_dir = path.join(path.dirname(__file__), 'swampy')
swampy_dir = "/Library/Python/2.7/site-packages/swampy-2.1.1-py2.7.egg/swampy/"


def main():
    #create a variable called 'words_txt', make it have path of words.txt
    words_txt = swampy_dir + '/words.txt'
    print words_txt
    # open the file
    f = open(words_txt)
    # Do a loop, if the line is > 20 chars, print
    for line in f:
        if len(line) > 20:
            # we strip the line, or else it will print the trailing '\r\n'
            print line.strip()
            
    
if __name__ == '__main__':
	main()

