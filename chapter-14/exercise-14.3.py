#!/usr/bin/env python
# encoding: utf-8
"""
exercise-14.3.py

Created by Terry Bates on 2014-02-04.
Copyright (c) 2014 http://the-awesome-python-blog.posterous.com. All rights reserved.
"""

import sys
import os
import collections

import cPickle

#word_list = "food doof ape pea pole lope".split()

word_list_file = open('../words_list', 'rb')
word_list = cPickle.load(word_list_file)

def main():
    total_words_dict = dict()
    for word in word_list:
        # Create a dictionary value
        word_dict = dict()
        for char in word:
            # Use setdefault method to create new key if need be, update current key
            word_dict[char] = word_dict.setdefault(char,0) + 1
        # Once we have word_dict populated, we must sort it, due to random acccess nature.
        # Use the 'collections' module because we are lazy.  http://docs.python.org/2/library/collections.html
        # Section 8.3.5
        sorted_word_dict = collections.OrderedDict(sorted(word_dict.items(), key=lambda t: t[0]))
        letter_count_t = tuple(sorted_word_dict.items())
        #print letter_count_t
        # Use letter_count_t as a dictionary key and append the current word as value
        total_words_dict.setdefault(letter_count_t,[]).append(word)
        
    # Pretty print the anagrams
    for anagram_list in total_words_dict.values():
        if len(anagram_list) > 1:
            print anagram_list
if __name__ == '__main__':
    main()

