#!/usr/bin/env python
import string
import random

def process_line(line, h):
    line = line.replace('-', ' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace) 
        word = word.lower()
        h[word] = h.get(word, 0) + 1

def process_file(filename): 
    h = dict()
    fp = open(filename) 
    for line in fp:
        process_line(line, h) 
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


def cum_sum(h):
    my_sum = 0
    sum_list = []
    for val in h.values():
        my_sum += val
        # print my_sum
        # the original idea of sum_list[i] = my_sum *does not work*
        sum_list.append(my_sum)
    return sum_list


def bisect(search_term, my_list):

    # Shamelessly stolen from bisect.py
    lo = 0
    hi = len(my_list)
    while lo < hi:
        print "hi: %s lo: %s" % (hi, lo)
        mid = (lo+hi)/2
        if search_term == my_list[mid]:
            print "found search term %s at/near index %s in loop" % (search_term, mid)            
            return mid - 1
        elif search_term < my_list[mid]: 
            hi = mid
        else: 
            lo = mid + 1
    # Since we will likely not precisely find the search term, we may need to 
    # infer a position based on the last values of hi and lo
    print 
    print "out of loop hi: %s lo: %s" % (hi, lo)
    print "found search term %s at/near index %s" % (search_term, mid)

    return mid


if __name__ == "__main__":
    hist = process_file('pg7178.txt')
    # Create a list based on keys of histogram
    word_list = hist.keys()
    # Create a list containing the running cumulative sum of all words
    # use the last list entry, since it is the total
    cumulative_sum = cum_sum(hist)
    #print cumulative_sum
    # Choose random number between 1 to n, cast into string
    random_choice = random.randint(1, cumulative_sum[-1])
    print random_choice
    # Use the bisection search to find where random number is to be found on 
    # the cumulative sum list
    word_index = bisect(random_choice, cumulative_sum)
    print "Random word is ", word_list[word_index]
    print
    print 'Total number of words:', total_words(hist)
    print 'Number of different words:', different_words(hist)
    # print_most_common(hist)
