# Authors: Joshua R., Grant S.
# Last Updated: 12-2
# Description: Holds functions for displaying UI elements.

import pygame
from Map import Map
from Player import Player
from Room import Room

# inventory display?

MINIMAP_XSIZE = 160
MINIMAP_XPOS = 395
MINIMAP_YSIZE = 160
MINIMAP_YPOS = 60

def drawWin(screen):
    """
    Draws victory message.
    :param screen: Screen to draw onto.
    """
    win = pygame.image.load('img/win.png').convert()
    win.set_colorkey((255, 255, 255))
    screen.blit(win, (116, 150))

def drawLose(screen):
    """
    Draws lose message.
    :param screen: Screen to draw onto.
    """
    lose = pygame.image.load('img/lose.png').convert()
    lose.set_colorkey((255, 255, 255))
    screen.blit(lose,(116,150))

def drawMiniMap(mapObject, playerObject, screen):
    """
    Draws minimap visuals based on player location and map tiles.
    :param mapObject: Map object (for tiletypes).
    :param playerObject: Player object (for facing and coords).
    :param screen: Display to draw onto.
    """
    pygame.draw.rect(screen, "red", pygame.Rect(MINIMAP_XPOS, MINIMAP_YPOS, MINIMAP_XSIZE, MINIMAP_YSIZE))
    if isinstance(mapObject,Map):
        roomData = mapObject.getRoomData()
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
                elif roomData[j][i].getisVisited() == False:
                    pygame.draw.rect(screen, "red", rect)
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
    roomData = mapObject.getRoomData()[playerCoords[0]][playerCoords[1]]
    if roomData.getisWood():
        roomFloor = pygame.image.load('img/roomFloorWood.png').convert()
        screen.blit(roomFloor,(60,60))
        roomForward = pygame.image.load('img/roomForwardWood.png').convert()
        roomLeft = pygame.image.load('img/roomLeftWood.png').convert()
        roomRight = pygame.image.load('img/roomRightWood.png').convert()
    elif roomData.getisStone():
        roomFloor = pygame.image.load('img/roomFloor.png').convert()
        screen.blit(roomFloor, (60, 60))
        roomForward = pygame.image.load('img/roomForward.png').convert()
        roomLeft = pygame.image.load('img/roomLeft.png').convert()
        roomRight = pygame.image.load('img/roomRight.png').convert()
    # position is [y,x]
    # draw walls
    try:
        if playerFacing == 0:
            if not (playerCoords[0]-1 >= 0 and mapLayoutArray[playerCoords[0]-1,playerCoords[1]] != 0):
                screen.blit(roomForward, (60, 60))
            if not (playerCoords[1] - 1 >= 0 and mapLayoutArray[playerCoords[0], playerCoords[1]-1] != 0):
                screen.blit(roomLeft, (60, 60))
            if not (mapLayoutArray[playerCoords[0], playerCoords[1]+1] != 0):
                screen.blit(roomRight, (60, 60))
        elif playerFacing == 1:
            if not (mapLayoutArray[playerCoords[0],playerCoords[1]+1] != 0):
                screen.blit(roomForward, (60, 60))
            if not (playerCoords[0] - 1 >= 0 and mapLayoutArray[playerCoords[0]-1, playerCoords[1]] != 0):
                screen.blit(roomLeft, (60, 60))
            if not (mapLayoutArray[playerCoords[0]+1, playerCoords[1]] != 0):
                screen.blit(roomRight, (60, 60))
        elif playerFacing == 2:
            if not (mapLayoutArray[playerCoords[0]+1,playerCoords[1]] != 0):
                screen.blit(roomForward, (60, 60))
            if not (mapLayoutArray[playerCoords[0], playerCoords[1]+1] != 0):
                screen.blit(roomLeft, (60, 60))
            if not (playerCoords[1] - 1 >= 0 and mapLayoutArray[playerCoords[0], playerCoords[1]-1] != 0):
                screen.blit(roomRight, (60, 60))
        elif playerFacing == 3:
            if not (playerCoords[1]-1 >= 0 and mapLayoutArray[playerCoords[0],playerCoords[1]-1] != 0):
                screen.blit(roomForward, (60, 60))
            if not (mapLayoutArray[playerCoords[0]+1, playerCoords[1]] != 0):
                screen.blit(roomLeft, (60, 60))
            if not (playerCoords[0] - 1 >= 0 and mapLayoutArray[playerCoords[0]-1, playerCoords[1]] != 0):
                screen.blit(roomRight, (60, 60))
    except IndexError:
        # pointless line to silence error
        silencer = True
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

def drawHealthBar(screen, player):
    """
    Draws healthbar onto screen.
    :param screen: Display to draw onto.
    """
    #Grabbing player current and max HP
    maxHealth = player.GetMaxHP()
    currentHealth = player.GetHP()

    #Calculating health ratio
    ratio = float(currentHealth/maxHealth)

    #Drawing gray (border) under red under green rect for hp bar, Formatted (X start, Y start, Length, Width)
    #Ratio Applied to green bar length
    #Making border yellow if player has armor
    if "Armor" in player.GetInventory():
        pygame.draw.rect(screen, "yellow", (60,325,280,35))
    else:
        pygame.draw.rect(screen, "gray", (60, 325, 280, 35))
    pygame.draw.rect(screen, "red", (90,330,250,25))
    pygame.draw.rect(screen, "green", (90,330,250 * ratio, 25))

    #Displaying text on health bar
    cHP = player.GetHP()
    mHP = player.GetMaxHP()
    Font = pygame.font.SysFont("Arial",26, True)
    hptext = Font.render(f"{cHP}/{mHP}", 1, 'black')
    screen.blit(hptext, (195,327))

    #Drawing health Icon
    healthIcon = pygame.image.load('img/HealthIcon.png').convert_alpha()
    screen.blit(healthIcon,(65,333))

    #Drawing Weapon Icon (if weapon)
    if "Sword" in player.GetInventory():
        s = pygame.image.load('img/weapon.png').convert()
        s.set_colorkey((255,255,255))
        screen.blit(s,(-60,300))