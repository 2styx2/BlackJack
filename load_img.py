import pygame, sys

suits = ['C', 'D', 'H', 'S']
picture_cards = ['A', 'J', 'K', 'Q']
deck = [[],[],[],[]]

def set_img(path):
    for suit in suits:
        for i in range(2, 11):
            img_loc = path + '/' + str(i) + suit + '.png'
            img = pygame.image.load(img_loc).convert()
            deck[suits.index(suit)].append(img)
        for pic in picture_cards:
            img_loc = path + '/' + pic + suit + '.png'
            img = pygame.image.load(img_loc).convert()
            deck[suits.index(suit)].append(img)
    return deck
