#!/usr/bin/env python3
import math
import time
import random
import contextlib
with contextlib.redirect_stdout(None): import pygame # No console message

# Setup
pygame.init()
screenDisplay = pygame.display.set_mode((800,600))
#pygame.mouse.set_visible(False)
pygame.display.set_caption("blah")
clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get(): # Events
        if event.type == pygame.QUIT:
            pygame.mouse.set_visible(True)
            pygame.quit()
            quit()

    screenDisplay.fill((154, 219, 235))
    screenDisplay.blit(pygame.image.load('menuAssets/playButton.png'), (275, 255))
    screenDisplay.blit(pygame.image.load('menuAssets/optionsButton.png'), (275, 377))
    screenDisplay.blit(pygame.image.load('menuAssets/quitButton.png'), (275, 500))
    pygame.display.update()
    clock.tick(60)
