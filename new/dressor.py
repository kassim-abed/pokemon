import pygame, sys
pygame.init()

from button import Button


window = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Menu")

background = pygame.image.load("image/backgroundresize.jpg").convert()


text_fight = Button ((300, 250), "image/text_fight.jpg")
text_pokedex = Button ((300, 400), "image/text_pokedex.jpg")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if text_fight.is_pressed():
        print("Start Button pressed")

    if text_pokedex.is_pressed():
        pygame.quit()
        sys.exit()

    window.fill("black")
    window.blit(background, (0,0))
    text_fight.draw(window)
    text_pokedex.draw(window)
    logo.draw(window)

    pygame.display.flip()
    clock.tick(60)