import unittest
import pondukapall

class testFunctions(unittest.TestCase):
	
	def test_convertToTuple(self):
		testy = pondukapall.Deck()
		self.assertEqual(testy.convertToTuple("DK"), ('D', 'K'))
		self.assertEqual(testy.convertToTuple("S3"), ('S', '3'))
		self.assertEqual(testy.convertToTuple("HA"), ('H', 'A'))
		self.assertEqual(testy.convertToTuple("C8"), ('C', '8'))
		self.assertEqual(testy.convertToTuple("D10"), ('D', '10'))
		#self.assertEqual(1,1)

	def test_convertToString(self):
		testy = pondukapall.Deck()
		self.assertEqual(testy.convertToString(('H', 'J')), "HJ")
		self.assertEqual(testy.convertToString(('S', 'A')), "SA")
		self.assertEqual(testy.convertToString(('D', 7)), "D7")
		self.assertEqual(testy.convertToString(('C', 2)), "C2")
		self.assertEqual(testy.convertToString(('H', 10)), "H10")
		
	def test_count(self):
		testy = pondukapall.Deck()
		testy.cards = [('H', 'J'), ('S', 'A'), ('D', 7), ('C', 2), ('H', 10)]
		self.assertEqual(testy.count(), 5)
		
	def test_getRank(self):
		testy = pondukapall.Deck()
		testy.cards = [('H', 'J'), ('S', 'A'), ('D', 7), ('C', 2), ('H', 10)]
		self.assertEqual(testy.getRank(0), 'J')
		self.assertEqual(testy.getRank(1), 'A')
		self.assertEqual(testy.getRank(2), 7)
		self.assertEqual(testy.getRank(3), 2)
		self.assertEqual(testy.getRank(4), 10)
		
	def test_draw(self):
		testy = pondukapall.Deck()
		testy.cards = [('H', 'J'), ('S', 'A'), ('D', 7), ('C', 2), ('H', 10)]
		self.assertEqual(testy.draw(), ('H', 10))
		self.assertEqual(testy.draw(), ('C', 2))
		self.assertEqual(testy.draw(), ('D', 7))
		self.assertEqual(testy.draw(), ('S', 'A'))
		self.assertEqual(testy.draw(), ('H', 'J'))
		
if __name__ == '__main__':
	unittest.main(verbosity=2, exit=False)
	
#test_convertToTuple (__main__.testMaxFunctions)
#test_convertToString (__main__.testMaxFunctions)

