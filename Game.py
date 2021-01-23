import pygame, sys

WIDTH, HEIGHT = 800, 800
FPS = 60
GREEN = (34,139,34)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Blackjack')
pygame.init()
card = pygame.image.load(r'C:\Users\Styx2244\Desktop\BlackJack\Cards\2C.png')
cardlo = [50,50]

def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        screen.fill(GREEN)
        screen.blit(card,cardlo)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()
main()
