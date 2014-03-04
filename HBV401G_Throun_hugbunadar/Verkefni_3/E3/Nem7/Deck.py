
import random

class Deck:
	def __init__(self):
		self.deck = []
		suit = ["H", "C", "S", "D"]
		rank = range(1, 14)
		for i in suit:
			for j in rank:
				self.deck.append(str(j) + "o" + i)
				
	def shuffle(self):
		random.shuffle(self.deck)
		
	def draw(self):
		return self.deck.pop()