import random
import string
from msvcrt import getch


class Card(object):

    suit_names = ["L", "T", "H", "S"]
    rank_names = [None, "1", "2", "3", "4", "5", "6", "7", 
              "8", "9", "10", "11", "12", "13"]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '[%s %s]' %(Card.suit_names[self.suit],Card.rank_names[self.rank])
		

class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)
	
	
    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

    def pop_card(self, i=-1):
        return self.cards.pop(i)	

    def shuffle(self):
        random.shuffle(self.cards)
		

if __name__ == '__main__':
	deck = Deck()
	deck.shuffle()
	
	j = 0
	print('Enter til ad halda afram')
	print('Ctrl+C, er til ad haetta i kapli')
	n = 1
	while j < 53:
		for i in range(n):
			var = raw_input(deck.pop_card(n))
			string = var.split(',')
			print string
				
		j = j+1
		
	

	
	
	

	
