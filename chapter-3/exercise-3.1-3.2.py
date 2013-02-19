#!/usr/bin/env python
# encoding: utf-8
"""
exercise-3.1-3.2.py

Created by Terry Bates on 2012-07-14.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved.
"""

import sys
import os
#NameError: "name 'repeat_lyrics' is not defined"
#repeat_lyrics()


def repeat_lyrics():
    print_lyrics()
    print_lyrics


def print_lyrics():
    print "I am a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."


def print_twice(bruce):
    print bruce
    print bruce
    cat(bruce)


def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)

repeat_lyrics()
