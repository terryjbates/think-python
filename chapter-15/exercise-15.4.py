#!/usr/bin/env python
# encoding: utf-8
"""
exercise-15.4.py

Created by Terry Bates on 2014-02-19.
Copyright (c) 2014 http://the-awesome-python-blog.posterous.com.
All rights reserved.
"""

import sys
import os
from swampy.World import World



class Point(object):
    """Represent point in 2-D space"""


class Rectangle(object):
    """Represents a rectangle.

    attributes: width, height, corner.
    """

def create_canvas(world, w, h, my_background):
    my_canvas = world.ca(width=w, height=h, background=my_background)
    return my_canvas
    
#def draw_rectangle(canvas, rectangle):
    # 
def create_rectangle(height, width, color):
    my_rect = Rectangle()
    my_rect.width = height
    my_rect.height = width
    my_rect.corner = Point()
    my_rect.corner.x = 0.0
    my_rect.corner.y = 0.0
    my_rect.color = color
    return my_rect
    
    
def bbox(rectangle):
    """Return a list of lists, with individual lists containing coordinates."""
    # The rectangle object has an embedded "corner" 
    p1 = [rectangle.corner.x, rectangle.corner.y]
    
    # Use the height and width
    p2 = [rectangle.corner.x + rectangle.width, rectangle.corner.y + rectangle.height]
    
    # Return our binding box, a list of lists
    return [p1, p2]
    
def draw_rectangle(canvas, rectangle):
    # To draw on our canvas, we need to figure out the two points that make up
    # the "binding box." We have one, since the rectangle has a corner, we must
    # figure out the other point
    my_bbox = bbox(rectangle)
    
    # Now that we have the bbox, we must draw on the canvas
    canvas.rectangle(my_bbox, outline='black', width=2, fill=rectangle.color)

def main():
    # Create World object
    #print  sys.version_info
    world = World()
    # Create our canvas
    canvas = create_canvas(world, 500, 500, 'white')
    #canvas = world.ca(width=500, height=500, background='white')
    # Create our rectangle
    my_rect = create_rectangle(100, 200, 'blue')

    # Now that we have both our rectangle and our canvas, we must
    # draw a rectangle
    draw_rectangle(canvas, my_rect)
    
    #bbox = [[-150,-100], [150, 100]]
    #canvas.rectangle(bbox, outline='black', width=2, fill='green4')
    world.mainloop()


if __name__ == '__main__':
    main()

