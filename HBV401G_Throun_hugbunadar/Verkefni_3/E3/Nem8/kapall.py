# -*- coding: cp1252 -*-
import sys
from random import shuffle

def clear(s):
    k=s**2
    return k

class spil(object):
    def spilastokkur(self):
        spil =["H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "HG", "HD", "HK", "S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "SG", "SD", "SK", "T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9", "T10", "TG", "TD", "TK", "L1", "L2", "L3", "L4", "L5", "L6", "L7", "L8", "L9", "L10", "LG", "LD", "LK"]
        shuffle(spil)
        return spil
def main():
    cards = spil()
    stokkur = cards.spilastokkur()
    hendi = []
    hendi.append(stokkur.pop())
    hendi.append(stokkur.pop())
    hendi.append(stokkur.pop())
    i=3
    print("Reglur kapalsins eru eftirfarandi")
    print("Ef spilin á endunum hafa sömu sort, geturu losað þig við spilin tvö á milli þeirra")
    print("Eg spilin á endunum hafa sömu tölu eða gildi, geturu losað þig við öll fjögur spilin")
    print("Þú vinnur ef þú getur endað með færri en fjögur spil")
    while(len(stokkur)>0):
        if(len(hendi)<5):
            print(hendi)
        else:
            print(hendi[i-4], hendi[i-3], hendi[i-2], hendi[i-1])
        input_var = input("settu inn 1 fyrir draga, 2 fyrir aðgerð, 3 til að hætta: ")
        if(input_var == 3):
            print("Þú tapaðir")
            sys.exit(0)
        elif(input_var==1):
            hendi.append(stokkur.pop())
            i=len(hendi)
        elif(input_var==2):
            if(hendi[i-1][0]==hendi[i-4][0]):
                hendi.pop(i-2)
                hendi.pop(i-3)
                i=len(hendi)
            elif(hendi[i-1][1]==hendi[i-4][1]):
                hendi.pop(i-1)
                hendi.pop(i-2)
                hendi.pop(i-3)
                hendi.pop(i-4)
                i=len(hendi)
            else:
                print("getur ekki gert neina aðgerð í þessari stöðu")
        else:
            print("Þú verður að velja 1, 2 eða 3")
    if(len(hendi)<4):
        print("til hamingju þú hefur unnið")
        sys.exit(0)
    else:
        print("nú er stokkurinn búinn, svo þegar þú dregur núna þá ertu einungis að setja aftasta spilið fremst, en þú mátt halda áfram þar til þú ert tilbúinn að gefast upp eða vinnur.")
        print(hendi)
        while(len(hendi)>3):
            if(len(hendi)<5):
                print(hendi)
            else:
                print(hendi[i-4], hendi[i-3], hendi[i-2], hendi[i-1])
            input_var = input("settu inn 1 fyrir draga, 2 fyrir aðgerð, 3 til að hætta: ")
            if(input_var == 3):
                print("þú tapaðir")
                sys.exit(0)
            elif(input_var==1):
                hendi.append(hendi.pop(0))
            elif(input_var==2):
                if(hendi[i-1][0]==hendi[i-4][0]):
                    hendi.pop(i-2)
                    hendi.pop(i-3)
                    i=len(hendi)
                elif(hendi[i-1][1]==hendi[i-4][1]):
                    hendi.pop(i-1)
                    hendi.pop(i-2)
                    hendi.pop(i-3)
                    hendi.pop(i-4)
                    i=len(hendi)
                else:
                    print("getur ekki gert neina aðgerð í þessari stöðu")
            else:
                print("Þú verður að velja 1, 2 eða 3")
        print("til hamingju þú hefur unnið")
main()
