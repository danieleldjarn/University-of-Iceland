import unittest
import solitaire_prufa


class testFunctions(unittest.TestCase):
	def test_check_value_sort(self):
		self.assertEqual(solitaire_prufa.check_value_sort('6A'),'A')

	def test_check_value_number(self):
		self.assertEqual(solitaire_prufa.check_value_number('6A'),'6')


if __name__ == '__main__':
	unittest.main()