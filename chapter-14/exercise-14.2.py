#!/usr/bin/env python
# encoding: utf-8
"""
exercise-14.2.py

Created by Terry Bates on 2014-02-19.
Copyright (c) 2014 http://the-awesome-python-blog.posterous.com.
All rights reserved.
"""

import os
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", help="The target directory of walk function")
    args = parser.parse_args()
    dir_name = args.dir
    file_list_tuple = os.walk(dir_name)
    for item in file_list_tuple:
        print item


if __name__ == '__main__':
    main() 
