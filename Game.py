import pygame, sys
from load_img import *
from pygame.locals import *
WIDTH, HEIGHT = 800, 800
FPS = 60
GREEN = (34,139,34)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Blackjack')
pygame.init()
# card = pygame.image.load(r'Cards\5S.png')
# cardlo = [0,50]


set_img('Cards')
# for suits in deck:
#     for card in suits:
#         card = pygame.image.load(r + card)
def load_card_img(x, y):
    screen.blit(deck[x][y],loc)

clicking = False
right_clicking = False
def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        screen.fill(GREEN)
        mx, my = pygame.mouse.get_pos()
        rot = 0
        loc = [mx, my]
        #screen.blit(pygame.transform.rotate(deck[0][0],rot), (loc[0],loc[1]))


        #load_card_img(3,12)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    screen.blit(pygame.transform.rotate(deck[1][0],rot), (loc[0],loc[1]))
                    clicking = True
                if event.button == 3:
                    right_clicking = True


        pygame.display.update()

    pygame.quit()
main()
