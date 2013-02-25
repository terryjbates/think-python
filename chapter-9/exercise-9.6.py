#!/usr/bin/env python
# encoding: utf-8
"""
exercise-9.6.py

Write program with a function that will implement 'is_abecedarian' function. Return True if the letters appear in alphabetical order, and False if they do not.

Created by Terry Bates on 2012-09-16.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved.
We found 596 abecedarian words.
"""

swampy_dir = "/Library/Python/2.7/site-packages/swampy-2.1.1-py2.7.egg/swampy/"

def is_abecedarian(word):
    # iterate over the letters in word
    previous_letter = ''
    for letter in word:
        # we want to be case insensitive.
        letter = letter.lower()
        if letter  < previous_letter:
            #print "Letter %s  is not in %s " % (required_letter, uses_all_list)
            return False
        previous_letter = letter
    #print "We found the letters required in ", word
    return True


def main():

    # Now, we try running through words.txt with the avoid list
    #create a variable called 'words_txt', make it have path of words.txt
    words_txt = swampy_dir + '/words.txt'
    # # open a filehandle
    f = open(words_txt)
    abecedarian_count = 0
    # # Excluding the least == Including the most
    for line in f:
        line = line.strip()
        if is_abecedarian(line):
            #print "line : %s only uses %s" % (line, uses_all_string)
            abecedarian_count = abecedarian_count + 1
            #print line
    print abecedarian_count
if __name__ == '__main__':
    main()

