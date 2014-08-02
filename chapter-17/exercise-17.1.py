#!/usr/bin/env python
# encoding: utf-8
"""
exercise-17.1.py

Created by Terry Bates on 2014-07-05.
Copyright (c) 2014 http://the-awesome-python-blog.posterous.com. All rights reserved.
"""


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
        """

        :rtype : object
        """
        self_seconds = self.time_to_int()
        ret_time_seconds = self_seconds + seconds
        return self.int_to_time(ret_time_seconds)

    def is_after(self, other):
        # Return result from comparing via compute_scalar_time
        return self.time_to_int() < other.time_to_int()

    def __add__(self, other):
        if isinstance(other, Time):
            return self.increment(other.time_to_int())
        else:
            return self.increment(other)

    @staticmethod
    def int_to_time(seconds):
        time = Time()
        minutes, time.second = divmod(seconds, 60)
        time.hour, time.minute = divmod(minutes, 60)
        return time


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


if __name__ == '__main__':
    main()
