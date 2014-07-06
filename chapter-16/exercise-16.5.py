#!/usr/bin/env python
# encoding: utf-8
"""
exercise-16.5.py

Created by Terry Bates on 2014-07-05.
Copyright (c) 2014 http://the-awesome-python-blog.posterous.com. All rights reserved.
"""


import sys
import os
from copy import copy

class Time(object):
    """Represents the time of day.

        attributes: hour, minute, second
    """

def print_time(time_obj):
    hour, minute, second = time_obj.hour, time_obj.minute, time_obj.second
    # Use join to quickly print out string colon separated
    print ':'.join([str(hour).zfill(2), str(minute).zfill(2), str(second).zfill(2)])


def time_to_int(time_obj):
    # We create fractional portions of the "hour" attribute
    minutes = time_obj.hour * 60 + time_obj.minute 
    seconds = minutes * 60 + time_obj.second 
    return seconds


def int_to_time(seconds): 
    time = Time()
    minutes, time.second = divmod(seconds, 60) 
    time.hour, time.minute = divmod(minutes, 60) 
    return time


def is_after(time_obj_1, time_obj_2):
    # Return result from comparing via comput_scalar_time
    return time_to_int(time_obj_1) < time_to_int(time_obj_2)


        
def increment(time_obj, seconds):
    # Turn the time object into seconds
    time_obj_seconds = time_to_int(time_obj)
    ret_time_seconds = time_obj_seconds + seconds
    return int_to_time(ret_time_seconds)


def add_time(t1, t2):
    seconds = time_to_int(t1) + time_to_int(t2) 
    return int_to_time(seconds)


def main():
    t1 = Time()
    t1.hour = 12
    t1.minute = 59
    t1.second = 30

    t2 = Time()
    t2.hour = 11
    t2.minute = 59
    t2.second = 30    
    # Do comparison of two time objects, True if t1 occurs before t1, False otherwise
    print is_after(t1, t2)
    
    print "t1:Before increment"
    print_time(t1)
    print 
    print "Printing pure function increment value"
    print_time(increment(t1, 600))
    print
    print "t1:After increment"
    print_time(t1)


if __name__ == '__main__':
    main()
