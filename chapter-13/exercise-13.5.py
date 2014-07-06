#!/usr/bin/env python
# encoding: utf-8
"""
exercise-13.5.py

Write a function called 'choose_from_int' that takes a histogram as defined in
section 11.1, returns a random value from the histogram, chosen with 
probability in proportion to frequency.

Created by Terry Bates on 2012-10-31.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com. 
All rights reserved.
"""
import random
import collections

MAX_TESTS = 10000

def choose_from_hist(hist):
    list_of_vals = list()
    for key in hist:
        # Capture the timse a char occurs
        value = hist[key]
        # As many times as the value indicates, append the key
        # to the list.
        for index in range(value):
           list_of_vals.append(key)
           
    # Now that we have a list of values, we must randomly choose one of them
    # Pick a random integer, between 0 and the length of the result.
    # This is to deal with zero-indexing of lists
    choice_int = random.randint(0, len(list_of_vals) - 1 )
    # Obtain the value in the list at the given random number index
    return random.choice(list_of_vals[choice_int])

        
def histogram(s):
    d = dict()
    for c in s:
        dict_value = d.get(c,0)
        d[c] = dict_value + 1 
    return d

def main():
    # Create a dictionary to store random test results
    result_dict = dict()

    # Create a test historgram
    test_hist = histogram('aab')
    print test_hist
    # Repeat the operation a large number times, see if it aligns with 
    # percentage a char appears. 
    for index in range(MAX_TESTS):
        chosen_value = choose_from_hist(test_hist)
        # We use set default to either add or modify current dictionary value
        result_dict[chosen_value] = result_dict.setdefault(chosen_value,0) + 1
        # We sort the dictionary using the 'collections' module
        sorted_result_dict =  collections.OrderedDict(sorted(result_dict.items(), reverse=True, key=lambda t: t[1]))
    # Print our results, the char, and percentage of times encountered.
    for key, value in sorted_result_dict.items():
           print "%s: %s" % (key, (float(value)/MAX_TESTS) * 100)

if __name__ =='__main__':
    main()
