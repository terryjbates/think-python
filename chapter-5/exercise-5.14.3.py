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


# Suspect this will draw some sort of geometric shape
# Initially thought it might be a spiral, but unclear how/when
# recursion will hit and enable this to turn right then left

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    fd(t, length*n)
    lt(t, angle)
    draw(t, length, n-1)
    rt(t, 2*angle)
    draw(t, length, n-1)
    lt(t, angle)
    bk(t, length*n)
    
if __name__ == '__main__':
    world = TurtleWorld()    
    bob = Turtle()
    bob.delay = 0.001
    draw(bob, 10, 5)
    wait_for_user()
