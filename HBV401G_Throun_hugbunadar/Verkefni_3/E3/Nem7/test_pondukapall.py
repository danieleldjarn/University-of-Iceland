
import unittest
from Pondukapall import *

class testSolitaireFunctions(unittest.TestCase):
	def test_evaluate(self):
		game = Pondukapall()
		self.assertTrue(len(game.deck.deck) == 52)
		self.assertTrue(game.on)
		while game.on:
			game.draw()
		self.assertFalse(game.on)

	def test_Deck(self):
		testDeck = Deck()
		self.assertTrue(len(testDeck.deck) == 52)
		testDeck.shuffle()
		self.assertTrue(testDeck[0] != "1oH")
		testDeck.draw()
		self.assertTrue(len(testDeck.deck) == 51)

if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)