import random

#Keyrsla: python pandakapall.py
#Notkun: stokkur = pandakapall()
#Leikurinn pandakapall hefur verid settur upp og notandi getur spilad
class pandakapall:
    def __init__(self):
        sort = ["H", "S", "T", "L"]
        teg = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "G", "D", "K"]
        #Stokkur heldur utanum spilin sem eftir eru i stokknum
        self.stokkur = []
        #Bord heldur utanum spilin sem eru a bordi eda a hendi
        self.bord = []
        self.faersla = 0
        #Buum til spilastokk
        for s in sort:
            for t in teg:
                self.stokkur.append(s+t)
        #Stokkum stokkinn
        random.shuffle(self.stokkur)
        #Byrjum a ad draga 4 spil
        for i in range(4):
            self.draga()

    #Notkun: stokkur.draga()
    #Buid ad draga eitt spil ur stokknum
    def draga(self):
        if self.fjoldistokkur() != 0:
            self.bord.append(self.stokkur.pop())
        else:
            print "Stokkurinn er tomur, verdur ad Faera!"

    #Notkun: stokkur.takaspil()
    #Buid er ad fjarlaega spil ef ef reglur kapalsins leyfa
    #Fjarlaegd verda 2 eda 4 spil
    def takaspil(self, k):
        if k == 2:
            temp = self.bord.pop()
            self.bord.pop()
            self.bord.pop()
            self.bord.append(temp)
        else:
            for i in range(4):
                self.bord.pop()

    #Notkun: stokkur.mataka()
    #Skilar True ef notandi ma taka spilin, annars False
    def mataka(self):
        a = self.bord[self.fjoldi()-1]
        b = self.bord[self.fjoldi()-4]
        if a[0] == b[0] or a[1] == b[1]:
            return True
        else:
            print "Thu matt ekki taka spilin"
            return False

    #Notkun: stokkur.synaspil()
    #Skrifar ut spil i bordi eda a hendi
    def synaspil(self):
        print self.bord

    #Notkun: stokkur.faera()
    #Setur aftasta spilid a hendi fremst
    def faera(self):
        if self.fjoldistokkur() == 0:
            c = self.bord.pop()
            self.bord.insert(0, c)
            self.faersla += 1
        else:
            print "Thu matt ekki faera nuna"

    #Notkun: stokkur.fjoldi()
    #Skilar fjolda spila a bordi
    def fjoldi(self):
        return len(self.bord)

    #Notkun: stokkur.fjoldistokkur()
    #Skila fjolda spila i spilastokk
    def fjoldistokkur(self):
        return len(self.stokkur)

    #Notkun: stokkur.sigur()
    #Heldur utanum hvort spilari hafi unnid eda tapad
    def sigur(self):
        if self.fjoldistokkur() == 0 and self.fjoldi() == 0:
            print "Thu vannst"
            return False
        elif self.fjoldistokkur() == 0 and self.fjoldi() == 2:
            print "Thu vannst"
            return False
        elif self.fjoldistokkur() == 0 and self.faersla == 3:
            print "Thu getur ekkert gert, thu tapadir"
            return False
        else:
            return True


#Notkun: main()
#Her er vidmotid um leikinn, t.e.a.s. tolvan spyr notenda hvad hann vill gera
def main():
    print "Leyfd inntok:"
    print "D : Dregur eitt spil ur stokknum"
    print "D 1 : Dregur eitt spil ur stokknum"
    print "D 2 : Dregur tvo spil ur stokknum"
    print "D 3 : Dregur thrju spil ur stokknum"
    print "T 2 : Tekur tvo spilin sem eru milli sama lit eda sortar"
    print "T 4 : Tekur fjogur spilin sem eru milli sama lit eda sortar"
    print "F : Setur aftasta spilid fremst"
    print ""
    spil = pandakapall()
    spil.synaspil()
    while spil.sigur():
        gera = raw_input("Hvad viltu gera? [D #/T #/F] ")
        if gera == "D 1" or gera == "D":
            spil.draga()
            print ""
        elif gera == "D 2":
            spil.draga()
            spil.draga()
            print ""
        elif gera == "D 3":
            spil.draga()
            spil.draga()
            spil.draga()
            print ""
        elif gera == "T 2" and spil.mataka():
            spil.takaspil(2)
            print ""
        elif gera == "T 4" and spil.mataka():
            spil.takaspil(4)
            print ""
        elif gera == "F":
            spil.faera()
            print ""
        else:
            print "Ologleg adgerd, vinsamlegast reyndu aftur."
            print ""
        spil.synaspil()

#Keyrum main fallid
main()



