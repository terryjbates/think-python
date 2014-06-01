#!/usr/bin/env python
# encoding: utf-8
"""
exercise-14.3.py

Created by Terry Bates on 2014-02-04.
Copyright (c) 2014 http://the-awesome-python-blog.posterous.com. All rights reserved.
"""

import sys
import os
import collections
import argparse
import re
import collections


MP_PATTERN = ".mp(3|4)$"
MD5_CMD = '/sw/bin/md5sum'
# Create our globally available dictionary
music_dict = {}

def gen_md5sum(full_file_path):
    cmd = MD5_CMD + ' "' + full_file_path + '"'
    #print "cmd is ", cmd
    fp = os.popen(cmd)
    res = fp.read()
    stat = fp.read()
    return res

def check_for_mp_format(item):
    #print "item is ", item
    try:
        # Pattern match the file name for mp3 or mp4 files.
        # 'item' is a large data structure, representing a parent directory
        # containing a bunc of files contained within. 
        parent_dir = item[0]
        candidate_files = item[2]
        for cand_file in candidate_files:
            
            if re.search(".mp(3|4)$", cand_file):
                #print "Found mp(3|4) at ", item
                full_file_path = os.path.join(item[0], cand_file)
                #print "FULL PATH", full_file_path
                # We may have a full path, but may contain spaces
                # Use md5sum function 
                file_md5 = gen_md5sum(full_file_path)
                music_dict[file_md5] = full_file_path
                #print "Result for file %s is %s " % (full_file_path, 
                #    gen_md5sum(full_file_path))
                # Take results from the gen_md5sum function, insert into dictionary.
                # Use md5sum as the key, the filename as value and md5sum. 
                # If we were importing songs, the same md5sum would be equivalent
                # having the same "song" in our db
                
                #print "*" * 20
    except IndexError:
        pass


def recurse_dir(dir_name):
    # Create file list tuple based on specified directory
    file_list_tuple = os.walk(dir_name)
    # Call our check for mp format function on each item
    for item in file_list_tuple:
        check_for_mp_format(item)
        

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", help="The target directory of walk function")
    args = parser.parse_args()
    dir_name = args.dir
    recurse_dir(dir_name)
    print collections.OrderedDict(sorted(music_dict.items(), key=lambda t: t[0]))
if __name__ == '__main__':
    main()

