# Authors: Joshua R., Grant S.
# Last Updated: 12-3
# Description: Holds functions for puzzle interactions.

import pygame
import random

def puzzlePlaceholder(screen):
    roomImage = pygame.image.load('img/puzzleImage.png').convert()
    screen.blit(roomImage, (102, 102))

    #if player does thing:
        #player.setClearedTrue()
        #roomData[playerCoords[0]][playerCoords[1]].cleared()

    #^^^ needs every function to intake player object and roomdata object, which already exist in main!!!

def buttonInit():
    r = random.randint(1, 6)
    return r

def buttonPuzzle(screen,r):

    #Tablet import
    tablet = pygame.image.load('img/puzzleTablet.png').convert()
    tablet.set_colorkey((255,255,255))
    screen.blit(tablet,(116,150))

    #r = random.randint(1, 6)
    #Random sequence selection
    if r == 1:
        colorSequence = ['Red','Blue','Green']
    elif r == 2:
        colorSequence = ['Red','Green','Blue']
    elif r == 3:
        colorSequence = ['Blue','Red','Green']
    elif r == 4:
        colorSequence = ['Blue','Green','Red']
    elif r == 5:
        colorSequence = ['Green','Red','Blue']
    elif r == 6:
        colorSequence = ['Green','Blue','Red']


    #key1
    pygame.draw.circle(screen, colorSequence[0], (150, 200), 11)
    #Outline and Red button
    pygame.draw.circle(screen, "Black", (150, 200), 10)
    pygame.draw.circle(screen, "Red", (150,200), 8)

    #key2
    pygame.draw.circle(screen, colorSequence[1], (200, 200), 11)
    #Outline and Green button
    pygame.draw.circle(screen, "Black", (200, 200), 10)
    pygame.draw.circle(screen, "Green", (200, 200), 8)

    #key3
    pygame.draw.circle(screen, colorSequence[2], (250, 200), 11)
    #Outline and Blue button
    pygame.draw.circle(screen, "Black", (250, 200), 10)
    pygame.draw.circle(screen, "Blue", (250, 200), 8)

    #Need logic to determine how the game will "pause" in the event of a puzzle
    #Need logic to determine which color sequence, and then test for player clicks in the correct order (i.e buttons don't work until player presses previous)
    #Upon player button press, we need to take the playerCoords index, and pass that into the roomData object to trigger an isclear for the room which will unpause game
    #I.e^ roomData[playerCoords[0]][playerCoords[1]].isClear()
