# -*- coding: utf-8 -*-
from spil1 import Spil
import random

langtsort = ['Hjarta', 'Spada', 'Tigul', 'Laufa']
Spilastokkur = []
numerin = ['As',2,3,4,5,6,7,8,9,10,'Gosi','Drottning','Kongur']
#print len(numerin)

for i in range(0,13):
    for k in range(0,4):
        Spilastokkur.append(Spil(langtsort[k],numerin[i]))

random.shuffle(Spilastokkur)


# þegar spil byrjar, upphafsleikur

print 'Velkominn i kapalinn. Ef thu hefur ekki spilad adur lestu tha leidbeiningar:\n'
print 'Thetta virkar thannig ad thu byrjar med 4 spil a hendi. Ef sidasta spil thitt\n'
print 'og thad fjorda sidasta, (kemur efst her ad nedan), hafa somu sort, tha mattu\n'
print 'henda ut 2 spilunum sem eru a milli theirra med thvi ad sla inn 2.\n'
print 'Ef thessi somu spil hafa somu tolu tha mattu hinsvegar henda ollum spilunum\n'
print 'fjorum med thvi ad sla inn 4. Ef thu getur gert hvorugt tha gildir tvennt.\n'
print 'Ef enn eru spil i spilastokknum, tha verdurdu ad draga med thvi ad sla inn d.\n'
print 'Hinsvegar ef spilastokkurinn er tomur tha geturdu sett aftasta spilid thitt\n'
print 'fremst i hendi med thvi ad sla inn s. Adeins eru synd 4 oftustu spilin a hendi,\n'
print 'thau sem eru nothaef i hvert skipti. Thu vinnur (kapallinn gengur upp) ef thu\n'
print 'endar med 2 eda engin spil a hendi.\n'
print '\nHer fyrir nedan koma fyrstu 4 spilin thin. Gangi ther vel!\n'

hendi = []
for l in range(0,4):
    hendi.append(Spilastokkur[l])
    print len(hendi)
    hendi[l].sjaSpil()

del Spilastokkur[0:4]



while len(Spilastokkur) > 0: #Thegar stokkur er buinn er farid i adra lykkju thar sem s adgerdin er logleg
    val = raw_input('\nSladu inn adgerd (getur ytt a enter til ad fa upp adgerdir): ')
    if len(hendi) < 4 and val != 'd':
        print '\nThu verdur ad draga, ekkert annad haegt (sladu inn d)\n'
    elif val.lower() == 'draw': # Þessi adgerd er adeins her svo haegt se ad
        for l in range(0,42): # profa hina whilelykkjuna an thess ad draga 48 sinnum.
            hendi.append(Spilastokkur[l])
        for l in range(len(hendi)-4,len(hendi)):
            hendi[l].sjaSpil()
        del Spilastokkur[0:42]
    elif val.lower() == 'd':
        hendi.append(Spilastokkur[0])
        del Spilastokkur[0]
    elif val.lower() == '2':
        if hendi[len(hendi)-1].sort == hendi[len(hendi)-4].sort:
            del hendi[len(hendi)-3:len(hendi)-1]
        else:
            print '\nThetta mattu ekki gera, reyndu aftur\n'
    elif val.lower() == '4':
        if hendi[len(hendi)-1].numer == hendi[len(hendi)-4].numer:
            del hendi[len(hendi)-4:len(hendi)]
        else:
            print '\nThetta mattu ekki gera, reyndu aftur\n'
    else:
        print '\nLoglegar adgerdir, ef vid a, eru d (draga), 2 (henda 2 miðjuspilunum) og 4 (henda ollum 4 oftustu)\n'
    if len(hendi) >= 4:
        for l in range(len(hendi)-4,len(hendi)): #synir bara 4 oftustu spilin a hendi
            hendi[l].sjaSpil()
    else:
        for l in range(0,len(hendi)):
            hendi[l].sjaSpil() 
    print '\nThu hefur nu ' + str(len(hendi)) + ' spil a hendi. Synd eru nothaef spil'
    print 'I spilastokknu eru ' + str(len(Spilastokkur)) + ' spil eftir'

# Her er spilastokkurinn buinn og thvi adeins haegt ad setja aftasta spila a
# hendi fremst og halda thannig afram til ad sja hvort kapall gangi upp

fyrir = len(hendi)
teljari = 0
while len(hendi) != 2 and len(hendi) != 0: # Her ma setja fremsta spil aftast en ekki draga
    val = raw_input('\nSladu inn adgerd: ')
    if fyrir != len(hendi):
        teljari = 0
    teljari += 1
    fyrir = len(hendi)
    if val.lower() == 'd':
        print '\nThu getur ekki dregid, spilastokkur er tomur\n'
    elif val.lower() == '2':
        if hendi[len(hendi)-1].sort == hendi[len(hendi)-4].sort:
            del hendi[len(hendi)-3:len(hendi)-1]
        else:
            print '\nThetta mattu ekki gera, reyndu aftur\n'
    elif val.lower() == '4':
        if hendi[len(hendi)-1].numer == hendi[len(hendi)-4].numer:
            del hendi[len(hendi)-4:len(hendi)]
        else:
            print '\nThetta mattu ekki gera, reyndu aftur\n'
    elif val.lower() == 's':
        hendi.insert(0,hendi[len(hendi)-1])
        del hendi[len(hendi)-1]
    else:
        print '\nLoglegar adgerdir eru 2 (henda 2 miðjuspilunum), 4 (henda ollum 4 oftustu) og s (setja aftasta spila a hendi fremst)\n'
    if len(hendi) >= 4:
        for l in range(len(hendi)-4,len(hendi)): #synir bara 4 oftustu spilin a hendi
            hendi[l].sjaSpil()
    else:
        for l in range(0,len(hendi)):
            hendi[l].sjaSpil() 
    print '\nThu hefur nu ' + str(len(hendi)) + ' spil a hendi. Synd eru nothaef spil'
    if teljari >= fyrir*3:
        print 'Thu hefur reynt alltof oft, thessi virdist ekki aetla ad ganga upp'
        break

if teljari < fyrir*3:   
    print 'Thu hefur unnid leikinn, til hamingju!!'
    





#for l in range(0,len(hendi)):
#    hendi[l].sjaSpil()


    
#for x in range(3,len(sto))
