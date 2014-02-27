from pondukapall import CardTranslator
from pondukapall import Deck
from pondukapall import Hand
from pondukapall import Rules
import unittest


class CardTranslatorTests(unittest.TestCase):
    
    knownValues = (
        (1, 'HA'), (2, 'H2'), (3, 'H3'), (4, 'H4'), (5, 'H5'), (6, 'H6'),
        (7, 'H7'), (8, 'H8'), (9, 'H9'), (10, 'H10'), (11, 'HG'), (12, 'HD'),
        (13, 'HK'), (14, 'SA'), (15, 'S2'), (16, 'S3'), (17, 'S4'), (18, 'S5'),
        (19, 'S6'), (20, 'S7'), (21, 'S8'), (22, 'S9'), (23, 'S10'), (24, 'SG'),
        (25, 'SD'), (26, 'SK'), (27, 'TA'), (28, 'T2'), (29, 'T3'), (30, 'T4'),
        (31, 'T5'), (32, 'T6'), (33, 'T7'), (34, 'T8'), (35, 'T9'), (36, 'T10'),
        (37, 'TG'), (38, 'TD'), (39, 'TK'), (40, 'LA'), (41, 'L2'), (42, 'L3'),
        (43, 'L4'), (44, 'L5'), (45, 'L6'), (46, 'L7'), (47, 'L8'), (48, 'L9'),
        (49, 'L10'), (50, 'LG'), (51, 'LD'), (52, 'LK') 
        )

    def test_number_to_card(self):
        for number, name in self.knownValues:
            result = CardTranslator.number_to_card(number)
            self.assertEqual(name, result)

class DeckTests(unittest.TestCase):

    def test_is_empty_true(self):
        deck = Deck()
        for x in range(1,53):
            temp = deck.draw()
        result = deck.is_empty()
        self.assertEqual(True, result)
    
    def test_is_empty_false(self):
        deck = Deck()
        result = deck.is_empty()
        self.assertEqual(False, result)

class HandTests(unittest.TestCase):

    def test_number_of_cards(self):
        hand = Hand()
        result = hand.number_of_cards()
        self.assertEqual(0, result)

    def test_number_of_cards_1(self):
        hand = Hand()
        deck = Deck()

        hand.add_to_hand(deck.draw())
        result = hand.number_of_cards()
        self.assertEqual(1, result)

    def test_is_emoty_true(self):
        hand = Hand()
        result = hand.is_empty()
        self.assertEqual(True, result)

    def test_is_empty_false(self):
        hand = Hand()
        deck = Deck()

        hand.add_to_hand(deck.draw())
        result = hand.is_empty()
        self.assertEqual(False, result)

class RulesTests(unittest.TestCase):

    def test_is_same_card_number_true(self):
        result = Rules.is_same_card_number(1,14)
        self.assertEqual(True, result)

    def test_is_same_card_number_false(self):
        result = Rules.is_same_card_number(2,25)
        self.assertEqual(False, result)

    def test_is_same_card_type_true(self):
        result = Rules.is_same_card_type(3, 10)
        self.assertEqual(True, result)

if __name__ == '__main__':
    unittest.main(verbosity = 2, exit=False)