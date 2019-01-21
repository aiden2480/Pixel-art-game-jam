import math
import time
import random
from contextlib import redirect_stdout

with redirect_stdout(None):
    import pygame  # No console message

# Init
displayWidth, displayHeight = 800, 600
pygame.init()
screenDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()
loadImage = pygame.image.load

# Variables
gameState = "Menu"
MAP = MENU = F = {}
Keys = {"W": False, "A": False, "S": False, "D": False, "E": False}

# Areas
MAP["AreaSize"] = [displayWidth * 5, displayHeight * 5]
MAP["PlayerPos"] = [MAP["AreaSize"][0] / 2, MAP["AreaSize"][0] / 2]
MAP["PlayerDir"] = 0
MAP["ShipDrawPos"] = [displayWidth / 2, displayHeight / 2]
MAP["ActualDrawShip"] = MAP["ShipDrawPos"][:]

# Loading Sprites/images
ships = [
    loadImage("mapAssets/shipL.png"),
    loadImage("mapAssets/shipUL.png"),
    loadImage("mapAssets/shipU.png"),
    None,
    loadImage("mapAssets/shipR.png"),
    None,
    loadImage("mapAssets/shipD.png"),
    None,
]

MENU["ButtonPlay"] = loadImage("menuAssets/playButton.png")
MENU["ButtonOptions"] = loadImage("menuAssets/optionsButton.png")
MENU["ButtonQuit"] = loadImage("menuAssets/quitButton.png")

# Surfaces
MAP["MainSurf"] = pygame.Surface(MAP["AreaSize"])  # is shifted

# GAME STATES (Functions)
def map():
    global MAP
    
    MAP["MainSurf"].fill((0, 0, 200))
    pygame.draw.line(MAP["MainSurf"], (0, 0, 0), (0, 0), (MAP["AreaSize"][0], MAP["AreaSize"][1]))
    pygame.draw.line(MAP["MainSurf"], (0, 0, 0), (MAP["AreaSize"][0], 0), (0, MAP["AreaSize"][1]))
    if Keys["W"] == True:
        MAP["PlayerPos"][1] -= frameTime * 100
        MAP["PlayerDir"] = 2
        MAP["ShipDrawPos"][1] = displayHeight * 0.46

    if Keys["A"] == True:
        MAP["PlayerPos"][0] -= frameTime * 100
        MAP["PlayerDir"] = 0
        MAP["ShipDrawPos"][0] = displayWidth * 0.46

    if Keys["S"] == True:
        MAP["PlayerPos"][1] += frameTime * 100
        MAP["PlayerDir"] = 2  # 6
        MAP["ShipDrawPos"][1] = displayHeight * 0.54

    if Keys["D"] == True:
        MAP["PlayerPos"][0] += frameTime * 100
        MAP["PlayerDir"] = 0  # 4
        MAP["ShipDrawPos"][0] = displayWidth * 0.54

    if Keys["W"] == False and Keys["S"] == False:
        MAP["ShipDrawPos"][1] = displayHeight * 0.5

    if Keys["A"] == False and Keys["D"] == False:
        MAP["ShipDrawPos"][0] = displayWidth * 0.5

    screenDisplay.blit(MAP["MainSurf"], [-MAP["PlayerPos"][0], -MAP["PlayerPos"][1]])
    drawShip = ships[MAP["PlayerDir"]]
    MAP["ActualDrawShip"] = [
        (MAP["ActualDrawShip"][0] + MAP["ShipDrawPos"][0] + MAP["ShipDrawPos"][0]) / 3,
        (MAP["ActualDrawShip"][1] + MAP["ShipDrawPos"][1] + MAP["ShipDrawPos"][1]) / 3,
    ]
    screenDisplay.blit(drawShip, MAP["ActualDrawShip"])


def menu():
    # Display Assets
    screenDisplay.fill((154, 219, 235))
    playButton = screenDisplay.blit(MENU["ButtonPlay"], (275, 255))
    optionsButton = screenDisplay.blit(MENU["ButtonOptions"], (275, 377))
    quitButton = screenDisplay.blit(MENU["ButtonQuit"], (275, 500))

    """Add code"""
    if playButton.collidepoint(mousePos[0], mousePos[1]) and mouseButtons[0]:
        gameState = "Map"
    if optionsButton.collidepoint(mousePos[0], mousePos[1]) and mouseButtons[0]:
        gameState = "Options"
    if quitButton.collidepoint(mousePos[0], mousePos[1]) and mouseButtons[0]:
        pygame.mouse.set_visible(True)
        pygame.quit()
        quit()
    


def battleScreen():
    # Display Assets
    screenDisplay.blit(loadImage("fightAssets/background.png"), (0, 0))
    screenDisplay.blit(loadImage("fightAssets/friendlyShip.png"), (50, 250))
    screenDisplay.blit(loadImage("fightAssets/enemyShip.png"), (585, 250))

    slots_drawn = 0
    for item in F["inventory"]:
        slots_drawn += 1
        screenDisplay.blit(
            loadImage(f"fightAssets/INV_{item}.png"),
            (30 * slots_drawn + 50 * slots_drawn, 515))

    """Behaviorial script"""


def cutScene():
    pass


### Other funtions ###

# Main Loop
while True:
    startFrame = time.time()
    screenDisplay.fill((0, 0, 0))
    mouseButtons = pygame.mouse.get_pressed()  # (left mouse button, middle, right)
    mousePos = pygame.mouse.get_pos()  # (x, y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mouse.set_visible(True)
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Keys["W"] = True
            if event.key == pygame.K_a:
                Keys["A"] = True
            if event.key == pygame.K_s:
                Keys["S"] = True
            if event.key == pygame.K_d:
                Keys["D"] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                Keys["W"] = False
            if event.key == pygame.K_a:
                Keys["A"] = False
            if event.key == pygame.K_s:
                Keys["S"] = False
            if event.key == pygame.K_d:
                Keys["D"] = False

    menu()

    pygame.display.update()
    clock.tick(60)
    frameTime = time.time() - startFrame