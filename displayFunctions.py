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
    # position is [y,x]
    # current quirk - at left/upper edge, draw based on other side
    try:
        if playerFacing == 0:
            if playerCoords[0]-1 < 0 or mapLayoutArray[playerCoords[0]-1,playerCoords[1]] == 0:
                pygame.draw.rect(screen, "black", pygame.Rect(60, 60, VIEWPORT_XSIZE, VIEWPORT_YSIZE))
            else:
                pygame.draw.rect(screen, "grey", pygame.Rect(60, 60, VIEWPORT_XSIZE, VIEWPORT_YSIZE))
            return
        elif playerFacing == 1:
            if mapLayoutArray[playerCoords[0],playerCoords[1]+1] == 0:
                pygame.draw.rect(screen, "black", pygame.Rect(60, 60, VIEWPORT_XSIZE, VIEWPORT_YSIZE))
            else:
                pygame.draw.rect(screen, "grey", pygame.Rect(60, 60, VIEWPORT_XSIZE, VIEWPORT_YSIZE))
            return
        elif playerFacing == 2:
            if mapLayoutArray[playerCoords[0]+1,playerCoords[1]] == 0:
                pygame.draw.rect(screen, "black", pygame.Rect(60, 60, VIEWPORT_XSIZE, VIEWPORT_YSIZE))
            else:
                pygame.draw.rect(screen, "grey", pygame.Rect(60, 60, VIEWPORT_XSIZE, VIEWPORT_YSIZE))
            return
        elif playerFacing == 3:
            if playerCoords[1]-1 < 0 or mapLayoutArray[playerCoords[0],playerCoords[1]-1] == 0:
                pygame.draw.rect(screen, "black", pygame.Rect(60, 60, VIEWPORT_XSIZE, VIEWPORT_YSIZE))
            else:
                pygame.draw.rect(screen, "grey", pygame.Rect(60, 60, VIEWPORT_XSIZE, VIEWPORT_YSIZE))
            return
    except IndexError:
        pygame.draw.rect(screen, "black", pygame.Rect(60, 60, VIEWPORT_XSIZE, VIEWPORT_YSIZE))
    else:
        return

BUTTON_SIZE = 48
def drawButtons(screen):
    """
    Draws movement buttons.
    :param screen: Display to draw onto.
    """
    pygame.draw.rect(screen, "blue", pygame.Rect(400, 250, BUTTON_SIZE, BUTTON_SIZE))
    pygame.draw.rect(screen, "blue", pygame.Rect(450, 250, BUTTON_SIZE, BUTTON_SIZE))
    pygame.draw.rect(screen, "blue", pygame.Rect(500, 250, BUTTON_SIZE, BUTTON_SIZE))
    pygame.draw.rect(screen, "blue", pygame.Rect(400, 300, BUTTON_SIZE, BUTTON_SIZE))
    pygame.draw.rect(screen, "blue", pygame.Rect(450, 300, BUTTON_SIZE, BUTTON_SIZE))
    pygame.draw.rect(screen, "blue", pygame.Rect(500, 300, BUTTON_SIZE, BUTTON_SIZE))
    return