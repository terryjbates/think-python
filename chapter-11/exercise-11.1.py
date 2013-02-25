#!/usr/bin/env python
# encoding: utf-8
"""
exercise-11.1.py

Create a dictionary made of words from the swampy module. Make words the keys, the values can be anything. 

Created by Terry Bates on 2012-10-31.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved."""
import random
import time

swampy_dir = "/Library/Python/2.7/site-packages/swampy-2.1.1-py2.7.egg/swampy/"


def main():
    #create a variable called 'words_txt', make it have path of words.txt
    words_txt = swampy_dir + '/words.txt'

    # # open a filehandle
    f = open(words_txt)
    # create an empty word list
    total_word_dict = {}
    
    for word in f:
        total_word_dict[word.strip()] = random.randint(0,100)

    time_start = time.time()
    if 'lollipop' in total_word_dict:
        print total_word_dict['lollipop']
    time_end = time.time()
    print "time diff is ", time_end - time_start
    # print total_word_dict['full']

if __name__ == '__main__':
    main()
