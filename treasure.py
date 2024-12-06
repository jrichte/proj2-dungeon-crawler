# Authors: Joshua R., Grant S.
# Last Updated: 12-2
# Description: Holds functions for combat interactions.

import pygame
import random
import Room
import Player

def treasureInit():
    r = random.randint(1, 3)
    return r

def treasurePlaceholder(screen):
    roomImage = pygame.image.load('img/treasureImage.png').convert()
    screen.blit(roomImage, (102, 102))

def treasureEvent(screen,r,player,map):
    if r == 1:
        # weapon
        itemIcon = pygame.image.load('img/weapon.png').convert()
    elif r == 2:
        # armor
        itemIcon = pygame.image.load('img/armor.png').convert()
    elif r == 3:
        # healing
        itemIcon = pygame.image.load('img/healing.png').convert()
    itemIcon.set_colorkey((255,255,255))
    screen.blit(itemIcon,(116,150))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # get item, add to inventory
            if r == 1:
                player.AddItemToInventory("Sword")
            elif r == 2:
                player.AddItemToInventory("Armor")
            elif r == 3:
                player.ApplyHPChange(2)
            # Storing player coords
            playerCoords = player.GetPosition()
            # Clearing map
            map.getRoomData()[playerCoords[0]][playerCoords[1]].cleared()
            # Clearing player
            player.setClearedTrue()


    #if player does thing:
        #player.setClearedTrue()
        #roomData[playerCoords[0]][playerCoords[1]].cleared()

    #^^^ needs every function to intake player object and roomdata object, which already exist in main!!!