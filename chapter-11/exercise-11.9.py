#!/usr/bin/env python
# encoding: utf-8
"""
exercise-11.9py



Created by Terry Bates on 2013-01-16.
Copyright (c) 2013 http://the-awesome-python-blog.posterous.com. All rights reserved.
"""

import cPickle

# Load our stored list of every word in the swampy file
pickle_file = '/Users/tbates/python/Think-Python/think-python/words_list'
word_list_file = open(pickle_file,'rb')
word_list = cPickle.load(word_list_file)
rot_pairs_dict = dict()


def rotate_word(word, rotate_num):
    # a = 97, z = 122, A = 65, Z = 90
    new_word = ''
    base_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxy"
    lookup_table = ''
    
    # Cut off the rotation number
    # assume this is a positive number for now
    rotate_portion = base_table[:rotate_num]
    
    # Run through the chars in base_table
    # Append to the end of lookup_table
    for char in base_table[rotate_num:]:
        # populate the lookup_table, starting at the rotated number
        lookup_table = lookup_table + char
    # ...then append rotated portion to the tail end    
    lookup_table = lookup_table + rotate_portion
    for char in word:
        # if it is alphanumeric
        if char.isalnum():
            # Find the first instance of the char in the base_table
            index = base_table.find(char,1)
            # then lookup up this index in the lookup_table
            new_word = new_word + lookup_table[index]
        # else, keep the character as it is.
        else:
            new_word = new_word + char
    return new_word

    
def bisect(search_term, my_list):
    lo = 0
    hi = len(my_list)
    while lo < hi:
        #print "hi: %s lo: %s" % (hi, lo)
        mid = (lo+hi)//2
        if search_term == my_list[mid]:
            return mid - 1 
        elif search_term < my_list[mid]: 
            hi = mid
        else: 
            lo = mid+1        
    return None


def main():
    # For every word in the list, check it
    for word in word_list:
        # Get the rotated word
        rotated_word = rotate_word(word, 13)
        if bisect(rotated_word, word_list):
            rot_pairs_dict[word] = rotated_word
    for key in rot_pairs_dict:
        print "%s:%s" % (key, rot_pairs_dict[key])
if __name__ == '__main__':
	main()

