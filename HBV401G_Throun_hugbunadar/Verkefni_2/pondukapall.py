#!/usr/bin/python

import sys
import random # Used to shuffle the deck (randomize array)

class CardTranslator:

    card_names = [
        'HA', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HG', 'HD', 'HK',
        'SA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SG', 'SD', 'SK',
        'TA', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'TG', 'TD', 'TK',
        'LA', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'L9', 'L10', 'LG', 'LD', 'LK']
        # Dict to translate card numbers to names and vice versa
    deck_dict = dict(zip(range(1,53), card_names))

    # Translate a card number to a card name
    @staticmethod
    def number_to_card(int):
        return CardTranslator.deck_dict[int]

class Deck:

    # Initialize a shuffled deck of cards
    def __init__(self):
        self.deck_array = range(1,53)
        random.shuffle(self.deck_array)

    # Draw a card from the deck and return it
    def draw(self):
        return self.deck_array.pop()

class Hand:

    def show_hand():
        print map(CardTranslator.number_to_card, self.cards)

    def add_to_hand(int):
        self.cards.append(int)



def main():
    deck = Deck()
    hand = Hand()

if __name__ == '__main__':
    main()