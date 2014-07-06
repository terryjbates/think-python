#!/usr/bin/env python
# encoding: utf-8
"""
exercise-16.1.py

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
    # Use join to quickly print out string colon separate
    print ':'.join([str(hour), str(minute), str(second)])
    
def main():
    my_time = Time()
    my_time.hour = 11
    my_time.minute = 59
    my_time.second = 30
    print_time(my_time)

if __name__ == '__main__':
    main()

