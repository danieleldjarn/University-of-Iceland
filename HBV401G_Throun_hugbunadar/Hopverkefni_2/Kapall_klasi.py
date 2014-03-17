#!/usr/bin/python
#coding=utf-8

################################################################################
class Spil(object):
    'Klasi sem býr til eitt spil í einu og heldur utan um gildi þess og sort'
    def __init__(self,sort,gildi):
        self.sort  = sort
        self.gildi = gildi
        

    def __repr__(self):
        'Strengjaframsetning spils'
        letters = {1:'Ás', 11:'Gosi', 12:'Drolla', 13:'Kóngur'}
        letter = letters.get(self.gildi, str(self.gildi))
        return "<%s %s>" % (self.sort, letter)
#-------------------------------------------------------------------------------

################################################################################
class Stokkur(object):
    'Klasi sem býr til stokk og heldur utan um spilin sem eru í honum'
    def __init__(self, spil=0, make_card=Spil):
        self.stokkur = []
        self.spilafjoldi = spil
        self.make_card = make_card

    def nyr_random_stokkur(self):
        'Tæmir stokk og setur 52 ný spil í hann í random röð'
        sort = ["H","S","T","L"]
        gildi = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        self.stokkur = []
        self.spilafjoldi = 0
        for i in range(len(sort)):
            for j in range(len(gildi)):
                self.add(self.make_card(sort=sort[i], gildi=gildi[j]))
        return self.stokka()

    def stokka(self):
        'Stokkar stokkinn'
        from random import shuffle
        return shuffle(self.stokkur)

    def add(self,*spilin):
        'Bætir ótakmörkuðum fjölda spila í stokk'
        for spil in spilin:
            self.stokkur += [spil]
            self.spilafjoldi += 1

    def get_next(self):
        'Sækir næsta spil í stokkinn og skilar því'
        if self.spilafjoldi == 0:
            return None
        else:
            self.spilafjoldi -= 1
            spil = self.stokkur[-1]
            del self.stokkur[-1]
            return spil

    def has_next(self):
        'Skilar True þþaa stokkurinn sé ekki tómur'
        return self.spilafjoldi > 0


    def __repr__(self):
        'Strengjaframmsetning stokks'
        s = "Stokkurinn samanstendur af: \n"
        for i in range(len(self.stokkur)):
            s = s + " " + str(self.stokkur[i])+"\n"
        return s
#-------------------------------------------------------------------------------

if __name__ == '__main__':
	kapall = Stokkur()
	kapall.nyr_random_stokkur()
	print kapall.spilafjoldi
	while kapall.has_next():
	    print kapall.get_next()
	print kapall.spilafjoldi
