import pygame, sys
pygame.init()

from button import Button


window = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Menu")

background = pygame.image.load("image/backgroundresize.jpg").convert()


save_button = Button ("image/text_ng.jpg", (300, 250))
load_button = Button ("image/text_lg.jpg", (300, 400))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if save_button.is_pressed():
        print("Start Button pressed")

    if load_button.is_pressed():
        pygame.quit()
        sys.exit()

    window.fill("black")
    window.blit(background, (0,0))
    save_button.draw(window)
    load_button.draw(window)
    logo.draw(window)

    pygame.display.flip()
    clock.tick(60)