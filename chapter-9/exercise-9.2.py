#!/usr/bin/env python
# encoding: utf-8
"""
exercise-9.2.py

Program to print out entries in words.txt that have no 'e' character

Created by Terry Bates on 2012-09-15.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved."""

import swampy

# Neat trick learned from 
from os import path
#swampy_dir = path.join(path.dirname(__file__), 'swampy')
swampy_dir = "/Library/Python/2.7/site-packages/swampy-2.1.1-py2.7.egg/swampy/"

def has_no_e(line):
    if line.find('e') == -1:
        return True
    else:
        return False


def main():
    #create a variable called 'words_txt', make it have path of words.txt
    words_txt = swampy_dir + '/words.txt'
    print words_txt
    # open the file
    with_e = 0
    without_e = 0
    total_words = 0
    f = open(words_txt)
    # Do a loop, if the line is > 20 chars, print
    for line in f:
        line = line.strip()
        if has_no_e(line):
            without_e = without_e + 1
            # We can print this out, but too damned long for output
            #print line
        else:
            with_e = with_e +1 
        # We can increment as we go along
    # Or just do one add operation after the loop is complete
    total_words = with_e + without_e
    # Calculate percentage of words that have no e
    print "total: %s with_e: %s without_e: %s" % (total_words, with_e, without_e)
    print ""
    print "Percentage of words without e: ", (float(without_e) / float(total_words) ) * 100.0
if __name__ == '__main__':
	main()

