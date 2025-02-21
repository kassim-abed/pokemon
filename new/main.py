import pygame, sys
pygame.init()

from button import Button


window = pygame.display.set_mode((600,600))
pygame.display.set_caption("Menu")

background = pygame.image.load("image/backgroundresize.jpg").convert()


start_button = Button((200, 200),"image/text_play.png" )
exit_button = Button((300, 400), "image/text_quit.png" )


clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if start_button.is_pressed():
        print("Start Button pressed")

    if exit_button.is_pressed():
        pygame.quit()
        sys.exit()

    window.fill("black")
    window.blit(background, (0,0))
    start_button.draw(window)
    exit_button.draw(window)
    pygame.display.update() 
    #pygame.display.flip()
    clock.tick(60)