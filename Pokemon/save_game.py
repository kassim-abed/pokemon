import pygame
pygame.init()
import json

###############################################

# Sample game data
game_data = {
    'player_name': 'Player1',
    'level': 2
}

# Save data to slot 1
def save_game(slot):
    filename = f'savegame_slot{slot}.json'
    with open(filename, 'w') as f:
        json.dump(game_data, f)
    print(f"Game data saved in slot {slot}.")

# Save in different slots
save_game(1)
save_game(2)
save_game(3)

###############################################

# Load data from a specific slot
def load_game(slot):
    filename = f'savegame_slot{slot}.json'
    with open(filename, 'r') as f:
        game_data = json.load(f)
    print(f"Loaded game data from slot {slot}: {game_data}")

# Load from different slots
load_game(1)
load_game(2)
load_game(3)

###############################################