#!/usr/bin/env python
# encoding: utf-8
"""
exercise-9.7.py

Write program with a function that will find a word with three consecutive letters.


Created by Terry Bates on 2012-09-16.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved.

Son of a gun:

bookkeeper
bookkeepers
bookkeeping
bookkeepings

"""

swampy_dir = "/Library/Python/2.7/site-packages/swampy-2.1.1-py2.7.egg/swampy/"

def three_double_letters(word):
    # we must recall the previous letter we looked at
    previous_letter = ''
    # initialize pair count
    pair_count = previous_pair_index = current_pair_index = 0 
    index = 0 
    for letter in word:
        # we want to be case insensitive.
        letter = letter.lower()
        previous_pair_index = current_pair_index
        if letter == previous_letter:
            # set this up, if we have no pairs, no problem
            # Once we have found a pair, set the current_pair_index
            current_pair_index = index

            # If the difference between the current_pair_index and previous_pair_index is greater han one, don't increment our pair count
            if current_pair_index - previous_pair_index == 2:
                # increment our count of pairs
                pair_count = pair_count + 1 
        previous_letter = letter
        index = index + 1
    if pair_count == 3:
        #print "We found the letters required in ", word
        return True
    return False

def main():

    # Now, we try running through words.txt with the avoid list
    #create a variable called 'words_txt', make it have path of words.txt
    words_txt = swampy_dir + '/words.txt'
    # # open a filehandle
    f = open(words_txt)
    triple_double_count = 0
    # # Excluding the least == Including the most
    for line in f:
        line = line.strip()
        if three_double_letters(line):
            #print "line : %s only uses %s" % (line, uses_all_string)
            triple_double_count = triple_double_count + 1
            print line
    print triple_double_count
if __name__ == '__main__':
    main()

