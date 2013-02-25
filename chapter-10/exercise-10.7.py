#!/usr/bin/env python
# encoding: utf-8
"""
exercise-10.7.py

Created by Terry Bates on 2012-11-25.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved."""

import sys
import os

swampy_dir = "/Library/Python/2.7/site-packages/swampy-2.1.1-py2.7.egg/swampy/"

def append_word_to_list(my_list, file_handle, method):

    if method == 'append':
        for line in file_handle:
            line = line.strip()
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
    
    append_word_to_list(total_word_list, f, 'new_list')
    print total_word_list

if __name__ == '__main__':
    main()

