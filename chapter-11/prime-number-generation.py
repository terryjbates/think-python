#!/usr/bin/env python
# encoding: utf-8
"""
prime-number-generation.py

Created by Terry Bates on 2013-01-11.
Copyright (c) 2013 http://the-awesome-python-blog.posterous.com. All rights reserved.
"""

import sys
import os

def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}  

    # The running integer that's checked for primeness
    q = 2  

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            # 
            yield q        
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1

primes = gen_primes()




def main():
    x = set()
    y = 0
    a = gen_primes()
    while y < 10000:
      x |= set([a.next()])
      y+=1

    print sorted(x)

if __name__ == '__main__':
    main()

