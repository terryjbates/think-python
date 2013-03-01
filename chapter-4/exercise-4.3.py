#!/usr/bin/env python
# encoding: utf-8
"""
exercise-4.3.py

Created by Terry Bates on 2012-07-16.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved."""


from swampy.TurtleWorld import *
import math
from polygon import circle, arc


def square(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)


def polyline(t, n, length, angle):
    """Draws n line segments.
    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        fd(t, length)
        lt(t, angle)


def polygon(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t, angle)


def polygon(t, n, length):
    angle = 360.0 / n
    # repeat for as many sides(n)
    polyline(t, n, length, angle)


def arc(t, r, angle):
    arc_length = (2 * math.pi * r) * (angle / 360)
    n = int(arc_length/3) + 1
    step_length = arc_length / n
    step_angle = float(angle)/n
    polyline(t, n, step_length, step_angle)


def circle(t, radius):
    arc(t, radius, 360)


def main():
    world = TurtleWorld()
    bob = Turtle()
    bob.delay = 0.005
    # square(bob,45)
    # square(bob,100)
    # square(bob,180)
    # polygon(bob,15,30)
    # square(bob,60)
    circle(bob, 60)
    #arc(bob,80,180)
    polyline
    wait_for_user()

if __name__ == '__main__':
    main()
