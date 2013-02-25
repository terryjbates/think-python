#!/usr/bin/env python
# encoding: utf-8
"""
exercise-8.9.py

Created by Terry Bates on 2012-09-08.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved."""

def is_palindrome(word):
    # if word == word[::-1]:
    #     return True
    # else:
    #     return False
    return word == word[::-1]

        
if __name__ == '__main__':
    print is_palindrome('bob')
    print is_palindrome('alpapla')
    print is_palindrome('shlomo')