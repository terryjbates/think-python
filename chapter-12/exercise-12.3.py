#!/usr/bin/env python
# encoding: utf-8
"""
exercise-12.3.py

Created by Terry Bates on 2013-01-31.
Copyright (c) 2013 http://the-awesome-python-blog.posterous.com. All rights reserved.
"""

import re
letter_pattern = re.compile('[a-zA-Z]')

def compare(a,b):
    # sort on descending index
    return cmp(b[1], a[1])

def most_frequent(text_sample):
    # Create a list to store our tuple of letters and their counts
    list_of_letter_counts = []
    # Create dictionary to actually store key/value pairs of letters and
    # their respective counts.
    
    letter_count_dict = dict()
    for letter in text_sample:
        # Only match text that is a letter, using letter_pattern variable
        if letter_pattern.match(letter):
            letter = letter.lower()
            # Use setdefault. If no key, add key set to 0, then incremented 1.
            # If key already exists, it will be returned and incremented 1.        
            letter_count_dict[letter] = letter_count_dict.setdefault(letter,0) + 1
    # Use the .items() method to create a list of tuples containing
    # the letter and the count of occurrence.
    list_of_letter_counts = letter_count_dict.items()
    # Reverse sort the list of tuples
    list_of_letter_counts.sort(compare)
    
    res = []
    for letter,count in list_of_letter_counts:
        res.append((letter,count))
    return res
    
def main():
    # read in our word list from pickled object
    paragraph = """


    The enigmatic Italy international flew into Milan's Malpensa airport prior to undergoing a medical after the two clubs agreed a fee for the 22-year-old on Tuesday.

    There were chaotic scenes in Milan, with police forced to use smoke bombs to disperse jubilant fans crowding round a restaurant where Balotelli was meeting with club vice-president Adriano Galliani.

    Balotelli, who moved to the Premier League from Inter Milan in August 2010, is expected to put pen-to-paper on a four-and-a-half-year contract before Thursday's transfer deadline.

    The striker has endured a miserable time with City this season, scoring just one Premier League goal, and with his last start coming in the 3-2 derby defeat by Manchester United on 9 December, when he was hauled off after 52 minutes by a clearly frustrated Roberto Mancini.

    Balotelli is confident he will rediscover his best form away from the Etihad Stadium and is hoping that he will receive nothing but the full backing of the Milan supporters.

    Speaking to the Milan Channel, he admitted: "I ran to Milan.

    "I had wanted to play here for a long time. The start of this season was negative, but with this jersey I will do better.

    "I made some important choices, so I hope they can bring good luck to me and the team. I just want the fans to love me."

    Milan vice-president Adriano Galliani has admitted the transfer is a 'dream come true' and believes the arrival of Balotelli can only drive the Italian giants on to greater heights.

    Galliani told the club's official website: "It is a dream come true and something that we all wanted, with the president Silvio Berlusconi at the forefront.

    "With the arrival of Mario, we have strengthened our team a lot.

    "We have worked so hard and Mario has been in our hearts for a long time and finally we have succeeded in signing him."

    To find out more about live football on Sky sports, Click here

"""   
    print most_frequent(paragraph)

if __name__ == '__main__':
	main()

