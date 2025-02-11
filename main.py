import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (800, 600)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("pokemon")

# Set the background color (R, G, B)
background_color = (0, 0, 0)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the window with the background color
    window.fill(background_color)
    
    # Update the display
    pygame.display.flip()
