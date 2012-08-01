#!/usr/bin/env python
# encoding: utf-8
"""
exercise-5.14.1.py

Created by Terry Bates on 2012-08-01.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com. All rights reserved.
"""

import sys
import os


def prompt_user():
    '''Prompt the user to input the required values
    for Fermat's last theorem
    a^n + b^n = c^n
    Use a for loop to avoid repeated prompts
    '''
    # create general prompt
    prompt = "Please enter " 
    
    for value in ['a', 'b', 'c', 'n']:
        new_prompt = prompt + value + '\n' # modify prompt for value in loop
        my_input = raw_input(new_prompt)   # get input
        float_input = float(my_input)      # convert the entered value to float
        exec ("%s=%f" % (value, float_input))

def check_fermat():
    prompt_user()
    
def main():
    check_fermat()


if __name__ == '__main__':
	main()

