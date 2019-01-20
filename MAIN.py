import pygame
import math

pygame.init()
screenDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

while True:
    if event.type == pygame.QUIT:
            pygame.mouse.set_visible(False)
            pygame.quit()
            quit()
    screenDisplay.fill((255,0,0))
    pygame.display.update()
    clock.tick(60)
