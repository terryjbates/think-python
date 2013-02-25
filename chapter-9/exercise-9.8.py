#!/usr/bin/env python
# encoding: utf-8
"""
exercise-9.8.py


Write a program to test all the 6 digit numbers and prints any numbers that are
palindromic. 



odometer_string: 199999 odometer_number + 1: 200000 odometer_number + 2 200001
odometer_string: 299999 odometer_number + 1: 300000 odometer_number + 2 300001
** odometer_string: 399999 odometer_number + 1: 400000 odometer_number + 2 400001
odometer_string: 499999 odometer_number + 1: 500000 odometer_number + 2 500001
odometer_string: 599999 odometer_number + 1: 600000 odometer_number + 2 600001
odometer_string: 699999 odometer_number + 1: 700000 odometer_number + 2 700001
odometer_string: 799999 odometer_number + 1: 800000 odometer_number + 2 800001
odometer_string: 899999 odometer_number + 1: 900000 odometer_number + 2 900001



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
    
    
def main():
	
    # go through all six digit numbers
    for odometer_number in range(100000,999999):
    #for odometer_number in range(123454,123858):
        
        # convert the number into a string
        odometer_string = str(odometer_number)

        # palindromes must be in combos
        # of 3, 4, 5, 6

        if is_palindrome(odometer_string[2:6]) and is_palindrome(str(odometer_number + 1)[1:6]) and is_palindrome(str(odometer_number + 2)[1:4]):
            print "odometer_string: %s odometer_number + 1: %s odometer_number + 2 %s" % (odometer_string, odometer_number + 1, odometer_number + 2)





if __name__ == '__main__':
	main()

