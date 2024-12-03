# Authors: Joshua R., Grant S.
# Last Updated: 12-2
# Description: Holds functions for combat interactions.

import pygame

def treasurePlaceholder(screen):
    roomImage = pygame.image.load('img/treasureImage.png').convert()
    screen.blit(roomImage, (102, 102))

    #if player does thing:
        #player.setClearedTrue()
        #roomData[playerCoords[0]][playerCoords[1]].cleared()

    #^^^ needs every function to intake player object and roomdata object, which already exist in main!!!