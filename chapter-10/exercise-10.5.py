#!/usr/bin/env python
# encoding: utf-8
"""
exercise-10.5.py

Birthday Paradox program. If there are 23 students in a class, what is the probability that any two of them share the same birthday

Created by Terry Bates on 2012-11-20.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com. All rights reserved.
"""

import random

def has_duplicates(input_list):
    '''For each item in the list see if there is a duplicate.'''
    # create empty dictionary to store key/value pairs
    check_duplicate_dict = {}
    for item in input_list:
        if check_duplicate_dict.has_key(item):
            print "dup item is: ", item
            return True
        else:
            check_duplicate_dict[item] = 1
                
    return False

def main():
    # We will be running 100 times, so start our count
    # of instances where a sample has duplicates to 0
    dup_count = 0 
    for i in range(1,100):
        # Create a list to store 23 birthdays, using random module
        my_bday_list = []
        # Populate the birthday list
        for i in range(23):
            # We use assume "birthday" is measured from
            # first to last day in the year sequentially.
            my_bday_list.append(random.randint(1,365))

        # See if the list has duplicates
        if has_duplicates(my_bday_list):
            print my_bday_list
            # Increment our count of samples that have duplicates
            dup_count += 1
        print
    # Print the discovered probability
    print "Probability of having duplicates in a sample of 23 students", dup_count/100.0        

if __name__ == '__main__':
    main()

