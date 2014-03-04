
from Deck import *

class Pondukapall:
	def __init__(self):
		self.board = [] #cards on the board(hand)
		self.on = True
		self.deck = Deck() #the deck
		self.deck.shuffle()
		for i in range(0,4):
			self.board.append(self.deck.draw())
		self.beginDisplay()
		self.redisplay()
	def checkSuit(self):
		if len(self.board) < 4:
				print "not enough cards"
				return
		if self.board[-1][-1] == self.board[-4][-1]: #if last character in last and fourth last is same
			self.board.pop(len(self.board)-2)
			self.board.pop(len(self.board)-2)
		else: 
			print "the last and fouth last cards are not the same suit\n"
		self.checkWinCondition()
		self.redisplay()
	def checkRank(self):
		if len(self.board) < 4:
			print "not enough cards"
			return
		if self.board[-4][0] == self.board[-1][0]:
			if len(self.board[-4]) == 3 or self.board[-4][1] == self.board[-1][1]:
				for i in range(0,4):
					self.board.pop()
		else: 
			print "\n the last and fourth last cards are not the same rank\n"
		self.checkWinCondition()
		self.redisplay()
	def draw(self):
		if len(self.deck.deck) > 0:
			if len(self.board) > 3:
				if self.board[-4][0] == self.board[-1][0] or self.board[-1][-1] == self.board[-4][-1]:
					print "you missed one LOSER, now live with it"
			self.board.append(self.deck.deck.pop())
		else:
			print "deck over"
		self.checkWinCondition()
		self.redisplay()
	def checkWinCondition(self):
		if len(self.deck.deck) <= 0:
			self.on = False
			if len(self.board) >= 4:
				if (self.board[-4][0] == self.board[-1][0] or self.board[-1][-1] == self.board[-4][-1]):
					return
			if len(self.board) <= 2:
				print "Game Over: YOU WIN!!\n"
				print "type restart to start over or exit to quit"
			else: 
				print "Game Over: You Lose"
				print "type restart to start over or exit to quit"
		return self.on
	def redisplay(self):
		print "\n"
		print map(str, self.board)
		print "\n"
	def beginDisplay(self):
		print "Welcome to Panda Solitaire\n"
		print "Type help for controlls"
	def helpDisplay(self):
		print "insert commands to play the game\n"
		print "d or draw: will draw a card\n"
		print "s or suit: will check the last and fourth last cards for same suit\n"
		print "r or rank: will check the lst and fourth last cards for the same rank\n"
		print "exit or quit: will end the game\n"
		print "help: will bring up this help text, but you know that allready"
		print "restart: will restart your game"
		self.redisplay()
		
		
def main():
	game = Pondukapall()
	while True:
		s = raw_input("-->")
		if s in ["d", "draw"]:
			game.draw()
		if s in ["quit", "exit"]:
			return
		if s in ["s", "suit"]:
			game.checkSuit()
		if s in ["r", "rank"]:
			game.checkRank()
		if s == "help":
			game.helpDisplay()
		if s == "restart":
			game = Pondukapall()
	
if __name__ == "__main__":
	main()
