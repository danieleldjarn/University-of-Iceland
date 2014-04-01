import pygame
from pygame.locals import *
import pygame.mouse as mouse
import Kapall_klasi as game

WIDTH, HEIGHT = 800, 600
CARDW, CARDH = 72, 96

def loadCardImage(name):
    path = "cards/"+str(name)+'.png'
    try:
        image = pygame.image.load(path)
    except pygame.error, message:
        raise SystemExit, message
    image = image.convert()
    return image, image.get_rect()

def initPygame(width, height):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Tri Peaks")
    pygame.mouse.set_visible(1)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((1, 83, 9))
    return screen, background

def initTriPeaks():
    tree = game.Tree()
    deck = game.Stokkur()
    deck.nyr_random_stokkur()
    tree.make_tree(deck)
    trash = game.Stokkur()
    return tree, deck, trash

def main():
    screen, background = initPygame(WIDTH, HEIGHT)
    tree, deck, trash = initTriPeaks()

    screen.blit(background, (0, 0))
    pygame.display.flip()
    trash.add(deck.get_next())
    print str(trash.stokkur[-1])
    img, imgRect = loadCardImage(str(trash.stokkur[-1]))
    imgRect.topleft = 20, 10

    img2, imgRect2 = loadCardImage("deck")
    imgRect2.topleft = 20, 100

    rects = [imgRect, imgRect2]

    clock = pygame.time.Clock()

    xCoordinate = 20
    direction = "left"
    while 1:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == MOUSEBUTTONDOWN:
                for rect in rects:
                    if rect.collidepoint(mouse.get_pos()):
                        print("You clicked on {}".format(rect))
                print "mbdwn"

        # if xCoordinate > 400:
        #     direction = "right"
        # elif xCoordinate < 0:
        #     direction = "left"

        # if direction == "left":
        #     xCoordinate += 2
        # else:
        #     xCoordinate -= 2

        screen.blit(background, (0, 0))
        screen.blit(img, (xCoordinate, 10))
        screen.blit(img2, (WIDTH/2-7*CARDW/2, 10))
        screen.blit(img2, (WIDTH/2-CARDW/2, 10))
        screen.blit(img2, (WIDTH/2+5*CARDW/2, 10))

        screen.blit(img2, (WIDTH/2-4*CARDW, 10+CARDH/2))
        screen.blit(img2, (WIDTH/2-3*CARDW, 10+CARDH/2))
        screen.blit(img2, (WIDTH/2-CARDW, 10+CARDH/2))
        screen.blit(img2, (WIDTH/2, 10+CARDH/2))
        screen.blit(img2, (WIDTH/2+2*CARDW, 10+CARDH/2))
        screen.blit(img2, (WIDTH/2+3*CARDW, 10+CARDH/2))

        screen.blit(img2, (WIDTH/2-9*CARDW/2, 10+CARDH))
        screen.blit(img2, (WIDTH/2-7*CARDW/2, 10+CARDH))
        screen.blit(img2, (WIDTH/2-5*CARDW/2, 10+CARDH))
        screen.blit(img2, (WIDTH/2-3*CARDW/2, 10+CARDH))
        screen.blit(img2, (WIDTH/2-CARDW/2, 10+CARDH))
        screen.blit(img2, (WIDTH/2+CARDW/2, 10+CARDH))
        screen.blit(img2, (WIDTH/2+3*CARDW/2, 10+CARDH))
        screen.blit(img2, (WIDTH/2+5*CARDW/2, 10+CARDH))
        screen.blit(img2, (WIDTH/2+7*CARDW/2, 10+CARDH))

        screen.blit(img2, (WIDTH/2-9*CARDW/2, 10+3*CARDH/2))


        pygame.display.flip()


if __name__ == '__main__':
    main()