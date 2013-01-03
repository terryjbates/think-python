#!/usr/bin/env python
# encoding: utf-8
"""
exercise-10.10.py

Created by Terry Bates on 2013-01-03.
Copyright (c) 2013 http://the-awesome-python-blog.posterous.com. All rights reserved.
"""

import sys
import os
import time

swampy_dir = "/Library/Python/2.7/site-packages/swampy-2.1.1-py2.7.egg/swampy/"

def bisect(search_term, my_list):
    # Shamelessly stolen from bisect.py
    lo = 0
    hi = len(my_list)
    while lo < hi:
        #print "hi: %s lo: %s" % (hi, lo)
        mid = (lo+hi)//2
        if search_term == my_list[mid]:
            return mid - 1 
        elif search_term < my_list[mid]: 
            hi = mid
        else: 
            lo = mid+1
        
    return None

def append_word_to_list(my_list, file_handle, method):
    if method == 'append':
        for line in file_handle:
            line = line.strip()
            # 'appending',line
            my_list.append(line)     
    elif method == 'new_list':
        for line in file_handle:
            line = line.strip()
            my_list = my_list + [line]

def is_even_num(number):
    if number % 2 == 0 or number == 0:
        return True
    else:
        return False


def shuffle_word(plain_word, search_word):
    # Get two lists from the words we are given
    plain_word_list = list(plain_word)
    search_word_list = list(search_word)
    shuffle_word_list = []
    # Make the words into list, then get all even or odd list members
    index = 0
    while True:
        # If odd, append corresponding element from first word
        if is_even_num(index):
            shuffle_word_list.append(plain_word_list[index])

        # Otherwise, append the 'even' element from the other list    
        else:
            shuffle_word_list.append(search_word_list[index])

        # Increment the index    
        index += 1   
    # Print out the garbage we have created.    
    print ''.join(shuffle_word_list)
    return ''.join(shuffle_word_list)

def interlock(word, total_word_list):
    for search_word in total_word_list:
        new_word = shuffle_word(word, search_word)
        
    if bisect(new_word, total_word_list):
        print new_word

  
def main():
    #create a variable called 'words_txt', make it have path of words.txt
    words_txt = swampy_dir + '/words.txt'
    # # open a filehandle
    f = open(words_txt)
    # create an empty word list
    total_word_list = []
    
    append_word_to_list(total_word_list, f, 'append')
    #print total_word_list
    for word in total_word_list:    
        interlock(word, total_word_list)
    
    
if __name__ == '__main__':
    main()

