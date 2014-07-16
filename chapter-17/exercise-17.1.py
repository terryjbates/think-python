#!/usr/bin/env python
# encoding: utf-8
"""
exercise-17.1.py

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
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second


    def __str__(self):
        # Use join to quickly print out string colon separated
        return ':'.join([str(self.hour).zfill(2), str(self.minute).zfill(2), str(self.second).zfill(2)])


    def time_to_int(self):
        # We create fractional portions of the "hour" attribute
        minutes = self.hour * 60 + self.minute 
        seconds = minutes * 60 + self.second 
        return seconds


    def increment(self, seconds):
        # Turn the time object into seconds
        self_seconds = self.time_to_int()
        ret_time_seconds = self_seconds + seconds
        return int_to_time(ret_time_seconds)


    def is_after(self, other):
        # Return result from comparing via comput_scalar_time
        return self.time_to_int() < other.time_to_int()

def int_to_time(seconds): 
    time = Time()
    minutes, time.second = divmod(seconds, 60) 
    time.hour, time.minute = divmod(minutes, 60) 
    return time





        



def add_time(t1, t2):
    seconds = time_to_int(t1) + time_to_int(t2) 
    return int_to_time(seconds)


def mul_time(time_obj, number):
    ret_time = Time()
    ret_time_sec = int_to_time(ret_time_sec)
    product = number / ret_time_sec
    return int_to_time(product)

def time_per_mile(time_obj, distance):
    # We have a time object, make it into a large integer
    time_obj_int = Time.time_to_int(time_obj)
    # Once we have a large number, we then divide this by distance
    sec_per_mile = time_obj_int / distance
    # This gives us a second/mile pace, convert to a Time object
    return int_to_time(sec_per_mile)



def main():
    # Initialize Time objects
    t1 = Time(12, 59, 30)
    t2 = Time(11, 59, 30)

  
    # Do comparison of two time objects, True if t1 occurs before t1, False otherwise
    print t1.is_after(t2)
    
    print "t1:Before increment"
    print t1
    print 
    print "Printing pure function increment value"
    t1.increment(600)
    print
    print "t1:After increment"
    print t1
    print "Time / distance foolishness"
    t3 = Time(5, 13, 30)
    distance = 5
    print (time_per_mile(t3, distance))


if __name__ == '__main__':
    main()
