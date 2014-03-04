import random

# Skilgreining a spilastokknum:
deck =['H1','H2','H3','H4','H5','H6','H7','H8','H9','HT','HG','HD','HK',
    'S1','S2','S3','S4','S5','S6','S7','S8','S9','ST','SG','SD','SK',
    'T1','T2','T3','T4','T5','T6','T7','T8','T9','TT','TG','TD','TK',
    'L1','L2','L3','L4','L5','L6','L7','L8','L9','LT','LG','LD','LK']
print (' ')
print ('stokkurinn skilgreindur sem breytan "deck"')
print (' ')
print deck


# Spilin stokkud:
print (' ')
print ('nu stokka eg spilastokkinn thrisvar og prenta hann ut i hvert skipti')
print (' ')

for x in range(0,3):
	random.shuffle(deck)
	print deck
	print (' '),
	print (' ')

# Svona eru spilin dregin

hand = []
print ('eftirfarandi kodi er notadur til ad draga spil:')
print (' ')
print ('hand.append(deck.pop(0))')
print (' ')
print ('Herna eru svo utprentanir af fjorum umferdum af "draw":')
hand.append(deck.pop(0))
print hand
hand.append(deck.pop(0))
print hand
hand.append(deck.pop(0))
print hand
hand.append(deck.pop(0))
print hand