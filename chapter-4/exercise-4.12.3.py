#!/usr/bin/env python


"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *

from polygon import *
import math


def draw_slice(t, r, slice_angle):
    """Draws a slice.

    t: Turtle
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    # so the sine is equal to the opposite/hypotenuse
    # hypotenuse is r
    # sin(c) = o/h
    # c = (360/n) / 2 or half the angle of "entire" slice
    half_edge = math.sin(slice_angle/2) * r
    edge = 2 * half_edge
    turn_angle = abs(180 - (slice_angle/2) - 90)
    fd(t, r)
    lt(t, turn_angle)
    fd(t, edge)
    lt(t, turn_angle)
    fd(t, r)


def pie(t, s, r):
    """Draws a pie with n petals.

    t: Turtle
    s: number of slices
    r: radius of the arcs
    """
    slice_angle = 360.0 / s
    draw_slice(t, r, slice_angle)
    #lt(t, slice_angle )


def move(t, length):
    """Move Turtle (t) forward (length) units without leaving a trail.
    Leaves the pen down.
    """
    pu(t)
    fd(t, length)
    pd(t)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

# draw a sequence of three pies, as shown in the book.
move(bob, -100)
pie(bob, 5, 10.0)
die(bob)
# dump the contents of the campus to the file canvas.eps
world.canvas.dump()
wait_for_user()
