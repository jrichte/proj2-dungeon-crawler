# Authors: Joshua R., Grant S.
# Last Updated: 12-3
# Description: Holds main function for EE 551 Project 2.

import pygame
import displayFunctions as disp
from Map import Map
from Player import Player
import puzzle
import combat
import treasure
from combat import combatPlaceholder
from puzzle import puzzlePlaceholder
from treasure import treasurePlaceholder


# classes to handle player/inventory, map, minimap, enemies?

# file of functions for movement, tie together player (position in class) and map (coordinates in class)
# combat functions (use elements of enemy classes to determine required dodge?)

def main():
    # pygame setup (basic structural code borrowed from docs)
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    clock = pygame.time.Clock()
    running = True

    X_DIM = 16
    Y_DIM = 16
    map = Map(X_DIM, Y_DIM)
    map.populateMap()
    map.createRoomData()
    map.makeArray()
    player = Player([int(X_DIM/2),int(Y_DIM/2)],0,3,[0])
    map.getRoomData()[int(X_DIM/2)][int(Y_DIM/2)].visited()
    map.getRoomData()[int(X_DIM/2)][int(Y_DIM/2)].cleared()
    encounterInit = False
    while running:
        #Puzzle/Combat/Treasure logic
        #Important vars
        playerCoords = player.GetPosition()
        roomData = map.getRoomData()[playerCoords[0]][playerCoords[1]]

        if not roomData.getisClear():
            # Setting player cleared as false
            player.setClearedFalse()


        # poll for events
        if player.GetCleared() == True:
            # reset flag for initializing room
            encounterInit = False
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    facing = player.GetFacing()
                    keys = pygame.key.get_pressed()

                    #W key press (move forward facing considered)
                    if keys[pygame.K_w]:
                        if facing == 0:
                            player.MoveCoordinates([-1, 0], map)
                        elif facing == 1:
                            player.MoveCoordinates([0, 1], map)
                        elif facing == 2:
                            player.MoveCoordinates([1, 0], map)
                        elif facing == 3:
                            player.MoveCoordinates([0, -1], map)

                    #S key press (move backward facing considered)
                    elif keys[pygame.K_s]:
                        if facing == 0:
                            player.MoveCoordinates([1, 0], map)
                        elif facing == 1:
                            player.MoveCoordinates([0, -1], map)
                        elif facing == 2:
                            player.MoveCoordinates([-1, 0], map)
                        elif facing == 3:
                            player.MoveCoordinates([0, 1], map)

                    #A key press (move left facing considered)
                    elif keys[pygame.K_a]:
                        if facing == 0:
                            player.MoveCoordinates([0, -1], map)
                        elif facing == 1:
                            player.MoveCoordinates([-1, 0], map)
                        elif facing == 2:
                            player.MoveCoordinates([0, 1], map)
                        elif facing == 3:
                            player.MoveCoordinates([1, 0], map)

                    #D key press (move right facing considered)
                    elif keys[pygame.K_d]:
                        if facing == 0:
                            player.MoveCoordinates([0, 1], map)
                        elif facing == 1:
                            player.MoveCoordinates([1, 0], map)
                        elif facing == 2:
                            player.MoveCoordinates([0, -1], map)
                        elif facing == 3:
                            player.MoveCoordinates([-1, 0], map)

                    #Q key press (rotate counter-clockwise)
                    if keys[pygame.K_q]:
                        player.RotateLeft()
                    #E key press (rotate clockwise)
                    if keys[pygame.K_e]:
                        player.RotateRight()

                # copying movement logic for mouse-based movement
                if event.type == pygame.MOUSEBUTTONDOWN:
                    facing = player.GetFacing()
                    pos = pygame.mouse.get_pos()

                    #Rotate counter-clockwise button
                    if pos[0] in range(400,450) and pos[1] in range(250,300):
                        player.RotateLeft()

                    #Rotate clockwise button
                    elif pos[0] in range(500,550) and pos[1] in range(250,300):
                        player.RotateRight()

                    #Move forward button (facing considered)
                    elif pos[0] in range(450,500) and pos[1] in range(250,300):
                        if facing == 0:
                            player.MoveCoordinates([-1, 0], map)
                        elif facing == 1:
                            player.MoveCoordinates([0, 1], map)
                        elif facing == 2:
                            player.MoveCoordinates([1, 0], map)
                        elif facing == 3:
                            player.MoveCoordinates([0, -1], map)

                    #Move left button (facing considered)
                    elif pos[0] in range(400, 450) and pos[1] in range(300, 350):
                        if facing == 0:
                            player.MoveCoordinates([0, -1], map)
                        elif facing == 1:
                            player.MoveCoordinates([-1, 0], map)
                        elif facing == 2:
                            player.MoveCoordinates([0, 1], map)
                        elif facing == 3:
                            player.MoveCoordinates([1, 0], map)

                    #Move back button (facing considered)
                    elif pos[0] in range(450, 500) and pos[1] in range(300, 350):
                        if facing == 0:
                            player.MoveCoordinates([1, 0], map)
                        elif facing == 1:
                            player.MoveCoordinates([0, -1], map)
                        elif facing == 2:
                            player.MoveCoordinates([-1, 0], map)
                        elif facing == 3:
                            player.MoveCoordinates([0, 1], map)

                    #Move right button (facing considered)
                    elif pos[0] in range(500, 550) and pos[1] in range(300, 350):
                        if facing == 0:
                            player.MoveCoordinates([0, 1], map)
                        elif facing == 1:
                            player.MoveCoordinates([1, 0], map)
                        elif facing == 2:
                            player.MoveCoordinates([0, -1], map)
                        elif facing == 3:
                            player.MoveCoordinates([-1, 0], map)




        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        # RENDER YOUR GAME HERE
        # render UI
        disp.drawButtons(screen)
        disp.drawViewport(map, player, screen)
        disp.drawMiniMap(map, player, screen)
        disp.drawHealthBar(screen, player)


        if player.GetCleared() == False:
            # initialize each encounter once
            if encounterInit == False:
                # draw encounter and provide logic if room not cleared
                    # puzzle rooms
                if roomData.getisPuzzle():
                    randState = puzzle.buttonInit()
                    # combat rooms
                elif roomData.getisCombat():
                    combatPlaceholder(screen)
                    # treasure rooms
                elif roomData.getisTreasure():
                    treasurePlaceholder(screen)
                encounterInit = True
            else:
                if roomData.getisPuzzle():
                    puzzle.buttonPuzzle(screen,randState)
                    # combat rooms
                elif roomData.getisCombat():
                    combatPlaceholder(screen)
                    # treasure rooms
                elif roomData.getisTreasure():
                    treasurePlaceholder(screen)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    coords = player.GetPosition()
                    if pos[0] in range(60,340) and pos[1] in range(60,300):
                        player.setClearedTrue()
                        map.getRoomData()[coords[0]][coords[1]].cleared()


        """
        Can add logic to above if statement for different random puzzle room and monster room spawns potentially
        EACH FUNCTION FOR TREASURE, COMBAT, AND PUZZLE WILL NEED TO HAVE A FLAG TO SET BOTH PLAYER AND ROOM AS CLEARED
        """

        # eventually update this part to handle button clicks

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__ == '__main__':
        main()