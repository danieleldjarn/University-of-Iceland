# -*- coding: cp1252 -*-
import sys
import math
import Image
import random
import itertools

	#set föllin fyrir utan klasa til að eiga auðveldara með að einingaprófa þau.
		#fall sem skilar að hvaða sort spil er
def check_value_sort(card):
	return card[1:]
		#fall sem skilar hvaða gildi er á spilinu, ás uppí kóng.
def check_value_number(card):
	return card[:1]	

class kapli:
	
	def deckofcards_test():
		#tilviksbreytur
		ruslatunna = []
		sortir = 'HSDC'
		radir = '23456789TJQKA'
		global array
		array = []
		victory = False
		break_from_while = False

		#bý til stokkinn
		DECK = tuple(''.join(card) for card in itertools.product(radir, sortir))
		unused_cards = DECK
		unused_cards #geymir spilin í "rétti röð 2-ás"
	
		#shuffle up!!
		for x in range(0,51):
			unused_cardss = random.sample(unused_cards,52)
		
		unused_cardss #geymir stokk sem búið er að stokka! 

		#dreg þrjú spil og prenta þau út.
		for x in xrange(0,3):
			 array.append(unused_cardss.pop())
		print array



		#hérna kemur "leikurinn" sjálfur
		while(len(unused_cardss) != 0 ): 
			s = raw_input("hvað viltu gera? draw, pull2, pull4")

			if(len(array) == 0 and len(ruslatunna)>47):
				victory = True
			if( len(ruslatunna)>47 and len(array) == 2 ): 
				victory = True

			if(victory == True):
				print "Til hamingju þú vannst leikinn!"
				#image = Image.open('victory.jpg') - just for fun!
				#image.show()

				break_from_while = True
				break

			if(s == "draw" and victory == False and len(unused_cardss) > 0):
				array.append(unused_cardss.pop())
				print array

			if(len(array) >3 ):



				if(s == "pull2" and victory == False):

					if( check_value_sort(array[len(array)-1]) != check_value_sort(array[len(array)-4]) ):
						print "skamm má ekki, veldu annað"
						print array		

					elif( check_value_sort(array[len(array)-1]) == check_value_sort(array[len(array)-4]) ):	
						
							ruslatunna.append(array.pop(len(array)-2))
							ruslatunna.append(array.pop(len(array)-2))
							print array
				if(s == "pull4" and victory == False):			
					if( check_value_number(array[len(array)-1]) != check_value_number(array[len(array)-4]) ):	
							print "skamm má ekki,veldu annað"
							print array

					if( check_value_number(array[len(array)-1]) == check_value_number(array[len(array)-4]) ):		
						
							ruslatunna.append(array.pop(len(array)-1))
							ruslatunna.append(array.pop(len(array)-1))
							ruslatunna.append(array.pop(len(array)-1))
							ruslatunna.append(array.pop(len(array)-1))
							print array

			if( break_from_while == True):
				break	
		if(break_from_while == False):
			print "Djöfulsins aumingi, þú tapaðir reyndu aftur"	
	

	if __name__ == "__main__":
		deckofcards_test()

