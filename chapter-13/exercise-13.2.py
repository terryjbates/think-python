#!/usr/bin/env python
# encoding: utf-8
"""
exercise-13.2.py

Script to read in Gutenburg books, count up total amount of words and the amount of time each word was used. 


Created by Terry Bates on 2012-07-13.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import argparse
import re
import string
import collections
import cPickle


# Neat idea. Rather than using a list and "in" to see if word is valid
# Create a dictionary with each value being = to a ceremonial value.
# Access to the dictionary appears to be random access, versus being 
# serially looked up as a list appears to be. This also has side-effect
# of actually ensuring only valid words are counted after stripping of 
# punctuation.

word_list_dict_file = open('/Users/tbates/python/Think-Python/think-python/words_dict', 'rb')
word_list_dict = cPickle.load(word_list_dict_file)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source_file", help="The text file containing the source and target urls")
    args = parser.parse_args()
    filename = args.source_file
    f = open(args.source_file,'r')
    # Create dictionary to store word-specific counts
    book_word_dict = dict()
    # Store total word count
    total_word_count = 0
    # Use for loop in order to process each line.
    # Remove all punctuation
    for line in f:
        for char in string.punctuation:
            line = line.replace(char,'')
        # After line is stripped of punctuation, count member words
        #print line.lower().strip()
        # We make all words lowercase, strip whitespace, split on spaces
        # All in one fell swoop.
        for word in line.lower().strip().split():
            try: 
                # See if the word is in our word list dictionary.
                if word_list_dict[word]:
                    book_word_dict[word] = book_word_dict.setdefault(word,0) + 1
                    total_word_count += 1
            except:
                pass
    # Generate a sorted directory
    sorted_word_dict =  collections.OrderedDict(sorted(book_word_dict.items(), reverse=True, key=lambda t: t[1]))
    # Print out sorted directory, keys and values
    for key in sorted_word_dict:
        pass
        #print "%s : %s" % (key, sorted_word_dict[key])

    #print book_word_dict
    print "Total word count", total_word_count
    print "Number of unique words", len(sorted_word_dict)

if __name__ == '__main__':
    main()