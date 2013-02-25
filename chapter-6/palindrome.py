#!/usr/bin/env python
# encoding: utf-8
"""
palindrome.py

AKA exercise-6.6. 


Created by Terry Bates on 2012-08-15.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved."""

import sys
import os


def first(word):
    return word[0]
    
def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_odd_char(word):
    if len(word) % 2 == 1:
        return True
    else:
        return False
    
def first_equals_last(a):
    if first(a) == last (a):
        return True
    else:
        return False
    

def is_palindrome(word):    
    # base case is 3 character word
    if not first_equals_last(word) or not is_odd_char(word):
        return False
    else:
        if len(word) > 3:
            word = middle(word)
            return is_palindrome(word)
        elif len(word) == 3:
            return True
        else:
            return False
    # First Attempt:        
    # if first_equals_last(word) and len(word) > 3:
    #     print word + ": in if"
    #     word = middle(word)
    #     return is_palindrome(word)
    # elif first_equals_last(word) and len(word) == 3:
    #     print word + ": in elif"
    #     return True
    # else:
    #     print word + ": in else"
    #     return False
    # 
if __name__ == '__main__':
    print 'bob ' + str(is_palindrome('bob'))
    print 'terry ' + str(is_palindrome('terry'))
    print 'coraroc ' + str(is_palindrome('coraroc'))