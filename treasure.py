# Authors: Joshua R., Grant S.
# Last Updated: 12-2
# Description: Holds functions for combat interactions.

import pygame
import random
import Room
import Player

def treasureInit():
    """
    Initializes treasure random state.
    :return: Returns an int from 1-3, inclusive.
    """
    r = random.randint(1, 3)
    return r

def treasurePlaceholder(screen):
    """
    placeholder function for testing treasure
    :param screen:
    :return:
    """
    roomImage = pygame.image.load('img/treasureImage.png').convert()
    screen.blit(roomImage, (102, 102))

def treasureEvent(screen,r,player,map):
    """
    Function for handling treasure gets.
    :param screen: The screen to display on.
    :param r: Random int from 1-3, via treasureInit.
    :param player: Player object.
    :param map: Map object.
    """
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
                if player.GetMaxHP() == player.GetHP():
                    player.ChangeMaxHP(1)
                    player.ApplyHPChange(1)
                else:
                    player.ApplyHPChange(1)
            item_sound = pygame.mixer.Sound("bgm/item.wav")
            pygame.mixer.Sound.play(item_sound)
            # Storing player coords
            playerCoords = player.GetPosition()
            # Clearing map
            map.getRoomData()[playerCoords[0]][playerCoords[1]].cleared()
            # Clearing player
            player.setClearedTrue()
            # check map end
            map.setAllClear()


    #if player does thing:
        #player.setClearedTrue()
        #roomData[playerCoords[0]][playerCoords[1]].cleared()

    #^^^ needs every function to intake player object and roomdata object, which already exist in main!!!