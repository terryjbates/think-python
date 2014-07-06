#!/usr/bin/env python

import string
import cPickle

def process_line(line, h):
    # We iterate over the string.punctuation string. This allows us to avoid
    # multiple occurences of an unwanted character.

    for char in string.punctuation:
        line = line.replace(char,' ')

    for word in line.split():
        # Strip the word of punctuation and whitespace all in one swoop
        
        word = word.strip(string.punctuation + string.whitespace)
        # Get the current value and increment. If non-existent, set 
        # the initial value to 0, then increment. This generalizes nicely.
        h[word] = h.get(word, 0) + 1


def process_file(filename):
    # Create a histogram dictionary to count word frequencies
    h = dict()
    # Open the file for reading
    fp = open(filename, 'r')
    # For each line in the file, process the line
    for line in fp:
        # Process the line and provide the histogram dictionary
        process_line(line, h)
    return h


def total_words(h):
    # h.values returns a sequence containing the frequencies of the words
    # stored in the histogram dictionary. We use 'sum' to return the sum
    # of the values in the sequence. So, if a sequence is [1,3 , 4]
    # then 'sum' should return 8.
    return sum(h.values())


def different_words(h):
    # The length of the dictionary is equal to the number of keys
    return len(h)


if __name__ == "__main__":
    # Generate a histogram based on the contents of "Swann's Way"
    hist = process_file('pg7178.txt')
    print "Total amount of words is ", total_words(hist)
    print "Total amount of unique words is ", different_words(hist)

    # Read in our word list via its Cpickle file
    word_list_dict_file = open('/Users/tbates/python/Think-Python/think-python/words_dict', 'rb')
    word_list_dict = cPickle.load(word_list_dict_file)        


    # Now that we have our two dictionaries, we can do set subtraction to see
    # what words do not occur within the dictionary.
    hist_set = set(hist)
    word_list_set = set(word_list_dict)
    
    difference_set =  hist_set - word_list_set 
    print "Total amount of words not found in dictionary: ", different_words(difference_set)
    #print difference_set









