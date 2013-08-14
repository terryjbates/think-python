#!/usr/bin/env python
# encoding: utf-8
"""
exercise-13.9.py

Created by Terry Bates on 2013-08-13.
Copyright (c) 2013 http://the-awesome-python-blog.posterous.com. All rights reserved.
"""

import sys
import os
import argparse
import string
import re
import math

def print_points_to_file(points_list):
    try:
        output_file = open('/tmp/ex-13.tsv', 'w')
    except:
        print "Cannot open output file"
        sys.exit()

    for word, x, y in points_list:
        x += 1
        y += 1
        x = math.log10(x)
        y = math.log10(y)
        
        print >> output_file, "%s\t%s\t%s" % (word, x, y)
    output_file.close()

def calc_y_val(count_word_tuple, mod=1):
    # Get each portion of tuple
    freq, word = count_word_tuple
    # Calculate modified y value, and divide by our modulus if needed
    y_val = float(freq/mod)
    return (word,y_val)


def sort_word_dict(word_dict):
    '''Return a sorted list of (word,count) tuples.'''
    # Created a list
    sort_l = []
    # Use list comprehension to quickly transpose the (word,count) tuples into
    # (count, word) tuples.
    for k,v in word_dict.items():
        sort_l.append((v,k))
    # Sort the list in-place, it will use the count as the initial sort key.
    sort_l.sort(reverse=True)
    # Return our sorted list.
    return sort_l


def strip_word_punc(word):
    return word.translate(string.maketrans("",""), string.punctuation)


def gen_rank(input_file):
    '''Generate Zipf details given a specified input file.'''
    word_count_d = dict()
    try:
        # Open our input file
        with open (input_file, 'r')  as file_of_words:
            # Process each line of words
            for line in file_of_words:
                # Take each line and split into a list of words
                words_in_line = line.strip().split()
                # For each word in the list...
                for word in words_in_line:
                    # Strip word of punctuation
                    word = strip_word_punc(word)
                    # See if key already exists, if not set to 0.
                    # In either case, increment the value by 1.
                    word_count_d[word] = word_count_d.get(word, 0) + 1
                    # print word
                    # print word_count_d[word]
                    #print "word: %s word_count_d[word]" % (word, word_count_d[word])
    except:
        print "Problem accessing file"
        sys.exit(1)
    
    # Generate a list of words with associated counts
    word_count_l = sort_word_dict(word_count_d)

    # Create a list to store the word frequencies as points in cartesian 
    # coordinate system.
    word_freq_points = []

    # Use enumerate to calculate X and Y values easily
    for x, count_word_t in enumerate(word_count_l):
        (word, y) = calc_y_val(count_word_t)
        word_freq_points.append((word, x, y))

    # Print out our X, Y values
    # for word, x,y in word_freq_points:
    #     print "%s x:%s y:%s" % (word, x, y)

    # Estimate equation valuse using first and last elements
    first_point = word_freq_points[0]
    second_point = word_freq_points[1]
    third_point = word_freq_points[1]    
    last_point =  word_freq_points[-1]
    
    b = first_point[2]
    m = -float(first_point[2]/last_point[1])
    
    # Figure out sum of all words
    total_word_count = sum([y for word, x, y in word_freq_points])
    print "Total word count", total_word_count
    
    # Print out the slope and y intercept
    print "first_point: %s last point: %s" % (first_point, last_point)
    print "first_point percentage: %s " % ((first_point[2] / total_word_count) * 100)
    print "second_point percentage: %s " % ((second_point[2] / total_word_count) * 100)
    print "third_point percentage: %s " % ((third_point[2] / total_word_count) * 100)

    print "slope: %s y-intercept: %s" % (m, b) 
    
    print_points_to_file(word_freq_points)

if __name__ == '__main__':
    # Create argparse object
    parser = argparse.ArgumentParser()
    # Add 'filename' argument
    parser.add_argument("filename")
    # Put the arguments into a variable
    args = parser.parse_args()
    
    # If specified argument is not a file, exit program
    if not os.path.isfile(args.filename):
        print "%s is not a valid file" % args.filename
    else:
        gen_rank(args.filename)

