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

def koch(t, length):
    if length < 3 :
        fd(t, length)
        return
    koch(t, length / 3)
    lt(t, 60)
    koch(t, length / 3 )
    rt(t, 120)
    koch(t, length / 3)
    lt(t, 60)
    koch(t, length / 3 )
    
if __name__ == '__main__':
    world = TurtleWorld()    
    bob = Turtle()
    bob.delay = 0.001
    koch(bob, 1000)
    wait_for_user()
