#!/usr/bin/env python
# encoding: utf-8
"""
exercise-12.2.py

Modify book's code example to tie-break between words of equal length using the "random" module

Created by Terry Bates on 2013-01-29.
Copyright (c) 2013 http://the-awesome-python-blog.posterous.com. All rights reserved.
"""
import cPickle
import random


def sort_by_length(words):
    list_of_words = []
    for word in words:
        # (length_of_word, random_number, word)
        list_of_words.append((len(word), random.random(), word))
    
    list_of_words.sort(reverse=True)
    
    res = []
    for length, random_value, word in list_of_words:
        res.append(word)
    return res
    
def main():
    # read in our word list from pickled object
    word_list_file = open('/Users/tbates/python/Think-Python/think-python/words_list', 'rb')
    words = cPickle.load(word_list_file)
    long_to_short_words = sort_by_length(words)
    for word in long_to_short_words:
        print word

if __name__ == '__main__':
	main()

