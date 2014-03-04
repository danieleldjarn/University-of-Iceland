
# Unit test for deck.py

import pondukapall as p
import unittest

class LegalDeck(unittest.TestCase):
	
	# Check whether the deck is of the correct size w.r.t.
	# the number of suits and ranks
	def testDeckSize(self):
		deck = p.Deck()
		deckSize = len(deck.suits) * len(deck.ranks)
		self.assertEqual(len(deck.cards), deckSize)
	
	# Check whether each card exists only once within the deck
	def testCardUnique(self):
		deck = p.Deck()
		for c in deck.cards:
			deck.cards.sort(key=lambda c: c.suit, reverse=True)
			deck.suits.sort()
			for s in deck.suits:
				for f in deck.ranks:
					d = [d for d in deck.cards if d == deck.Card(s, f)]
					# Check whether there's exactly one card of each type
					self.assertTrue(len(d) == 1)
					deck.cards.remove(d[0])
		# Check whether there are any cards that were not popped
		# from the list in the for-loop.
		self.assertTrue(len(deck.cards) == 0)

	# Test for the __eq__ function
	def testCardComparison(self):
		deck = p.Deck()
		ah1 = deck.Card('H', 'A')
		ah2 = deck.Card('H', 'A')
		self.assertTrue(ah1 == ah2)

		as1 = deck.Card('S', 'A')
		self.assertFalse(ah1 == as1)


class DeckActions(unittest.TestCase):
	# Create a dummy prompt structure so we don't write to std output:
	class dummyPrompt:
		def freshCard(self, c):
			return 0
		def display(self, d):
			return 0
		def removed(self, r):
			return 0
		def notLegal(self):
			return 0

	def testIsEmpty(self):
		deck = p.Deck()
		# Here we use an index in the range of len(deck.cards)
		# because we're popping from deck.cards in each iteration
		# (=> deck.cards is mutable for the duration of the loop)
		for i in range(len(deck.cards)):
			self.assertFalse(deck.isEmpty())
			deck.cards.pop()
		self.assertTrue(deck.isEmpty())

	def testDraw(self):
		dummy = self.dummyPrompt()
		deck = p.Deck()
		c1 = len(deck.cards)
		h1 = len(deck.hand)
		deck.draw(dummy)
		c2 = len(deck.cards) + 1
		h2 = len(deck.hand) - 1
		self.assertTrue(c1 == c2 and h1 == h2)

	def testHasLegalMoves(self):
		dummy = self.dummyPrompt()
		deck = p.Deck()
		# Create a hand with only illegal moves:
		deck.hand.append(deck.Card('H', '2'))
		deck.hand.append(deck.Card('H', '3'))
		deck.hand.append(deck.Card('H', '4'))
		deck.hand.append(deck.Card('S', '5'))
		deck.hand.append(deck.Card('S', '6'))
		deck.hand.append(deck.Card('S', '7'))
		deck.hand.append(deck.Card('D', '9'))
		deck.hand.append(deck.Card('D', '10'))
		deck.hand.append(deck.Card('D', 'J'))
		deck.hand.append(deck.Card('C', 'Q'))

		self.assertFalse(deck.hasLegalMoves())

		# Create a legal suit move:
		deck.hand[5] = deck.Card('H', 'A')
		deck.hand[8] = deck.Card('H', 'K')

		self.assertTrue(deck.hasLegalMoves())

		# Create a legal rank move:
		deck.hand[8] = deck.Card('S', 'A')

		self.assertTrue(deck.hasLegalMoves())

	def testRemove(self):
		# This function does not return a value, 
		dummy = self.dummyPrompt()
		deck = p.Deck()
		# Create a hand with an illegal move:
		deck.hand.append(deck.Card('H', '2'))
		deck.hand.append(deck.Card('H', '3'))
		deck.hand.append(deck.Card('H', '4'))
		deck.hand.append(deck.Card('S', '5'))

		try:
			deck.remove('1,2', dummy)
		except:
			self.assertTrue(len(deck.hand) == 4)

		# Create a legal suit move:
		deck.hand[3] = deck.Card('H', '5')
		deck.remove('1,2', dummy)
		self.assertTrue(len(deck.hand) == 2)

		# Create a legal rank move:
		deck.hand.append(deck.Card('S', 'A'))
		deck.hand.append(deck.Card('S', '2'))
		deck.remove('0:4', dummy)

		self.assertTrue(len(deck.hand) == 0)


if __name__ == "__main__":
	unittest.main() 