#!/usr/bin/env python
# encoding: utf-8
"""
exercise-16.4.py

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
    if int(second) < 10:
        second = '0' + str(second)

    if int(minute) < 10:
        minute = '0' + str(minute)

    print ':'.join([str(hour), str(minute), str(second)])


def compute_scalar_time(time_obj):
    # We create fractional portions of the "hour" attribute
    return time_obj.hour + (time_obj.minute / 60) + (time_obj.second / 3600)


def is_after(time_obj_1, time_obj_2):
    # Get attribute info from objects.
    hour_1, minute_1, second_1 = time_obj_1.hour, time_obj_1.minute, time_obj_1.second
    hour_2, minute_2, second_2 = time_obj_2.hour, time_obj_2.minute, time_obj_2.second
    # Return result from comparing via comput_scalar_time
    return compute_scalar_time(time_obj_1) < compute_scalar_time(time_obj_2)


def increment(time_obj, seconds):
    ret_time_obj = Time()
    # Copy data from the time_obj to our ret_time_obj
    ret_time_obj = copy(time_obj)
    
    ret_time_obj.second += seconds
    if ret_time_obj.second >= 60: 
        added_min, remaining_sec = divmod(ret_time_obj.second, 60)
        ret_time_obj.second = remaining_sec
        ret_time_obj.minute += added_min
    if ret_time_obj.minute >= 60:
        added_hour, remaining_min = divmod(ret_time_obj.minute, 60)
        ret_time_obj.minute = remaining_min
        ret_time_obj.hour += added_hour
    return ret_time_obj

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
    #print is_after(t1, t2)
    
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
