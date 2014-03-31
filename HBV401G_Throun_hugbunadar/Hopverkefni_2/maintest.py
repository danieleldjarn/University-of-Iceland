#!/usr/bin/python
#coding=utf-8

from Kapall_klasi import *

if __name__ == '__main__':
	tree = Tree()
	spilastokkur = Stokkur()
	spilastokkur.nyr_random_stokkur()
	tree.make_tree(spilastokkur)
	'''
	Á þesum tímapunkti er tréið fullt og spilastokkur heldur utan um þau spil sem eftir eru
	og öll spil eru komin í tréið. Spilin í tréinu eru geymd í t.stokkur.stokkur og hægt
	er að komast að því hvort hægt sé að sækja það úr tréinu með tree.is_removeable(x),
	þar sem x er einhvað spil úr tréinu.
	'''
	ruslabunki = Stokkur()

	while True:
		print "\n"
		if not tree.stokkur.has_next() or not spilastokkur.has_next():
			break
		if ruslabunki.spilafjoldi == 0:
			ruslabunki.add(spilastokkur.get_next())

		print "Spilið efst í ruslastokknum er: ",ruslabunki.stokkur[-1]
		print "Spil sem þú getur fjarlægt úr tréi:"
		removeables = tree.get_removeables()
		cnt = len(removeables.stokkur)-1

		print removeables
		what_to_do = raw_input("Veldu 1 til að fjarlægja spil úr tréi, annars verður dregið nýtt spil úr stokki: ")
		if what_to_do == "1":
			try:
				tala = int(raw_input("Veldu tölu frá 0 upp í "+str(cnt)+" og athugaðu hvort það sé hægt að setja það efst í ruslabunkann: "))
			except:
				print "Verður að slá inn tölu frá 0 upp í ",cnt
				continue
			if tala > cnt or tala < 0:
				print "Verður að slá inn tölu frá 0 upp í ",cnt
				continue

			delgildi = removeables.stokkur[tala].gildi
			if delgildi == 13:
				legit_remove = [1,12]
			elif delgildi == 1:
				legit_remove = [2,13]
			else:
				legit_remove = [delgildi+1, delgildi-1]


			if ruslabunki.stokkur[-1].gildi in legit_remove:
				ruslabunki.add(removeables.get_next(tala))
				tree.update_tree(ruslabunki.stokkur[-1])

			else:
				print "\n"
				print "***********************************************"
				print "Ekki hægt hægt að bæta spili við í ruslabunkann"
				print "***********************************************"

		else:
			ruslabunki.add(spilastokkur.get_next())

	if tree.stokkur.spilafjoldi == 0:
		print "stokkur trés: ",tree.stokkur.stokkur
		print "Þú vannst!"
	else:
		print "aaaawwwwwwwww, spilin eftir í tréinu eru:"
		print tree.get_removeables()
