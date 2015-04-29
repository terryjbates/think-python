#!/usr/bin/env python
# encoding: utf-8
"""
exercise-18.3.py

Created by Terry Bates on 2014-08-03.
Copyright (c) 2014 http://the-awesome-python-blog.posterous.com. All rights reserved.
"""

import sys
import os
import random
import pprint

class Card(object):
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7','8', 
        '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    """Represents a standard playing card."""
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __cmp__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return cmp(t1, t2)


class Deck(object):
    # Alternative with nasty list comprehension
    # self.cards = [Card(suit,rank) for suit in range(4)
    #         for rank in range(1, 14)]
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        # Or use a list comprehension
        # res = [str(card) for card in self.cards]
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def shuffle(self):
        random.shuffle(self.cards)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def sort(self):
        # Method to have deck sort itself.
        self.cards.sort(cmp=Card.__cmp__)

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def count_card_freq(self):
        card_count_dict = dict()
        for card in self.cards:
            print card
            card_count_dict[card.rank] = card_count_dict.setdefault(card.rank, 0) + 1
        #pprint.pprint(card_count_dict)
        return card_count_dict

    def deal_hands(self, num_of_hands, cards_per_hand, hist):
        for hand_count in range(num_of_hands):
            # Create hand and label based on index
            hand_name = 'hand_num' + str(hand_count)
            hand = Hand(hand_name)
            #print
            #print "Created hand called", hand_name
            for card_count in range(cards_per_hand):
                # Pop cards into hand from the deck
                hand.add_card(self.pop_card())
                pass
            #print "Hand has cards"
            #print hand
            print "Hand Sum", hand.hand_value()
            hist.add_hand(hand)
            # Sum values of cards in hand

            #print "#" * 30


class Hand(Deck):
    def __init__(self, label=''):
        self.cards = []
        self.label = label

    def hand_value(self):
        total = 0
        for card in self.cards:
            total += card.rank
        return total


class Histogram(object):
    def __init__(self):
        self.count_dict = dict()

    def add_hand(self, hand):
        hand_dict = hand.count_card_freq()
        #pprint.pprint(hand_dict)
        for rank, count in hand_dict.items():
            self.count_dict[rank] = self.count_dict.setdefault(rank, 0) + count

def shuffle_deck(input_deck):
    # Shuffle the shit out of it
    for i in xrange(100):
        input_deck.shuffle()

def main():

    card_hist = Histogram()
    # Create new deck
    hot_deck = Deck()
    #hot_deck.count_card_freq()

    shuffle_deck(hot_deck)
    hot_deck.deal_hands(17, 3, card_hist)
    del hot_deck

    hot_deck = Deck()
    shuffle_deck(hot_deck)
    hot_deck.deal_hands(13, 3, card_hist)
    #pprint.pprint(card_hist.count_dict)
    for rank, count in card_hist.count_dict.items():
        print "{}\t{}".format(rank, count)


if __name__ == "__main__":
    main()