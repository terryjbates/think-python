#!/usr/bin/env python
# encoding: utf-8
"""
exercise-14.1.py

Created by Terry Bates on 2014-02-19.
Copyright (c) 2014 http://the-awesome-python-blog.posterous.com.
All rights reserved.
"""

import sys
import os
import argparse


def walk(dir):
    # Create a list to story names of discovered files
    list_of_names = []
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        if os.path.isfile(path):
            list_of_names.append(path)
        else:
            walk(path)
    return list_of_names


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", help="The target directory of walk function")
    args = parser.parse_args()
    dir_name = args.dir
    file_list = walk(dir_name)
    print file_list
if __name__ == '__main__':
    main()
