#!/usr/bin/env python3
import math
import time
import random
from contextlib import redirect_stdout
with redirect_stdout(None): import pygame # No console message

# Setup
pygame.init()
screenDisplay = pygame.display.set_mode((800,600))
#pygame.mouse.set_visible(False)
pygame.display.set_caption("blah")
clock = pygame.time.Clock()
loadImage = pygame.image.load

# Globaling
global coins

# Data
coins = 0
F_inventory = ['cannonball', 'birb', 'monkey'] # Items must be lower

def menu():
    # Display Assets
    screenDisplay.fill((154, 219, 235))
    screenDisplay.blit(loadImage('menuAssets/playButton.png'), (275, 255))
    screenDisplay.blit(loadImage('menuAssets/optionsButton.png'), (275, 377))
    screenDisplay.blit(loadImage('menuAssets/quitButton.png'), (275, 500))

    """Add code"""

def battleScreen():
    # Display Assets
    screenDisplay.blit(loadImage('fightAssets/background.png'), (0, 0))
    screenDisplay.blit(loadImage('fightAssets/friendlyShip.png'), (50, 250))
    screenDisplay.blit(loadImage('fightAssets/enemyShip.png'), (585, 250))

    slots_drawn = 0
    for item in F_inventory:
        slots_drawn += 1
        screenDisplay.blit(loadImage(f'fightAssets/INV_{item}.png'), (30 * slots_drawn + 50 * slots_drawn, 515))


# Game loop
while True:
    print(pygame.mouse.get_pos())
    #screenDisplay.blit(loadImage('assets/mouse.png'), pygame.mouse.get_pos()) # Custom mouse cursor
    for event in pygame.event.get(): # Events
        if event.type == pygame.QUIT:
            pygame.mouse.set_visible(True)
            pygame.quit()
            quit()

    menu()
    #battleScreen()

    pygame.display.update()
    clock.tick(60)
