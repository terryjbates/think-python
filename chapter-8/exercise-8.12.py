#!/usr/bin/env python
# encoding: utf-8
"""
exercise-8.12.py

Created by Terry Bates on 2012-09-08.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com. All rights reserved.
"""

import sys
import os

def rotate_word(word, rotate_num):
    # a = 97, z = 122, A = 65, Z = 90
    new_word = ''
    index = 0
    for char in word:
        # Get the ordinal value
        my_ord = ord(char)
        print "original ord value" , my_ord        
        # Add the rotation to ordinal value
        # If this is negative, that is OK
        # since adding a negative number = subtraction
        my_ord = my_ord + rotate_num
        print "new ord value" , my_ord
        #print chr(my_ord)
        if my_ord > 90 and my_ord < 97 :
            my_ord = my_ord + 7
        elif my_ord > 122:
            my_ord = my_ord - 57
        elif my_ord < 65:
            my_ord = my_ord + 57
        print "ord value after if/elif" , my_ord        
        my_char = chr(my_ord)
        print "old char: %s | new char: %s \n" % (char.encode(),my_char.encode())
        new_word = new_word + my_char
        index = index + 1    
    return new_word

if __name__ == '__main__':
    print rotate_word('banana', 13)
    print rotate_word("In the elevators, the extrovert looks at the OTHER guy's shoes.", 13)
