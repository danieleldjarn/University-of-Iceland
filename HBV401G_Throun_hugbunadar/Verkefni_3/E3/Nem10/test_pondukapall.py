import unittest
import pondukapall

class test(unittest.TestCase):

    def test_athuga(self):
        prufari = pondukapall.Hond()
        self.assertEqual(prufari.athuga([('H',1)]),[])
        self.assertEqual(prufari.athuga([('H',1),('S',2)]),[])
        self.assertEqual(prufari.athuga([('H',1),('S',2),('T',3)]),[])
        self.assertEqual(prufari.athuga([('H',1),('S',2),('T',3),('L',4)]),[])
        self.assertEqual(prufari.athuga([('H',1),('S',2),('T',3),('H',4)]),[('S',2),('T',3)])
        self.assertEqual(prufari.athuga([('H',1),('S',2),('T',3),('L',1)]),[('H',1),('S',2),('T',3),('L',1)])
        self.assertEqual(prufari.athuga([('H',1),('S',2),('T',3),('L',4),('T',5)]),[])
        self.assertEqual(prufari.athuga([('H',1),('S',2),('T',3),('L',4),('S',5)]),[('T',3),('L',4)])
        self.assertEqual(prufari.athuga([('H',1),('S',2),('T',3),('L',4),('T',2)]),[('S',2),('T',3),('L',4),('T',2)])

    def test_fallega(self):
        prufari = pondukapall.Hond()
        self.assertEqual(prufari.fallega([('H',1)]),'H1')
        self.assertEqual(prufari.fallega([('H',1),('S',2)]),'H1, S2')
        self.assertEqual(prufari.fallega([('H',1),('S',2),('T',3),('L',4),('T',5)]),'H1, S2, T3, L4, T5')

    def test_hond_buinn(self):
        prufari = pondukapall.Hond()
        self.assertEqual(prufari.buinn([('H',1)]),True)
        self.assertEqual(prufari.buinn([('H',1),('S',1)]),True)
        self.assertEqual(prufari.buinn([('H',1),('S',1),('T',1)]),False)
        self.assertEqual(prufari.buinn([('H',1),('S',1),('T',1),('L',1)]),False)

    def test_stokkur_buinn(self):
        prufari = pondukapall.Stokkur()
        self.assertEqual(prufari.buinn([('H',1)]),False)
        self.assertEqual(prufari.buinn([('H',1),('S',1)]),False)
        self.assertEqual(prufari.buinn([('H',1),('S',1),('T',1)]),False)
        self.assertEqual(prufari.buinn([('H',1),('S',1),('T',1),('L',1)]),False)

if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)
