#!/usr/bin/env python

"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

import sys
import string
import random


class Markov(object):

    def __init__(self, order=2, n=100):

        # Data structures to capture data
        self.suffix_map = {}
        self.prefix = ()

        # Order of words captured for prefix
        self.order = int(order)
        # Number of random words to generate
        self.n = int(n)

    def process_word(self, word):
        """Processes each word.

        word: string
        order: integer

        During the first few iterations, all we do is store up the words;
        after that we start adding entries to the dictionary.
        """
        #print "processing word", word

        if len(self.prefix) < self.order:
            self.prefix += (word,)
            print "self.prefix: ", self.prefix
            return

        try:
            #print "we append %s word to %s self.prefix" % (word, self.prefix)
            self.suffix_map[self.prefix].append(word)
        except KeyError:
            # if there is no entry for this self.prefix, make one
            self.suffix_map[self.prefix] = [word]

        self.prefix = shift(self.prefix, word)

    def random_text(self):
        """Generates random wordsfrom the analyzed text.

        Starts with a random prefix from the dictionary.

        self.n: number of words to generate
        """
        # choose a random prefix (not weighted by frequency)
        start = random.choice(self.suffix_map.keys())

        for i in range(self.n):
            suffixes = self.suffix_map.get(start, None)
            if suffixes == None:
                # if the start isn't in map, we got to the end of the
                # original text, so we have to start again.
                self.n = self.n - 1
                self.random_text()
                return

            # choose a random suffix
            word = random.choice(suffixes)
            print word,
            start = shift(start, word)


def process_file(filename, markov_obj):
    """Reads a file and performs Markov analysis.

    filename: string
    order: integer number of words in the prefix

    Returns: map from prefix to list of possible suffixes.
    """
    print "Entered process_file"
    fp = open(filename)
    #print "Skipping gutenburg header"
    #skip_gutenberg_header(fp)
    #print "Skipped gutenburg header"
    for line in fp:
        #print "line is", line
        for word in line.rstrip().split():
            markov_obj.process_word(word)


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*END*THE SMALL PRINT!'):
            break


def shift(t, word):
    """Forms a new tuple by removing the head and adding word to the tail.

    t: tuple of strings
    word: string

    Returns: tuple of strings
    """
    return t[1:] + (word,)


def main(name, filename='', n=100, order=2, *args):
    print "Filename is ", filename
    print "n is", n

    try:
        n = int(n)
        order = int(order)
    except:
        print 'Usage: randomtext.py filename [# of words] [prefix length]'
    else:
        markov_obj = Markov(order, n)
        print "Processing file"
        process_file(filename, markov_obj)
        print "We have suffix map of length", len(markov_obj.suffix_map)
        print "Using random text with %s", markov_obj.n
        markov_obj.random_text()


if __name__ == '__main__':
    main(*sys.argv)
