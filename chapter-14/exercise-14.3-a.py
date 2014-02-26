#!/usr/bin/env python

import os
import sys
import cPickle
import anydbm
import anagram_sets


def store_anagrams(d):
    # Create the database
    db = anydbm.open('anagram_shelf','c')
    # Iterate over the dictionary items
    for key, value  in d.items():
        #print "key: %s value:%s" % (key, value)
        # If the anagram is not single character
        if len(value) > 1:
            db[key] = cPickle.dumps(value)
    return db

def read_anagrams(db, search_term):
    # Compute the search_term signature
    search_term_sig = anagram_sets.signature(search_term)
    pickled_search_result = db[search_term_sig]
    return cPickle.loads(pickled_search_result)

def main():
   # First, create your dictionary of anagrams
    d = anagram_sets.all_anagrams('../words.txt')
    # Create our anagram shelf
    anagram_shelf = store_anagrams(d)
    # Test and see if "less" properly returns anagrams
    print read_anagrams(anagram_shelf, 'less')
    # Test and see if "foal" properly returns anagrams
    print read_anagrams(anagram_shelf, 'foal')



if __name__ == '__main__':
    main()
