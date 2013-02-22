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

# Declare global total word count.
total_word_count = 0

def count_word(word, complete_word_set, book_word_dict, unknown_word_dict):
    global total_word_count
    
    # If we are using a dictionary
    if str(type(complete_word_set)) == "<type 'dict'>":
        try: 
            # See if the word is in our word list dictionary.
            if complete_word_set[word]:
                book_word_dict[word] = book_word_dict.setdefault(word,0) + 1
                total_word_count += 1
        except:
            unknown_word_dict[word] = unknown_word_dict.setdefault(word,0) + 1
            #pass        
    # If we are using a list.
    elif str(type(complete_word_set)) == "<type 'list'>":
        # Use 'in' to see if word is present in valid word list
        if word in complete_word_set:
            book_word_dict[word] = book_word_dict.setdefault(word,0) + 1
            total_word_count += 1

def main():
    # Create argparse object
    parser = argparse.ArgumentParser()
    # Use a positional argument
    parser.add_argument("source_file", help="The text file containing the source and target urls.")
    parser.add_argument("data_struct", help="Select 'list' or 'dict to use in checking for words.")
    parser.add_argument("-c","--count", help="Print out specified number of most frequently used words", type=int)
    # Obtain our positional arguments
    args = parser.parse_args()
    # Set the filename to first positional argument.
    filename = args.source_file
    # Set the data structure type to second positional argument
    data_struct = args.data_struct
    
    # First ensure that we are not picking an unspecified data structure.
    # If we choose a list or dict, we then set 'complete_word_set' accordingly.
    if data_struct not in ['list','dict']:
        print "Unknown data structure '%s': please use 'dict' or 'list'" % data_struct
        exit()
    elif data_struct == 'list':
        word_list_file = open('/Users/tbates/python/Think-Python/think-python/words_list', 'rb')
        complete_word_set = cPickle.load(word_list_file)        
    elif data_struct == 'dict':
        word_list_dict_file = open('/Users/tbates/python/Think-Python/think-python/words_dict', 'rb')
        complete_word_set = cPickle.load(word_list_dict_file)        

    # Open a file handle for the filename passed as argument
    f = open(args.source_file,'r')
    # Create dictionary to store word-specific counts
    book_word_dict = dict()
    unknown_word_dict = dict()
    # We use for loop in order to process each line.
    # Since 'string.punctuation' is literally a string,
    # We use a loop to replace any matching characters with nothing.
    for line in f:
        for char in string.punctuation:
            line = line.replace(char,'')
        # After line is stripped of punctuation, count member words
        # we make all words lowercase, strip whitespace, split on spaces
        # all in one fell swoop.
        for word in line.lower().strip().split():
            count_word(word, complete_word_set, book_word_dict, unknown_word_dict)
            
    # Generate a sorted directory via 'collections' module
    # Sort it based on the count values, and reverse it,
    # so that the largest counts appear first.
    sorted_word_dict =  collections.OrderedDict(sorted(book_word_dict.items(), reverse=True, key=lambda t: t[1]))
    sorted_unknown_word_dict =  collections.OrderedDict(sorted(unknown_word_dict.items(), reverse=True, key=lambda t: t[1]))

    if args.count:
        count = 0
        # Print out sorted directory, keys and values
        for key, value in sorted_word_dict.items():
            if count < args.count:
                #print "%s: %s" % (key,value)
                count += 1

        for key, value in sorted_unknown_word_dict.items():
            if count < args.count:
                print "%s: %s" % (key,value)
                count += 1
        
    # Output our total word count, and unique word count.
    print "Total word count", total_word_count
    print "Number of unique words", len(sorted_word_dict)

if __name__ == '__main__':
    main()