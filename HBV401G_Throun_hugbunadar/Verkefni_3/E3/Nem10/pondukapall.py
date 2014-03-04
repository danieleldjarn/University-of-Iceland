#!/usr/bin/env python
# encoding: utf-8

import random

class Stokkur:
    def __init__(self):
        self.stokkur = self.bua_til_stokk()

    def bua_til_stokk(self):
        stk = [(tegund,numer) for tegund in ['H','S','T','L'] for numer in range(1,14)]
        random.shuffle(stk)
        return stk

    def buinn(self, test=[]):
        stokkur = test or self.stokkur
        if len(self.stokkur) == 0:
            return True
        else:
            return False

    def fa_naesta(self):
        if not self.buinn():
            return self.stokkur.pop()

class Hond:
    def __init__(self):
        self.hond = []

    def __str__(self):
        return self.fallega(self.hond)

    def nytt_spil(self, spil):
        self.hond.append(spil)

    def athuga(self, test=[]):
        hond = test or self.hond
        if len(hond) < 4:
            return []
        elif hond[-4][1] == hond[-1][1]:
            return hond[-4:]
        elif hond[-4][0] == hond[-1][0]:
            return hond[-3:-1]
        else:
            return []

    def taka_aftast(self):
        return self.hond.pop(0)

    def fallega(self, spil):
        return ', '.join([x[0] + str(x[1]) for x in spil])

    def taka_burt(self, burt):
        for i in burt:
            self.hond.remove(i)

    def buinn(self, test=[]):
        hond = test or self.hond
        if len(hond) <= 2:
            return True
        else:
            return False


class Leikur:
    def __init__(self):
        self.stokkur = Stokkur()
        self.hond = Hond()
        self.afram()

    def afram(self):
        teljari = 1
        while True:
            if self.hond.buinn() and self.stokkur.buinn():
                print('Sigurvegari er þú!')
                break
            print('----- ' + str(teljari) + ' -----')
            teljari += 1
            print('Spilin þín:')
            print(self.hond)
            print('Hvað viltu gera?')
            burt = self.hond.athuga()
            if burt:
                print(str(1) + ' : Taka burt ' + self.hond.fallega(burt))
            print('Q : Hætta.')
            print('Allt annað : Næsta spil.')
            svar = raw_input()
            if svar == '1' or svar == '':
                self.hond.taka_burt(burt)
            if svar == 'q' or svar == 'Q':
                break
            if self.stokkur.buinn():
                self.hond.nytt_spil(self.hond.taka_aftast())
            else:
                self.hond.nytt_spil(self.stokkur.fa_naesta())
        print('Leik lokið.')

def main():
    leikur = Leikur()

if __name__ == '__main__':
    main()
