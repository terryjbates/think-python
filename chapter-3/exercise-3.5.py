#!/usr/bin/env python
# encoding: utf-8
"""
exercise-3.5.py

Create a script to draw a grid as shown on page 34 of textbook "Python for
Software Design"

Created by Terry Bates on 2012-07-15.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved."""


def print_twice(my_string):
    print my_string
    print my_string


def do_twice(f):
    f()
    f()


def do_four(f):
    do_twice(f)
    do_twice(f)


def print_beam():
    print '+ - - - -',


def print_post():
    print'|        ',


def print_beams():
    do_twice(print_beam)
    print '+'


def print_posts():
    do_twice(print_post)
    print '|'


def print_row():
    print_beams()
    do_four(print_posts)


def print_grid():
    do_twice(print_row)


def main():
    print_grid()
    print_beams()


if __name__ == '__main__':
    main()
