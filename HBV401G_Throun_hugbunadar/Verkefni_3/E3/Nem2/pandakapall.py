import random
import sys

class kapall:
	deck =['H1','H2','H3','H4','H5','H6','H7','H8','H9','HT','HG','HD','HK',
        'S1','S2','S3','S4','S5','S6','S7','S8','S9','ST','SG','SD','SK',
        'T1','T2','T3','T4','T5','T6','T7','T8','T9','TT','TG','TD','TK',
        'L1','L2','L3','L4','L5','L6','L7','L8','L9','LT','LG','LD','LK']


stokkur = kapall.deck

random.shuffle(stokkur)


def upphaf(x):
	
	if x is 'n' or x is 'N':
		p = raw_input('How about now? (y/n) ')
		return upphaf(p)
	if x is 'y' or x is 'Y':
		print ('Great!'),
		print ('You will be dealt three cards')
		print ('to begin with and then one by one')
		print ('each time you type draw a card.')
		print ('After each turn you will be presented')
		print ('with your hand and you can decide what')
		print ('you want to do next. Your options are ')
		print ('"remove2" , "remove4" , "draw" and ')
		print ('"surrender"')
	else:
		s = raw_input('please type either y or n ')
		return upphaf(s)

svar1 = raw_input('ready to start pandakapall? (y/n) ')

upphaf(svar1)

hand = []

for x in range(0,3):
	hand.append(stokkur.pop(0))

print ('the cards you have in your "hand" now are: ')
print hand
print ('all you can do now is draw, I will take care of that for you this time!')
hand.append(stokkur.pop(0))

def nextMove(svarid):
	p = int(len(hand))-1
	q = p-3
	z = hand[p]
	x = hand[q] 

	if	(
			svarid == 'remove2' and
			x[0] == z[0]
		):
		print('ok, you have removed the 2 cards in the middle.')
		del hand[q+1:p]
	if	(
			svarid == 'remove4' and
			x[1] == z[1]
		):
		print('ok, you have removed the 4 last cards.')
		del hand[q:p+1]
	if svarid == 'surrender':
		sys.exit()

talning = 48

while talning > 0:
	print ('the cards you have in your "hand" are: ')
	print hand
	svar2 = raw_input('What is your next move?  ' )


	if svar2 == 'draw':
		hand.append(stokkur.pop(0))
		talning-=1
	else:
		nextMove(svar2)

if	(
			talning == 0 and
			len(hand) == 0
		):
		print('Congratulations, you won!!!!!')
		sys.exit()

if	(
		talning == 0 and
		len(hand) == 2
	):
	print('Congratulations, you won!!!!!')
	sys.exit()

else:
	print('Sorry to tell you that you lost,')
	print('Feel free to try again!')