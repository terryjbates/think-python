#!/usr/bin/env python
import string

import sys 
reload(sys) 
sys.setdefaultencoding("utf-8")

def process_line(line, h, order):
    # Strip out all '-'
    line = line.replace('-', ' ')
    prev_word = str()
    current_word = str()
    word_list = []

    word_tuple = tuple()
    first_word = str()
    second_word = str()
    third_word = str()
    
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace) 
        word = word.lower()
        # Append the word to the word list
        word_list.append(word)
        print "word list", word_list        
        # If the length of the word list is equal to order plus one
        if len(word_list) == order + 1:
            # Create a tuple. We will need this for an immutabale
            # data structure to use as dictionary key.
            
            # Obtain first and second word from
            first_word = word_list[0]
            second_word = word_list[1]
            third_word = word_list[2]
            # We have a tuple to use for our dict key
            word_tuple = (first_word, second_word)
            print "tuple is ", word_tuple
            # See if the dictionary has a value, based on the key
            # that is a list. If not, create a dummy list
            if type(h.get(word_tuple)) != "<type 'str'>":
                # Set this to an empty list
                h[word_tuple] = []
                # Append the third word to the value pointed to by the tuple
                h[word_tuple].append(third_word) 
            # Pop the earliest entry off the word_list
            word_list.pop(0)                
        #h[word] = h.get(word, 0) + 1
    # Append current word to our word_list
    print "word list", word_list





def process_file(filename, order): 
    h = dict()
    fp = open(filename) 
    for line in fp:
        process_line(line, h, order) 
    return h


def total_words(h): 
    return sum(h.values())


def different_words(h): 
    return len(h)


def most_common(h, num=10): 
    t = []
    for key, value in h.items(): 
        t.append((value, key))
        t.sort(reverse=True) 
    return t


def print_most_common(hist, num=10):
    t = most_common(hist)
    print 'The most common words are:' 
    for freq, word in t[0:num]:
        print word, '\t', freq


def random_word(h):
    t=[]
    for word, freq in h.items():
        t.extend([word] * freq)
    return random.choice(t)


if __name__ == "__main__":
    order = 2
    hist = process_file('pg7178.txt', order)
    print 'Total number of words:', total_words(hist)
    print 'Number of different words:', different_words(hist)
    print_most_common(hist)
