#!/usr/bin/env python
# encoding: utf-8
"""
exercise-10.9.py


Two words are reverse pair if each is the reverse of the other. Write a program that finds all reverse pairs in the word list.

Created by Terry Bates on 2012-11-25.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved."""

import sys
import os
import time

swampy_dir = "/Library/Python/2.7/site-packages/swampy-2.1.1-py2.7.egg/swampy/"


def reverse_word(word):
    word_list = []
    for letter in word:
        word_list.append(letter)
    word_list.reverse()
    return ''.join(word_list)

def bisect(search_term, my_list ):
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
        reversed_word = reverse_word(word)
        # try:
        #     if bisect(reversed_word, total_word_list):
        #         print 'word: ', word
        #         print 'reversed word: ', reversed_word
        # except:
        #     pass
        if bisect(reversed_word, total_word_list):
            print 'word: ', word
            print 'reversed word: ', reversed_word


if __name__ == '__main__':
    main()

