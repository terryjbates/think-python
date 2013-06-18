#!/usr/bin/env python
# encoding: utf-8
"""
exercise-13.1.py

Script to read file, break line into words, strip whitespace and punctuation
from the words, convert to lowercase.


Created by Terry Bates on 2012-07-13.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import argparse
import re
import string

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source_file", help="The text file containing the source and target urls")
    args = parser.parse_args()
    filename = args.source_file
    f = open(args.source_file,'r')
    
    for line in f:
        for char in string.punctuation:
            line = line.replace(char,'')
        print line.lower().strip()

if __name__ == '__main__':
    main()