import pygame
pygame.init()
from save_game import game_data, save_game, load_game

###############################################


logo = pygame.image.load('image/logo.jpg')


def main_menu():
    pygame.display.set_caption("Menu")



class Main_Menu:

    def __init__(self, new_game, load_save, quit):

        self.new_game = new_game
        self.load_save = load_save
        self.quit = quit

    def new_game(self):
        save_game()
        return self.new_game
    
    def load_save(self):
        load_game()
        return self.new_game
    
    def quit(self):
        return self.quit
    

class Button:
    def __init__ (self):
        self.image = pygame.image.load('image/textblock.jpg').convert_alpha()
        self.rect = self.image.get_rect()

    def draw(self, window):
        window.blit(self.image, self.rect)