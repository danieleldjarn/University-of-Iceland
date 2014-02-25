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

    @staticmethod
    def card_to_number(str):
        for number, name in CardTranslator.deck_dict.items():
            if name == str:
                print number

class Deck:
    # Initialize a shuffled deck of cards
    def __init__(self):
        self.deck_array = range(1,53)
        random.shuffle(self.deck_array)

    # Draw a card from the deck and return it
    def draw(self):
        if self.is_empty() == False:
            return self.deck_array.pop()

    def is_empty(self):
        if (len(self.deck_array) == 0):
            return True
        else:
            return False

class Hand:
    def __init__(self):
        self.cards = []

    def show_hand(self):
        #print map(CardTranslator.number_to_card, self.cards)
        return self.cards

    def show_card(self, position):
        return self.cards[position]

    def add_to_hand(self, int):
        self.cards.append(int)

    def remove_from_hand(self, card_pos):
        self.cards.pop(card_pos)

    def number_of_cards(self):
        return len(self.cards)

    # Put the last card in the hand to the front
    def rotate(self):
        self.cards.insert(0, self.cards.pop())

    def is_empty(self):
        if (len(self.cards) == 0):
            return True
        else:
            return False

class Rules:

    @staticmethod
    def is_same_card_number(card1, card2):
        if card1%13 == card2%13:
            return True
        else:
            return False

    @staticmethod
    def is_same_card_type(card1, card2):
        if  card1 <= 13 and card2 <= 13 or \
            13 < card1 and card1 <= 26 and 13 < card2 and card2 <= 26 or \
            26 < card1 and card1 <= 39 and 26 < card2 and card2 <= 39 or \
            39 < card1 and card1 <= 52 and 39 < card2 and card2 <= 52:
            return True
        else:
            return False

    @staticmethod
    def rotate_hand(hand, deck):
        if deck.is_empty() == True:
            hand.rotate()
        else:
            print "This is an illegal move. Please draw all cards from the deck first."

    @staticmethod
    def remove_cards(hand, card_pos_1, card_pos_2):
        min_pos = min(card_pos_1, card_pos_2)
        max_pos = max(card_pos_1, card_pos_2)
        if max_pos - min_pos == 3:
            card1 = hand.show_card(min_pos)
            card2 = hand.show_card(max_pos)
            if Rules.is_same_card_number(card1, card2) == True:
                hand.remove_from_hand(max_pos)
                hand.remove_from_hand(max_pos - 1)
                hand.remove_from_hand(max_pos - 2)
                hand.remove_from_hand(min_pos) # max_pos - 3
            elif Rules.is_same_card_type(card1, card2) == True:
                hand.remove_from_hand(max_pos - 1)
                hand.remove_from_hand(max_pos - 2)
            else:
                "Unable to remove cards. Cards do neither have the same value or same type."

        else:
            print "This is an illegal move. The cards have to have two cards inbetween them."

    @staticmethod
    def is_game_over(deck, hand):
        if deck.is_empty() == False or hand.number_of_cards() > 2:
            return False
        else:
            return True

    @staticmethod
    def draw_from_deck(deck, hand):
        if deck.is_empty() == False:
            new_card = deck.draw()
            hand.add_to_hand(new_card)
            print "You drew", CardTranslator.number_to_card(new_card), "and it has been added to your hand"
        else:
            print "Unable to draw, deck is empty."

def main():
    deck = Deck()
    hand = Hand()

    print "Welcome to to Pondu"
    print "To draw a card type 'draw'"
    print "To remove cards from hand type 'remove' and then type \
     'X' and then 'Y', where X and Y are card positions"
    print "To rotate the hand when deck is empty type 'rotate'"
    print "To see this list of commands type 'help'"
    print ""
    print "Your hand is empty, please draw a card"

    while Rules.is_game_over(deck, hand) == False:
        command = raw_input('--> ')
        if command == "draw":
            Rules.draw_from_deck(deck, hand)
        elif command == "remove":
            # Here it would be easy to allow players to specify names of cards instead of 
            # positions, if I wan't to spend more time on this project.
            # Some sort of error handeling for the next two lines is needed in case the player
            # enters something other than an integer
            x = int(raw_input('Type the position of the first card (First position is 1): ')) - 1
            y = int(raw_input('Type the position of the second card: ')) - 1
            Rules.remove_cards(hand, x, y)
        elif command == "rotate":
            Rules.rotate_hand(hand, deck)
        elif command == "help":
            print "To draw a card type 'draw'"
            print "To remove cards from hand type 'remove' and then type \
             'X' and then 'Y', where X and Y are card positions"
            print "To rotate the hand when deck is empty type 'rotate'"
            print "To see this list of commands type 'help'"
            print ""
        else:
            print "Please enter a valid command"
        print "Your hand is", map(CardTranslator.number_to_card, hand.show_hand())

    print "Congratulations, you have won the game!"

if __name__ == '__main__':
    main()