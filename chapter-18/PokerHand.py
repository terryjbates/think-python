"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from Card import *


class PokerHand(Hand):

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def rank_hist(self):
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_pair(self):
        self.rank_hist()
        for rank, count in self.ranks.items():
            #print
            #print "rank is ", rank
            #print "count is", count
            if count > 1:
                #print "BIG count is ", count
                return True
        return False

    def has_twopair(self):
        self.rank_hist()
        pair_count = 0
        for count in self.ranks.values():
            #print "count in has_two", count
            if pair_count >1:
                return True
            if count > 1:
                pair_count += 1
                #print "Found a pair"
        return False

    def has_three_of_a_kind(self):
        self.suit_hist()
        for val in self.suits.values():
            if val == 3:
                return True
        return False


if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print hand
        print
        print "Hand has flush", hand.has_flush()
        print "Hand has pair", hand.has_pair()
        print "Has has at least two pair", hand.has_twopair()
        print "Hand has 3 of a kind", hand.has_three_of_a_kind()
        print "#" * 40