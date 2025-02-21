import pygame
pygame.init()
import sys
from main_menu import Button


#Screen Menu

pygame.display.set_caption("Menu")

screen = pygame.display.set_mode((1280,720))
background = pygame.image.load('image/backgroundresize.jpg').convert()
start_button = Button('image/textblock.jpg')




screen.fill("black")
screen.blit(background, (0,0))
start_button.draw(screen)

font = pygame.font.Font(None , 60)
menu_mouse_pos = pygame.mouse.get_pos()














#########################################################

