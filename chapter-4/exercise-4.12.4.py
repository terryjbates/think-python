#!/usr/bin/env python

from swampy.TurtleWorld import *
from polygon import circle, arc


def post(t, n):
    """Define a 'post' as a vertical line with a variable position.
    Use the parameter to function to determine its offset position
    from flush left."""
    pu(t)
    fd(t, n)
    pd(t)
    lt(t, 90)
    fd(t, 40)
    bk(t, 40)
    rt(t, 90)
    pu(t)
    bk(t, n)
    pd(t)


def beam(t, n):
    """Define a 'beam' as a horizontal line with a variable position.
    Use the parameter to function to determine its offset position
    from flush bottom."""
    pu(t)
    lt(t, 90)
    fd(t, n)
    rt(t, 90)
    pd(t)
    fd(t, 40)
    bk(t, 40)
    rt(t, 90)
    pu(t)
    fd(t, n)
    lt(t, 90)
    pd(t)


def draw_h(t):
    """Function to draw a 't' character. """
    post(t, 0)
    beam(t, 20)
    post(t, 40)


def draw_e(t):
    """Function to draw a 'e' character. """
    post(t, 0)
    n = 40
    while n >= 0:
        beam(t, n)
        n = n-20


def draw_l(t):
    """Function to draw a 'l' character. """
    post(t, 0)
    beam(t, 0)


def draw_o(t):
    """Function to draw a 'o' character. """
    fd(t, 20)
    circle(t, 20)
    pu(t)
    bk(t, 20)
    pd(t)


if __name__ == '__main__':
    world = TurtleWorld()
    # create and position the turtle
    size = 20
    bob = Turtle()
    bob.delay = 0.05
    draw_h
    wait_for_user()
