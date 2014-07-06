#!/usr/bin/env python
# encoding: utf-8
"""
exercise-16.2.py

Created by Terry Bates on 2014-07-05.
Copyright (c) 2014 http://the-awesome-python-blog.posterous.com. All rights reserved.
"""

import sys
import os


class Time(object):
    """Represents the time of day.

        attributes: hour, minute, second
    """


def compute_scalar_time(time_obj):
    # We create fractional portions of the "hour" attribute
    return time_obj.hour + (time_obj.minute / 60) + (time_obj.second / 3600)


def is_after(time_obj_1, time_obj_2):
    # Get attribute info from objects.
    hour_1, minute_1, second_1 = time_obj_1.hour, time_obj_1.minute, time_obj_1.second
    hour_2, minute_2, second_2 = time_obj_2.hour, time_obj_2.minute, time_obj_2.second
    # Return result from comparing via comput_scalar_time
    return compute_scalar_time(time_obj_1) < compute_scalar_time(time_obj_2)


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

if __name__ == '__main__':
    main()
