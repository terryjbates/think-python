
#!/usr/bin/env python
# encoding: utf-8
"""
exercise-16.7.py

Created by Terry Bates on 2014-07-06.
Copyright (c) 2014 http://the-awesome-python-blog.posterous.com. All rights reserved.
"""

import sys
import os
import datetime

FORMAT_STRING = "Year: {}\tMonth: {}\tWeekDay: {}"

# Create a dict that maps numerical days onto human readable
weekday_dict = {
    1:'Monday',   
    2:'Tuesday',
    3:'Wednesday',
    4:'Thursday',
    5:'Friday',
    6:'Saturday',
    7:'Sunday',
}


def get_weekday():
    today_date = datetime.date.today()
    return today_date.isoweekday()

def main():
    num_weekday = get_weekday()
    print weekday_dict[num_weekday]


if __name__ == '__main__':
    main()

