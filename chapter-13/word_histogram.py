#!/usr/bin/env python
import string

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


if __name__ == "__main__":
    hist = process_file('pg7178.txt')
    print 'Total number of words:', total_words(hist)
    print 'Number of different words:', different_words(hist)
    print_most_common(hist)
