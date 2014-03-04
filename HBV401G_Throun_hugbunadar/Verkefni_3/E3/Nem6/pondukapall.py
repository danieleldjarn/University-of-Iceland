#!/usr/local/bin/python2.7

import random
from array import *
import readline

class Deck:
	
	def __init__(self):
		self.cards = []
	
	def fill(self):
		for suit in ['C', 'D', 'H', 'S']:
			for rank in range(2,11):
				self.cards.append((suit, str(rank)))
			for rank in ['J', 'Q', 'K', 'A']:
				self.cards.append((suit, rank))
		return self
	
	def shuffle(self):
		random.shuffle(self.cards)
	
	def empty(self):
		self.cards = []
	
	def draw(self):
		return self.cards.pop()
	
	def add(self, card):
		self.cards.append(card)
	
	def count(self):
		return len(self.cards)
	
	def getRank(self, index):
		return self.cards[index][1]
		
	def getSuit(self, index):
		return self.cards[index][0]
		
	def removeCards(self, i, j):
		if j == self.count()-1:
			self.cards = self.cards[:i]
		else:
			b = self.cards[j+1:]
			self.cards = self.cards[:i]
			self.cards.extend(b)
			
	def convertToString(self, tup):
		suit = tup[0]
		rank = str(tup[1])
		return "" + suit + rank

	def convertToTuple(self, string):
		return (string[0],string[1:])
		
		
	def findCard(self, string):
		try:
			return self.cards.index(self.convertToTuple(string))
		except ValueError:
			return None
	
	def shift(self):
			x = self.cards.pop() 
			self.cards.insert(0, x)
		
	def deckToString(self):
		string = ""
		for card in self.cards:
			string += self.convertToString(card) + "  "
		return string



class solitaire:

	def __init__(self):
		self.drawPile = Deck()
		self.hand = Deck()
		self.discard = Deck()
		
	def deal(self):
		self.drawPile.empty()
		self.hand.empty()
		self.discard.empty()
		self.drawPile.fill().shuffle()
	
	def prepareHand(self):
		while self.drawPile.count() > 0 and self.hand.count() < 4:
			self.drawCard()
			
	def drawCard(self):
		if self.drawPile.count() > 0:
			card = self.drawPile.draw()
			self.hand.add(card)
		else:
			print "The deck is empty."
	
	def printTurn(self):
		print " "
		print "Your hand is: ", self.hand.deckToString()
		print "The deck has ", self.drawPile.count(), " cards left."
		print "type 'help' for a list of commands."
		
	def checkWin(self):
		if (self.hand.count() == 2 or self.hand.count() == 0) and self.drawPile.count() == 0:
			print "You won the game!"
			return true
		
	def commands(self):
		print "Here is a list of commands:"
		print "quit"
		print "pass"
		print "restart"
		print "help"
		print "shift"
		print "match suit 'name of first card to match' 'name of later card to match'"
		print "match rank 'name of first card to match' 'name of later card to match'"
		
	def take2(self, x, y):
		i = self.hand.findCard(x)
		if i is None:
			print x + " was not found"
		j = self.hand.findCard(y)
		if j is None:
			print y + " was not found"
		if self.hand.getSuit(i) == self.hand.getSuit(j):
			if j > i and j-i == 3:
				self.hand.removeCards(i+1, j-1)
			elif i > j and i-j == 3:
				self.hand.removeCards(j+1, i-1)	
			if j-i != 3:
				print "Two cards need to be in between the chosen cards."
		else:
			print "The chosen cards are not of the same sort."
		
	def take4(self, x, y):
		i = self.hand.findCard(x)
		if i is None:
			print x + " was not found"
		j = self.hand.findCard(y)
		if j is None:
			print y + " was not found"
		if self.hand.getRank(i) == self.hand.getRank(j):
			if j > i and j-i == 3:
				self.hand.removeCards(i, j)
			elif i > j and i-j == 3:
				self.hand.removeCards(j, i)	
			if j-i != 3:
				print "Two cards need to be in between the chosen cards."
		else:
			print "The chosen cards are not of the same rank."
			
			
	def shift(self):
		if len(self.drawPile.cards) == 0:
			self.hand.shift()	
		else:
			print "That is not a legal move."
			
	
def main():
	print "Welcome to panda solitaire, have fun."
	sol = solitaire()
	sol.deal()
	while True:
		sol.prepareHand()
		sol.printTurn() 
		sol.checkWin()
		if sol.checkWin() == True:
			break
		line = raw_input("Enter the desired command: ").split()
		if len(line) == 0:
			print "Unknown command."
			sol.commands()
		elif line[0] == 'quit':
			break
		elif line[0] == 'pass':
			sol.drawCard()
		elif line[0] == 'restart':
			sol.deal()
		elif line[0] == 'help':
			sol.commands()
		elif line[0] == 'match' and len(line) == 4 and line[1] == 'suit': 
			sol.take2(line[2], line[3])
		elif line[0] == 'match' and len(line) == 4 and line[1] == 'rank':  
			sol.take4(line[2], line[3])
		elif line[0] == 'shift':
			sol.shift()
		else:
			print "Unknown command."
			sol.commands()
	print "Goodbye." 

if __name__=="__main__":
	main()
