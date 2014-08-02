#!/usr/bin/env python
# encoding: utf-8
"""
exercise-17.7.py

Created by Terry Bates on 2014-07-05.
Copyright (c) 2014 http://the-awesome-python-blog.posterous.com. All rights reserved.
"""


class Kangaroo(object):
    """Represents the time of day.

        attributes: hour, minute, second
    """
    def __init__(self, contents=None):
        if contents == None:
            contents = []
        self.pouch = contents

    def put_in_pouch(self, item):
        self.pouch.append(item)

    def __str__(self):
        output_string = []
        for item in self.pouch:
            output_string.append(item)
        return str(output_string)

def main():
    print "Creating 'kanga' as Kangaroo object"
    kanga = Kangaroo()
    kanga.put_in_pouch('foo')
    print kanga

    print "Creating 'roo' as Kangaroo object"
    roo = Kangaroo()
    print "Putting 'roo' into 'kanga's pouch"
    kanga.put_in_pouch(roo)

    print "Printing 'kanga'"
    print kanga

if __name__ == "__main__":
    main()
