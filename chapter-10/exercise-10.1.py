#!/usr/bin/env python
# encoding: utf-8
"""
exercise-10.1.py

Create a function that will take a list [1,2,3]
and return a list such that i = i-1 + 1 so:
[1,2,3] --> [1, 3, 6]
Created by Terry Bates on 2012-10-31.
Copyright (c) 2012 http://the-awesome-python-blog.posterous.com.
All rights reserved."""

def cum_sum(start_list):
    my_sum = 0
    sum_list = []
    for i in range(len(start_list)):
        my_sum += start_list[i]
        # print my_sum
        # the original idea of sum_list[i] = my_sum *does not work*
        sum_list.append(my_sum)
    return sum_list

def main():
    start_list = [1,2,3]
    print cum_sum(start_list)

if __name__ == '__main__':
	main()

