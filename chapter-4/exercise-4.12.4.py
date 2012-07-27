from swampy.TurtleWorld import *

from polygon import circle, arc

def post(t,n):
    pu(t)
    fd(t,n)
    pd(t)
    lt(t,90)
    fd(t,40)
    bk(t,40)
    rt(t,90)
    pu(t)
    bk(t,n)
    pd(t)

def beam(t,n):
    pu(t)
    lt(t,90)
    fd(t,n)
    rt(t,90)
    pd(t)
    fd(t,40)
    bk(t,40)
    rt(t,90)
    pu(t)
    fd(t,n)
    lt(t,90)
    pd(t)


def draw_h(t):
    post(t,0)
    beam(t,20)
    post(t,40)

def draw_e(t):
    post(t,0)
    n = 40
    while n >= 0:
        beam(t,n)
        n = n-20

def draw_l(t):
    post(t,0)
    beam(t,0)

def draw_o(t):
    fd(t,20)
    circle(t,20)
    pu(t)
    bk(t,20)
    pd(t)
if __name__ == '__main__':
    world = TurtleWorld()

    # create and position the turtle
    size = 20
    bob = Turtle()
    bob.delay = 0.05
    draw_h

    # for f in [draw_h(bob), draw_e(bob), draw_l(bob), draw_l(bob),draw_o(bob)]:
    #     f(bob, size)
    #     skip(bob, size)

    wait_for_user()
