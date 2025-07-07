#!/usr/bin/env python
# encoding: utf-8
"""
exercise-3.5.py

Create a script to draw a grid as shown on page 34 of textbook "Python for
Software Design"

Created by Terry Bates on 2012-07-15.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved.

Cut down on some lines
Ciprian Saramet on 2019-11-22

"""
def do_four(f):
    do_twice(f)
    do_twice(f)

def do_twice(f):
    f()
    f()

def print_beam():
    print('+ - - - -', end="")

def print_pillar():
    print('|        |        |', end="\n")

def tier():
    do_twice(print_beam)
    print('+')
    do_four(print_pillar)

def main():
    do_twice(tier)
    do_twice(print_beam)
    print('+')
if __name__ == '__main__':
    main()
