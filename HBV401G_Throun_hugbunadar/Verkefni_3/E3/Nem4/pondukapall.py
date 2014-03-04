
from random import shuffle
import sys
import re

# Utility function to raise exceptions within lambda functions
def raise_(ex):
    raise ex


class Deck:
	class Card:
		def __init__(self, suit, rank):
			self.suit = suit
			self.rank = rank
		
		def __str__(self):
			return '[' + self.rank + self.suit + ']'
		
		def __eq__(self, other):
			return self.suit == other.suit and self.rank == other.rank
		
		def getRankStr(self):
			return {'A': 'Ace',
			 		'K': 'King',
					'Q': 'Queen',
					'J': 'Jack',
					'10': 'Ten',
					'9': 'Nine',
					'8': 'Eight',
					'7': 'Seven',
					'6': 'Six',
					'5': 'Five',
					'4': 'Four',
					'3': 'Three',
					'2': 'Two'}.get(self.rank, self.rank)
		
		def getSuitStr(self):
			return {'H': 'Hearts',
					'S': 'Spades',
					'D': 'Diamonds',
					'C': 'Clubs'}.get(self.suit, self.suit)

	# A non-standard deck can be created by passing extra
	# arguments to the constructor.
	def __init__(self,\
	             suits=['H', 'S', 'D', 'C'],\
                 ranks=['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']):
		self.suits = suits
		self.ranks = ranks
		self.cards = []
		for s in suits:
			for f in ranks:
				self.cards.append(self.Card(s, f))
		self.hand = []
	
	def shuffle(self):
		shuffle(self.cards)
	
	def isEmpty(self):
		return len(self.cards) == 0
	
	def isHandEmpty(self):
		return len(self.hand) == 0
		
	def isHandLegal(self):
		return self.isHandEmpty() or len(self.hand) == 2
	
	def hasLegalMoves(self):
		legal = False
		if len(self.hand) >= 4:
			for i in range(len(self.hand)-3):
				legal = legal or self.hand[i].suit == self.hand[i+3].suit
				legal = legal or self.hand[i].rank == self.hand[i+3].rank
		return legal
	
	def canWin(self):
		if not self.isEmpty():
			return True
		elif self.hasLegalMoves():
			return True
		else:
			return False
		
	def cardsRemaining(self):
		return len(self.cards)
	
	def hasWon(self):
		victory = True
		victory = victory and self.isEmpty()
		victory = victory and self.isHandLegal()
		return victory
	
	def draw(self, p):
		card = self.cards.pop()
		self.hand = [card] + self.hand
		p.freshCard(card)
		p.display(self)
	
	def remove(self, args, prompt):
		try:
			try:
				
				indices = re.split('; |, |;|,|\s', args)
				if len(indices) < 2:
					raise Exception()
				if indices[0] == '':
					raise Exception()
			except:
				indices = re.split('-|:',args)
				if len(indices) == 2:
					indices = range(int(indices[0]), int(indices[1]))
					if len(indices) != 4:
						raise Exception()
				else:
					raise Exception()
		except:
			prompt.error()
			return
		
		l = len(self.hand)
		# Check whether indices are out of bounds
		for i in indices:
			if not 0 <= int(i) <= l:
				prompt.notLegal()
				return
		
		# If removing 2 cards from between matching suits
		removed = []
		if len(indices) == 2:
			try:
				if int(indices[1]) - int(indices[0]) != 1:
					raise Exception()
				suit1 = self.hand[int(indices[0])-1].suit
				suit2 = self.hand[int(indices[1])+1].suit
				if suit1 == suit2:
					removed.append(self.hand.pop(int(indices[0])))
					removed.append(self.hand.pop(int(indices[0])))
					prompt.removed(removed)
					prompt.display(self)
				else:
					raise Exception()
			except:
				prompt.notLegal()
		
		# If removing 4 cards between and including matching ranks		
		elif len(indices) == 4:
			try:
				
				rank1 = self.hand[indices[0]].rank
				rank2 = self.hand[indices[3]].rank
				if rank1 == rank2:
					for i in indices[::-1]:
						removed.append(self.hand.pop(int(i)))
					prompt.removed(removed)
					prompt.display(self)
				else:
					raise Exception()
			except:
				prompt.notLegal()
		else:
			prompt.notLegal()
		

# We create a separate namespace for the prompts	
class Prompt:
	def intro(self):
		print("______               _       _                     _ _ ")
		print("| ___ \             | |     | |                   | | |")
		print("| |_/ /__  _ __   __| |_   _| | ____ _ _ __   __ _| | |")
		print("|  __/ _ \| '_ \ / _` | | | | |/ / _` | '_ \ / _` | | |")
		print("| | | (_) | | | | (_| | |_| |   < (_| | |_) | (_| | | |")
		print("\_|  \___/|_| |_|\__,_|\__,_|_|\_\__,_| .__/ \__,_|_|_|")
		print("                                      | |              ")
		print("                                      |_|")
		print("Author: Anonymous")
		print("=======================================================")
		self.instructions()
	
	def victory(self):
		print("/\   /(_) ___| |_ ___  _ __ _   _ ")
		print("\ \ / / |/ __| __/ _ \| '__| | | |")
		print(" \ V /| | (__| || (_) | |  | |_| |")
		print("  \_/ |_|\___|\__\___/|_|   \__, |")
		print("                            |___/")
		print("You have victorized the game! Play again? (y/n)")
	
	def defeat(self):
		print("    ___      __            _   ")
		print("   /   \___ / _| ___  __ _| |_ ")
		print("  / /\ / _ \ |_ / _ \/ _` | __|")
		print(" / /_//  __/  _|  __/ (_| | |_ ")
		print("/___,' \___|_|  \___|\__,_|\__|")
		print("Ha! I won! You're out of moves! Play again? (y/n)")
	
	def newGame(self):
		print("New game started! Oh yeah!")
	
	def quit(self):
		print("Quitting is for losers.")
	
	def instructions(self):
		print("Type 'd' or 'draw' to draw a card.")
		print("Type 's' or 'show' to display your current hand.")
		print("Type 'r' or 'remove' followed by a list of zero-based indices to remove the corresponding cards")
		print("\t(e.g. 'r 0,1,2,3'). You can also enter a range (e.g. 'r 0-4' or 'r 0:4'), note that the")
		print("\trange is not inclusive, the last number is not part of it.")
		print("Type 'h' or 'help' to redisplay this message.")
		print("Type 'q' or 'quit' to exit.")
	
	def display(self, deck):
		print("There are " + str(deck.cardsRemaining()) + " cards left in the deck.")
		if not deck.isHandEmpty():
			print("Your hand is:")
			for i in range(len(deck.hand)):
				print(str(i) + ":\t"),
			print("\n"),
			for c in deck.hand:
				print(c.__str__() + "\t"),
			print("\n"),
		else:
			print("Your hand is empty! Nice!")
	
	def error(self):
		print("Input not recognized. Please try again.")
		
	def notLegal(self):
		print("Not a legal move. Please try again.")
	
	def remove(self, deck):
		print("Oops! You didn't specify which cards to remove! Please, type a list (e.g. '0,1') or a range (e.g. '0:4')")
		cmd = self.prompt()
		deck.remove(cmd, p)
	
	def removed(self, rm):
		for r in rm:
			print("Discarded the " + r.getRankStr() + " of " + r.getSuitStr() + ".")
	
	def freshCard(self, card):
		print("You drew the " + card.getRankStr() + " of " + card.getSuitStr() + ", " + card.__str__() + "!")
	
	def deckIsEmpty(self):
		print("The deck is empty, but there are still legal moves to be made!")
	
	def prompt(self):
		cmd = raw_input("> ")
		cmd = cmd.strip()
		# Remove leading and trailing whitespace
		return cmd.lower()

# Proprietary switch-statement:	
def switch(x, p, d):
	cmd = x
	if cmd == "":
		cmd = 'error'
	elif x[-1].isdigit():
		if x[0] == 'r':
			cmd = 're'
			if x[2] == 'e':
				args = x[7:]
			else:
				args = x[2:]
		else:
			p.error()
	
	return {
		're': lambda: d.remove(args, p),
		# If user types 'r' or 'remove' without arguments
		# they get a second prompt asking for arguments.
		'r': lambda: p.remove(d),
		'remove': lambda: p.remove(d),
		's': lambda: p.display(d),
		'show': lambda: p.display(d),
		'd': lambda: d.draw(p),
		'draw': lambda: d.draw(p),
		'h': lambda: p.instructions(),
		'help': lambda: p.instructions(),
		'q': lambda: raise_(Exception()),
		'quit': lambda: raise_(Exception()),
		'error': lambda: p.error()
		}.get(cmd, lambda: p.error())


	
def main():
	p = Prompt()
	p.intro()
	playing = True
	# Replay loop
	while playing:
		p.newGame()
		deck = Deck()
		deck.shuffle()
		# Main game loop
		while deck.canWin():
			if deck.isEmpty():
				p.deckIsEmpty()
			cmd = p.prompt()
			cmd = cmd.lower()
			action = switch(cmd, p, deck)
			try:
				action()
			except:
				# If player quits by typing 'q' or 'quit'
				p.quit()
				return 0
		if deck.hasWon():
			p.victory()
		else:
			p.defeat()
		
		while True:
			ans = p.prompt()
			ans = ans.lower()
			if ans == 'y':
				playing = True
				break
			elif ans == 'n' or ans == 'q' or ans == 'quit':
				playing = False
				break
			else:
				p.error()
	p.quit()
	return 0
	
if __name__ == "__main__":
	sys.exit(main())