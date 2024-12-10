# Authors: Joshua R., Grant S.
# Last Updated: 12-3
# Description: Holds functions for puzzle interactions.

import pygame
import random
import Room

global b1,b2,b3

def puzzlePlaceholder(screen):
    roomImage = pygame.image.load('img/puzzleImage.png').convert()
    screen.blit(roomImage, (102, 102))

def buttonInit():
    r = random.randint(1, 6)
    return r

def buttonPuzzle(screen,r,player,map,b1,b2,b3):

    #Tablet import
    tablet = pygame.image.load('img/puzzleTablet.png').convert()
    tablet.set_colorkey((255,255,255))
    screen.blit(tablet,(116,150))

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


    pos = pygame.mouse.get_pos()

    #Button reactivity
    if b1 == True:
        colorSequence[0] = "White"
    if b2 == True:
        colorSequence[1] = "White"
    if b3 == True:
        colorSequence[2] = "White"

    beep_sound = pygame.mixer.Sound("bgm/beep.wav")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:

            #Red Button
            if r == 1 or r == 2:
                if pos[0] in range(142,158) and pos[1] in range(192,208):
                    b1 = True
                    pygame.mixer.Sound.play(beep_sound)
            #Green Button
            elif r == 5 or r == 6:
                if pos[0] in range(192, 208) and pos[1] in range(192, 208):
                    b1 = True
                    pygame.mixer.Sound.play(beep_sound)
            #Blue Button
            elif r == 3 or r == 4:
                if pos[0] in range(242, 258) and pos[1] in range(192, 208):
                    b1 = True
                    pygame.mixer.Sound.play(beep_sound)

            #Red Second Button
            if (r == 3 or r == 5) and (b1 == True):
                if pos[0] in range(142,158) and pos[1] in range(192,208):
                    b2 = True
                    pygame.mixer.Sound.play(beep_sound)
            #Green Second Button:
            elif (r == 2 or r == 4) and (b1 == True):
                if pos[0] in range(192, 208) and pos[1] in range(192, 208):
                    b2 = True
                    pygame.mixer.Sound.play(beep_sound)
            #Blue Second Button
            elif (r == 1 or r == 6) and (b1 == True):
                if pos[0] in range(242, 258) and pos[1] in range(192, 208):
                    b2 = True
                    pygame.mixer.Sound.play(beep_sound)

            # Red Third Button
            if (r == 4 or r == 6) and (b2 == True):
                if pos[0] in range(142, 158) and pos[1] in range(192, 208):
                    b3 = True
                    pygame.mixer.Sound.play(beep_sound)
            # Green Third Button:
            elif (r == 1 or r == 3) and (b2 == True):
                if pos[0] in range(192, 208) and pos[1] in range(192, 208):
                    b3 = True
                    pygame.mixer.Sound.play(beep_sound)
            # Blue Third Button
            elif (r == 2 or r == 5) and (b2 == True):
                if pos[0] in range(242, 258) and pos[1] in range(192, 208):
                    b3 = True
                    pygame.mixer.Sound.play(beep_sound)


    if b3:
        #Storing player coords
        playerCoords = player.GetPosition()
        #Clearing map
        map.getRoomData()[playerCoords[0]][playerCoords[1]].cleared()
        # check map end
        player.setClearedTrue()
        map.setAllClear()

    return b1,b2,b3