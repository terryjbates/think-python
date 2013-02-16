#!/usr/bin/env python
# encoding: utf-8
"""
word-dict-load.py

Script to create a word dictionary based on the word list. Use for faster lookups of valid words.
"""
import cPickle

# Open our original word list, for reading
word_list_file = open('/Users/tbates/python/Think-Python/think-python/words_list', 'rb')
word_list = cPickle.load(word_list_file)

# Open file descriptor for word dict, for writing
word_list_dict_file = open('/Users/tbates/python/Think-Python/think-python/words_dict', 'wb')

# Generate stupid dictionary with "key:value" --> "word:1"
word_list_dict = dict()
for word in word_list:
    word_list_dict[word] = 1

# Dump the structure to disk.
cPickle.dump(word_list_dict, word_list_dict_file)