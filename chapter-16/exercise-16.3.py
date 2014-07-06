#!/usr/bin/env python
# encoding: utf-8
"""
exercise-16.3.py

Created by Terry Bates on 2014-07-05.
Copyright (c) 2014 http://the-awesome-python-blog.posterous.com. All rights reserved.
"""

import sys
import os


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


def increment(time, seconds): 
    time.second += seconds
    if time.second >= 60: 
        added_min, remaining_sec = divmod(time.second, 60)
        time.second = remaining_sec
        time.minute += added_min
    if time.minute >= 60:
        added_hour, remaining_min = divmod(time.minute, 60)
        time.minute = remaining_min
        time.hour += added_hour
    

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
    
    print "t1:Before"
    print_time(t1)
    increment(t1, 600)
    print "t1:After"
    print_time(t1)


if __name__ == '__main__':
    main()
