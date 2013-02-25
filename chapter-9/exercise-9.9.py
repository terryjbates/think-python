#!/usr/bin/env python
# encoding: utf-8
"""
exercise-9.8.py


Write a program to test find when series of ages of two people seem to be 
palindromic:

Person A : 15  Person B : 51


Created by Terry Bates on 2012-10-01.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved."""

import sys
import os



def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2) - 1
    
    while j > 0:
        if word1[i] != word2[j]:
            return False
        i = i + 1
        j = j - 1
        
    return True
    
def is_palindrome(word):
    return is_reverse(word, word)
    
def reversed_age(age):
    if age < 10:
        age = str(age)
        age = age.zfill(2)
    else:
        age = str(age)
    age_length = len(age)
    #print "age is", age
    #print age_length
    rev_age = ''
    for i in age:
        rev_age = i + rev_age
    return rev_age
    #return reversed_age_value
    
def main():
    age_track_dict = {}
    age = rev_age = age_prev = rev_age_prev = 0

    for age in range (1, 100):

        
        rev_age = int(reversed_age(age))
        age = int(age)
        
        # calculate difference between the current loop values and previous
        age_diff = abs(age - rev_age)

        # If the differences between the ages are equidistant
        if age > rev_age and age_diff > 18 and age_diff < 60:
            print "age: %s\treversed age: %s\tage diff: %s" % (age, rev_age, age_diff)
            if not age_track_dict.has_key(age_diff):
                age_track_dict[age_diff] = 1
            else:
                age_track_dict[age_diff] = age_track_dict[age_diff]  + 1 
#print "age_prev: %s rev_age_prev %s " % (age_prev, rev_age_prev)
            print
        
        age_prev = age
        rev_age_prev = rev_age        
        
    print age_track_dict
    
if __name__ == '__main__':
	main()