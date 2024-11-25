# Authors: Joshua R., Grant S.
# Last Updated: 11-11
# Description: Holds functions for displaying UI elements.

import pygame
from Map import Map
from Player import Player

# hp display function
# inventory display?

MINIMAP_XSIZE = 160
MINIMAP_XPOS = 395
MINIMAP_YSIZE = 160
MINIMAP_YPOS = 60

def drawMiniMap(mapObject, playerObject, screen):
    """
    Draws minimap visuals based on player location and map tiles.
    :param mapObject: Map object (for tiletypes).
    :param playerObject: Player object (for facing and coords).
    :param screen: Display to draw onto.
    """
    pygame.draw.rect(screen, "red", pygame.Rect(MINIMAP_XPOS, MINIMAP_YPOS, MINIMAP_XSIZE, MINIMAP_YSIZE))
    if isinstance(mapObject,Map):
        mapLayoutArray = mapObject.getLayout()
        mapSize = mapLayoutArray.shape
        xSize = MINIMAP_XSIZE / mapSize[1]
        ySize = MINIMAP_YSIZE / mapSize[0]
        for i in range(mapSize[1]):
            for j in range(mapSize[0]):
                xPos = MINIMAP_XPOS+xSize*i
                yPos = MINIMAP_YPOS+ySize*j
                rect = pygame.Rect(xPos,yPos,xSize,ySize)
                if mapLayoutArray[j][i] == 0:
                    pygame.draw.rect(screen, "black", rect)
                else:
                    pygame.draw.rect(screen, "blue", rect)
    # now, draw player
        playerPosition = playerObject.GetPosition()
        facing = playerObject.GetFacing()
        playerX = (playerPosition[1]+.5)*xSize + MINIMAP_XPOS
        playerY = (playerPosition[0]+.5)*ySize + MINIMAP_YPOS
        pygame.draw.circle(screen, "green", (playerX,playerY), xSize/2)
        if facing == 0:
            pygame.draw.polygon(screen, "black", ((playerX,playerY - ySize/4), (playerX - xSize/4,playerY + ySize/4), (playerX + xSize/4,playerY + ySize/4)))
        elif facing == 1:
            pygame.draw.polygon(screen, "black", ((playerX + xSize/4,playerY), (playerX - xSize/4,playerY + ySize/4), (playerX - xSize/4,playerY - ySize/4)))
        elif facing == 2:
            pygame.draw.polygon(screen, "black", ((playerX,playerY + ySize/4), (playerX - xSize/4,playerY - ySize/4), (playerX + xSize/4,playerY - ySize/4)))
        elif facing == 3:
            pygame.draw.polygon(screen, "black", ((playerX - xSize/4,playerY), (playerX + xSize/4,playerY + ySize/4), (playerX + xSize/4,playerY - ySize/4)))
    return

VIEWPORT_XSIZE = 280
VIEWPORT_YSIZE = 240

def drawViewport(mapObject,playerObject,screen):
    """
    Draws viewport visuals based on player location and map tiles.
    :param mapObject: Map object (for tiletypes).
    :param playerObject: Player object (for facing and coords).
    :param screen: Display to draw onto.
    """
    # idea - grab tile type of current position and player facing to deduce visuals
    mapLayoutArray = mapObject.getLayout()
    playerFacing = playerObject.GetFacing()
    playerCoords = playerObject.GetPosition()
    # background fill
    pygame.draw.rect(screen, "black", pygame.Rect(60, 60, VIEWPORT_XSIZE, VIEWPORT_YSIZE))
    roomFloor = pygame.image.load('img/roomFloor.png').convert()
    screen.blit(roomFloor,(60,60))
    roomForward = pygame.image.load('img/roomForward.png').convert()
    roomLeft = pygame.image.load('img/roomLeft.png').convert()
    roomRight = pygame.image.load('img/roomRight.png').convert()
    # position is [y,x]
    try:
        if playerFacing == 0:
            if not (playerCoords[0]-1 >= 0 and mapLayoutArray[playerCoords[0]-1,playerCoords[1]] != 0):
                screen.blit(roomForward, (60, 60))
            if not (playerCoords[1] - 1 >= 0 and mapLayoutArray[playerCoords[0], playerCoords[1]-1] != 0):
                screen.blit(roomLeft, (60, 60))
            if not (mapLayoutArray[playerCoords[0], playerCoords[1]+1] != 0):
                screen.blit(roomRight, (60, 60))
            return
        elif playerFacing == 1:
            if not (mapLayoutArray[playerCoords[0],playerCoords[1]+1] != 0):
                screen.blit(roomForward, (60, 60))
            if not (playerCoords[0] - 1 >= 0 and mapLayoutArray[playerCoords[0]-1, playerCoords[1]] != 0):
                screen.blit(roomLeft, (60, 60))
            if not (mapLayoutArray[playerCoords[0]+1, playerCoords[1]] != 0):
                screen.blit(roomRight, (60, 60))
            return
        elif playerFacing == 2:
            if not (mapLayoutArray[playerCoords[0]+1,playerCoords[1]] != 0):
                screen.blit(roomForward, (60, 60))
            if not (mapLayoutArray[playerCoords[0], playerCoords[1]+1] != 0):
                screen.blit(roomLeft, (60, 60))
            if not (playerCoords[1] - 1 >= 0 and mapLayoutArray[playerCoords[0], playerCoords[1]-1] != 0):
                screen.blit(roomRight, (60, 60))
            return
        elif playerFacing == 3:
            if not (playerCoords[1]-1 >= 0 and mapLayoutArray[playerCoords[0],playerCoords[1]-1] != 0):
                screen.blit(roomForward, (60, 60))
            if not (mapLayoutArray[playerCoords[0]+1, playerCoords[1]] != 0):
                screen.blit(roomLeft, (60, 60))
            if not (playerCoords[0] - 1 >= 0 and mapLayoutArray[playerCoords[0]-1, playerCoords[1]] != 0):
                screen.blit(roomRight, (60, 60))
            return
    except IndexError:
        return
        #pygame.draw.rect(screen, "black", pygame.Rect(60, 60, VIEWPORT_XSIZE, VIEWPORT_YSIZE))
    else:
        return

# deprecated variable
BUTTON_SIZE = 48
def drawButtons(screen):
    """
    Draws movement buttons.
    :param screen: Display to draw onto.
    """
    lTurnButton = pygame.image.load('img/buttonLTurn.png').convert()
    screen.blit(lTurnButton,(400,250))
    upButton = pygame.image.load('img/buttonUp.png').convert()
    screen.blit(upButton,(450,250))
    rTurnButton = pygame.image.load('img/buttonRTurn.png').convert()
    screen.blit(rTurnButton,(500,250))
    leftButton = pygame.image.load('img/buttonLeft.png').convert()
    screen.blit(leftButton,(400,300))
    downButton = pygame.image.load('img/buttonDown.png').convert()
    screen.blit(downButton,(450,300))
    rightButton = pygame.image.load('img/buttonRight.png').convert()
    screen.blit(rightButton,(500,300))
    return