# Authors: Joshua R., Grant S.
# Last Updated: 12-8
# Description: Holds functions for combat interactions.

import random
import pygame

global cb1,cb2,cb3,cb4,cb5,cb6,hasWep,hasArm

def combatPlaceholder(screen):
    roomImage = pygame.image.load('img/combatImage.png').convert()
    screen.blit(roomImage, (102, 102))

def combatInit(cb1,cb2,cb3,cb4,cb5,cb6):
    # button 1
    cb1[0] = random.randint(130,270)
    cb1[1] = random.randint(80,285)

    # button 2
    cb2[0] = random.randint(130, 270)
    cb2[1] = random.randint(80, 285)

    # button 3
    cb3[0] = random.randint(130, 270)
    cb3[1] = random.randint(80, 285)

    # button 4
    cb4[0] = random.randint(130, 270)
    cb4[1] = random.randint(80, 285)

    # button 5
    cb5[0] = random.randint(130, 270)
    cb5[1] = random.randint(80, 285)

    # button 6
    cb6[0] = random.randint(130, 270)
    cb6[1] = random.randint(80, 285)


def combatEncounter(screen,player,cb1,cb2,cb3,cb4,cb5,cb6,hasWep,hasArm,map):

    #Goblin Import
    if player.GetHP() != 0:
        goblin = pygame.image.load('img/Goblin.png').convert()
        goblin.set_colorkey((255,255,255))
        screen.blit(goblin,(130,75))

        # button 1
        if cb1[2]:
            pygame.draw.circle(screen, 'red', (cb1[0],cb1[1]), 8)
        # button 2
        if cb2[2]:
            pygame.draw.circle(screen, 'red', (cb2[0], cb2[1]), 8)
        # button 3
        if cb3[2]:
            pygame.draw.circle(screen, 'red', (cb3[0], cb3[1]), 8)

        #Drawing remainder buttons if player does not have sword
        if not hasWep:
            # button 4
            if cb4[2]:
                pygame.draw.circle(screen, 'red', (cb4[0], cb4[1]), 8)
            # button 5
            if cb5[2]:
                pygame.draw.circle(screen, 'red', (cb5[0], cb5[1]), 8)
            # button 6
            if cb6[2]:
                pygame.draw.circle(screen, 'red', (cb6[0], cb6[1]), 8)

        #Click check logic
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:

                # button 1
                if pos[0] in range(cb1[0]-5,cb1[0]+5) and pos[1] in range(cb1[1]-5,cb1[1]+5) and cb1[2]:
                    cb1[2] = False
                # button 2
                elif pos[0] in range(cb2[0]-5,cb2[0]+5) and pos[1] in range(cb2[1]-5,cb2[1]+5) and cb2[2]:
                    cb2[2] = False
                # button 3
                elif pos[0] in range(cb3[0]-5,cb3[0]+5) and pos[1] in range(cb3[1]-5,cb3[1]+5) and cb3[2]:
                    cb3[2] = False
                # button 4
                elif pos[0] in range(cb4[0]-5,cb4[0]+5) and pos[1] in range(cb4[1]-5,cb4[1]+5) and cb4[2]:
                    cb4[2] = False
                # button 5
                elif pos[0] in range(cb5[0]-5,cb5[0]+5) and pos[1] in range(cb5[1]-5,cb5[1]+5) and cb5[2]:
                    cb5[2] = False
                # button 6
                elif pos[0] in range(cb6[0]-5,cb6[0]+5) and pos[1] in range(cb6[1]-5,cb6[1]+5) and cb6[2]:
                    cb6[2] = False

                #Misclick logic (taking damage)
                else:
                    if hasArm:
                        player.GetInventory().remove("Armor")
                    else:
                        player.ApplyHPChange(-1)

        #Completion Check
        if hasWep and (cb1[2] == False) and (cb2[2] == False) and (cb3[2] == False):
            #Storing player coords
            playerCoords = player.GetPosition()
            #Clearing map
            map.getRoomData()[playerCoords[0]][playerCoords[1]].cleared()
            #check map end
            player.setClearedTrue()
            map.setAllClear()
        elif (cb1[2] == False) and (cb2[2] == False) and (cb3[2] == False) and (cb4[2] == False) and (cb5[2] == False) and (cb6[2] == False):
            # Storing player coords
            playerCoords = player.GetPosition()
            # Clearing map
            map.getRoomData()[playerCoords[0]][playerCoords[1]].cleared()
            # check map end
            player.setClearedTrue()
            map.setAllClear()

    return cb1,cb2,cb3,cb4,cb5,cb6