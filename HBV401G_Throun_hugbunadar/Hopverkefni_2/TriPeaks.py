import pygame
from pygame.locals import *
import pygame.mouse as mouse
import Kapall_klasi as game
import Menu_test

WIDTH, HEIGHT = 800, 600
CARDW, CARDH = 72, 96
BACKGROUNDCOLOR = (1,83,9)
TOPMARGIN = 30
DECKLOCATION = WIDTH/2-CARDW, 2*HEIGHT/3
DECFONTLOCATION = DECKLOCATION[0]+CARDW/3, DECKLOCATION[1]+CARDH/4
TRASHLOCATION = WIDTH/2+CARDW/2, 2*HEIGHT/3 

def loadCardImage(name):
    path = "cards/"+str(name)+'.png'
    try:
        image = pygame.image.load(path)
    except pygame.error, message:
        raise SystemExit, message
    image = image.convert()
    return image

def initPygame(width, height):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Tri Peaks")
    pygame.mouse.set_visible(1)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BACKGROUNDCOLOR)
    font = pygame.font.Font(None, 45)
    return screen, background, font

def initTriPeaks():
    tree = game.Tree()
    deck = game.Stokkur()
    deck.nyr_random_stokkur()
    tree.make_tree(deck)
    trash = game.Stokkur()
    return tree, deck, trash

def initCards(backsideImage):
    # Card placement vectors
    firstRowWidth = [WIDTH/2+x*CARDW/2.0 for x in [-7, -1, 5]]
    secondRowWidth = [WIDTH/2+x*CARDW for x in [-4, -3, -1, 0, 2, 3]]
    thirdRowWidth = [WIDTH/2+x*CARDW/2.0 for x in [-9, -7, -5, -3, -1, 1, 3, 5, 7]]
    fourthRowWidth = [WIDTH/2+x*CARDW for x in [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]]

    firstRowHeight = TOPMARGIN
    secondRowHeight = TOPMARGIN+CARDH/2
    thirdRowHeight = TOPMARGIN+CARDH
    fourthRowHeight = TOPMARGIN+3*CARDH/2

    cards = {10: [Rect(firstRowWidth[0], firstRowHeight, CARDW, CARDH), backsideImage, 0],
             20: [Rect(firstRowWidth[1], firstRowHeight, CARDW, CARDH), backsideImage, 0],
             30: [Rect(firstRowWidth[2], firstRowHeight, CARDW, CARDH), backsideImage, 0],
             11: [Rect(secondRowWidth[0], secondRowHeight, CARDW, CARDH), backsideImage, 0],
             12: [Rect(secondRowWidth[1], secondRowHeight, CARDW, CARDH), backsideImage, 0],
             21: [Rect(secondRowWidth[2], secondRowHeight, CARDW, CARDH), backsideImage, 0],
             22: [Rect(secondRowWidth[3], secondRowHeight, CARDW, CARDH), backsideImage, 0],
             31: [Rect(secondRowWidth[4], secondRowHeight, CARDW, CARDH), backsideImage, 0],
             32: [Rect(secondRowWidth[5], secondRowHeight, CARDW, CARDH), backsideImage, 0],
             13: [Rect(thirdRowWidth[0], thirdRowHeight, CARDW, CARDH), backsideImage, 0],
             14: [Rect(thirdRowWidth[1], thirdRowHeight, CARDW, CARDH), backsideImage, 0],
             15: [Rect(thirdRowWidth[2], thirdRowHeight, CARDW, CARDH), backsideImage, 0],
             23: [Rect(thirdRowWidth[3], thirdRowHeight, CARDW, CARDH), backsideImage, 0],
             24: [Rect(thirdRowWidth[4], thirdRowHeight, CARDW, CARDH), backsideImage, 0],
             25: [Rect(thirdRowWidth[5], thirdRowHeight, CARDW, CARDH), backsideImage, 0],
             33: [Rect(thirdRowWidth[6], thirdRowHeight, CARDW, CARDH), backsideImage, 0],
             34: [Rect(thirdRowWidth[7], thirdRowHeight, CARDW, CARDH), backsideImage, 0],
             35: [Rect(thirdRowWidth[8], thirdRowHeight, CARDW, CARDH), backsideImage, 0],
             16: [Rect(fourthRowWidth[0], fourthRowHeight, CARDW, CARDH), backsideImage, 0],
             17: [Rect(fourthRowWidth[1], fourthRowHeight, CARDW, CARDH), backsideImage, 0],
             18: [Rect(fourthRowWidth[2], fourthRowHeight, CARDW, CARDH), backsideImage, 0],
             26: [Rect(fourthRowWidth[3], fourthRowHeight, CARDW, CARDH), backsideImage, 0],
             27: [Rect(fourthRowWidth[4], fourthRowHeight, CARDW, CARDH), backsideImage, 0],
             28: [Rect(fourthRowWidth[5], fourthRowHeight, CARDW, CARDH), backsideImage, 0],
             36: [Rect(fourthRowWidth[6], fourthRowHeight, CARDW, CARDH), backsideImage, 0],
             37: [Rect(fourthRowWidth[7], fourthRowHeight, CARDW, CARDH), backsideImage, 0],
             38: [Rect(fourthRowWidth[8], fourthRowHeight, CARDW, CARDH), backsideImage, 0],
             39: [Rect(fourthRowWidth[9], fourthRowHeight, CARDW, CARDH), backsideImage, 0],
             }
    return cards

def nextCardIsValid(next, current):
    if abs(next-current) is 1 or (max(next, current) is 13 and min(next, current) is 1):
        return True
    return False

def checkCard(tree, trash, cards, rects, rect):
    for card in cards:
        if rect is cards[card][0] and nextCardIsValid(int(str(trash.get_copy()[-1])[1:]), cards[card][2]):
            number = cards[card][2]
            removeables = tree.get_removeables().get_copy()
            for rmv in removeables:
                if str(rmv)[1:] == str(number):
                    trash.add(rmv)
                    tree.update_tree(rmv)
                    break
            rects.remove(cards[card][0])
            del[cards[card]]
            break

def refreshCards(tree, cards):
    removeables = tree.get_removeables()
    bla = []
    for i in removeables.stokkur:
        bla.append(tree.card_pos(i))
    bla.sort()
    print bla

    while removeables.has_next():
        tmp = removeables.get_next()
        pos = int(tree.card_pos(tmp))
        if pos in cards:
            cards[pos][2] = int(str(tmp)[1:])
            cards[pos][1] = loadCardImage(str(tmp))

def drawCard(deck, trash):
    trash.add(deck.get_next())

def loseCondition(tree, deck):
    if tree.get_removeables() != [] and deck.count() is 0:
        return True
    return False

def winCondition(tree):
    if tree.get_removeables() == []:
        return True
    return False

def main():
    screen, background, font = initPygame(WIDTH, HEIGHT)
    tree, deck, trash = initTriPeaks()
    lostGame = False
    deckRect = Rect(DECKLOCATION[0], DECKLOCATION[1], CARDW, CARDH)
    
    # Set background
    screen.blit(background, (0, 0))
    pygame.display.flip()

    backsideImage = loadCardImage("deck")
    cards = initCards(backsideImage)
    rects = []
    for card in cards:
        rects.append(cards[card][0])
    
    trash.add(deck.get_next())
    refreshCards(tree, cards)

    clock = pygame.time.Clock()

    while 1:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == MOUSEBUTTONDOWN:
                for rect in rects:
                    if rect.collidepoint(mouse.get_pos()):
                        checkCard(tree, trash, cards, rects, rect)
                        refreshCards(tree, cards)
                        print len(cards)
                if deckRect.collidepoint(mouse.get_pos()):
                    if loseCondition(tree, deck):
                        lostGame = True
                        break
                    drawCard(deck, trash)
                    refreshCards(tree, cards)
        if lostGame:
            while(True):
                for event in pygame.event.get():
                    if event.type == QUIT:
                        return
                            
        screen.blit(background, (0, 0))

        screen.blit(backsideImage, DECKLOCATION)
        cardsLeft = font.render(str(deck.count()), 0, (0, 0, 0))
        screen.blit(cardsLeft, DECFONTLOCATION)
        trashTop = trash.peek()
        screen.blit(loadCardImage(trashTop), TRASHLOCATION)
        for card in cards:
            screen.blit(cards[card][1], cards[card][0].topleft)

        pygame.display.flip()

        if winCondition(tree):
            print "JEI"


if __name__ == '__main__':
    main()