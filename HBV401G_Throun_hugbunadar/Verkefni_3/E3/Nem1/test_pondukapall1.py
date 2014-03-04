import unittest
from spil1 import Spil 


class test_pondukapall1(unittest.TestCase):
    def test_sjaSpil(self):
        SPIL_prof = Spil('Laufa',9)
        self.assertEqual(type(SPIL_prof.sjaSpil()),type('strengur'))
        self.assertEqual(SPIL_prof.sjaSpil(), 'Laufa 9')
        
    def test_Spil_Eiginleikar(self):
        SPIL_prof = Spil('Laufa',9)
        self.assertEqual(SPIL_prof.sort,'Laufa')
        self.assertEqual(SPIL_prof.numer,9)
        
        
# Ekki var haegt ad profa margt thvi adeins einn klasi var notadur vid
# gerd forritsins. Allt sem profad var virkar tho. sjaSpil adferdin
# skilar streng eins og hun a ad gera og skila lika rettum streng
# Einnig eru eigineikarnir rettir.
# Adallega var notast vid while-lykkjur vid gerd leiksins.

if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)
