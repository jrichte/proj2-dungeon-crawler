# Authors: Joshua R., Grant S.
# Last Updated: 11-17
# Description: Map superclass for map generation

#importing random library for map generation
import random
#importing numpy for list visualizations
import numpy as np
#importing list index supporter function
from supporterFunctions import indexExists

class Map():

    #Constructor (takes in map size in x and y and outputs a 2d list of that shape)
    def __init__(self, sizeX, sizeY): #BASED ON ALGORITHM FOR GENERATION MINIMUM ALLOWED SIZE SHOULD BE 3X3
        self._layout = [[0 for _ in range(sizeY)] for _ in range(sizeX)]
        #Storing sizeX and sizeY for later use in populate map
        self._sizeX = sizeX
        self._sizeY = sizeY

    #GETTERS
    #layout Getter
    def getLayout(self):
        return self._layout
    #sizeX Getter
    def getSizeX(self):
        return self._sizeX
    #sizeY Getter
    def getSizeY(self):
        return self._sizeY

    # Function to convert list into more palatable array
    def makeArray(self):
        self._layout = np.array(self._layout)

    #Function to populate list with continuous map objects
    def populateMap(self):
        #Creating a starting point in the (effective) center of the map
        basePositionX = int(self._sizeX - (self._sizeX/2))
        basePositionY = int(self._sizeY - (self._sizeY/2))
        self._layout[basePositionX][basePositionY] = 1 #1 could be replaced with a specific starting room object

        #Creating 1st random branch (randomly deciding a side to branch off of home)
        side = random.randint(1,4)

        #up branch
        if side == 1:
            currentX = basePositionX
            currentY = basePositionY - 1
        #down branch
        elif side == 2:
            currentX = basePositionX
            currentY = basePositionY + 1
        #right branch
        elif side == 3:
            currentX = basePositionX + 1
            currentY = basePositionY
        #left branch
        elif side == 4:
            currentX = basePositionX - 1
            currentY = basePositionY
        #populating random starting side
        self._layout[currentY][currentX] = 1

        #Randomly creating x rooms for first branch
        #[x is the sum of both dimensions of the map divided by 2, or until no possible moves can be made]
        for i in range(int((self._sizeY+self._sizeX)/2)):

            #Resetting option set (Variable to track possible allowed generations)
            optionSet = \
            {
                "up": 0,
                "down": 0,
                "left": 0,
                "right": 0
            }

            #DETERMINING POSSIBLE MOVEMENT OPTIONS
            #seeing if up is a valid index
            if indexExists(self._layout,(currentY-1),(currentX)):
                #seeing if up is already populated and not going to overflow into other end of list
                if self._layout[currentY-1][currentX] != 1 and currentY != 0 :
                    optionSet["up"] = 1

            #seeing if down is a valid index
            if indexExists(self._layout,(currentY+1),(currentX)):
                #seeing if down is already populated and not going to overflow into other end of list
                if self._layout[currentY+1][currentX] != 1 and currentY != self._sizeY - 1:
                    optionSet["down"] = 1

            #seeing if right is a valid index
            if indexExists(self._layout, (currentY), (currentX+1)):
                #seeing if right is already populated and not going to overflow into other end of list
                if self._layout[currentY][currentX+1] != 1 and currentX != self._sizeX -1:
                    optionSet["right"] = 1

            #seeing if left is a valid index
            if indexExists(self._layout, (currentY), (currentX-1)):
                #seeing if left is already populated and not going to overflow into other end of list
                if self._layout[currentY][currentX-1] != 1 and currentX != 0:
                    optionSet["left"] = 1

            #determining how many possible moves can be made to randomly pick one, breaking if no moves can be made
            if (optionSet['up'] + optionSet['down'] + optionSet['left'] + optionSet['right']) == 0:
                break
            else:
                while True:
                    #randomly deciding direction
                    direction = random.randint(1,4)

                    #If direction is up and up is valid
                    if direction == 1 and optionSet["up"] != 0:
                        self._layout[currentY -1 ][currentX] = 1
                        currentY = currentY - 1
                        break
                    #If direction is down and down is valid
                    elif direction == 2 and optionSet["down"] != 0:
                        self._layout[currentY + 1][currentX] = 1
                        currentY = currentY +1
                        break
                    #If direction is right and right is valid
                    elif direction == 3 and optionSet["right"] != 0:
                        self._layout[currentY][currentX + 1] = 1
                        currentX = currentX + 1
                        break
                    #If direction is left and left is valid
                    elif direction == 4 and optionSet["left"] != 0:
                        self._layout[currentY][currentX - 1] = 1
                        currentX = currentX - 1
                        break

        #SECOND BRANCH GENERATION
        #Checking possible open sides of home, if none open then no second branch generated

        #variable to track generation possibility
        possibleGen = 0

        #up check
        if self._layout[basePositionY-1][basePositionX] == 1:
            possibleGen += 1
        #down check
        if self._layout[basePositionY+1][basePositionX] == 1:
            possibleGen += 1
        #right check
        if self._layout[basePositionY][basePositionX+1] == 1:
            possibleGen += 1
        #left check
        if self._layout[basePositionY][basePositionX-1] == 1:
            possibleGen += 1

        #Creating second branch for map by randomly selecting a side (if generation possible)
        if possibleGen !=4:
            while True:
                side = random.randint(1,4)

                #up branch
                if side == 1 and self._layout[basePositionY-1][basePositionX] != 1:
                    currentX = basePositionX
                    currentY = basePositionY - 1
                    break
                #down branch
                elif side == 2 and self._layout[basePositionY+1][basePositionX] !=1:
                    currentX = basePositionX
                    currentY = basePositionY + 1
                    break
                #right branch
                elif side == 3 and self._layout[basePositionY][basePositionX+1] !=1:
                    currentX = basePositionX + 1
                    currentY = basePositionY
                    break
                #left branch
                elif side == 4 and self._layout[basePositionY][basePositionX-1] !=1:
                    currentX = basePositionX - 1
                    currentY = basePositionY
                    break

            # populating random starting side
            self._layout[currentY][currentX] = 1

            # Randomly creating x rooms for second branch
            # [x is the sum of both dimensions of the map divided by 2, or until no possible moves can be made]
            for i in range(int((self._sizeY + self._sizeX) / 2)):

                # Resetting option set (Variable to track possible allowed generations)
                optionSet = \
                    {
                        "up": 0,
                        "down": 0,
                        "left": 0,
                        "right": 0
                    }

                # DETERMINING POSSIBLE MOVEMENT OPTIONS
                # seeing if up is a valid index
                if indexExists(self._layout, (currentY - 1), (currentX)):
                    # seeing if up is already populated and not going to overflow into other end of list
                    if self._layout[currentY - 1][currentX] != 1 and currentY != 0:
                        optionSet["up"] = 1

                # seeing if down is a valid index
                if indexExists(self._layout, (currentY + 1), (currentX)):
                    # seeing if down is already populated and not going to overflow into other end of list
                    if self._layout[currentY + 1][currentX] != 1 and currentY != self._sizeY - 1:
                        optionSet["down"] = 1

                # seeing if right is a valid index
                if indexExists(self._layout, (currentY), (currentX + 1)):
                    # seeing if right is already populated and not going to overflow into other end of list
                    if self._layout[currentY][currentX + 1] != 1 and currentX != self._sizeX - 1:
                        optionSet["right"] = 1

                # seeing if left is a valid index
                if indexExists(self._layout, (currentY), (currentX - 1)):
                    # seeing if left is already populated and not going to overflow into other end of list
                    if self._layout[currentY][currentX - 1] != 1 and currentX != 0:
                        optionSet["left"] = 1

                #determining how many possible moves can be made to randomly pick one, braking if no moves can be made
                if (optionSet['up'] + optionSet['down'] + optionSet['left'] + optionSet['right']) == 0:
                    break
                else:
                    while True:
                        # randomly deciding direction
                        direction = random.randint(1, 4)

                        # If direction is up and up is valid
                        if direction == 1 and optionSet["up"] != 0:
                            self._layout[currentY - 1][currentX] = 1
                            currentY = currentY - 1
                            break
                        # If direction is down and down is valid
                        elif direction == 2 and optionSet["down"] != 0:
                            self._layout[currentY + 1][currentX] = 1
                            currentY = currentY + 1
                            break
                        # If direction is right and right is valid
                        elif direction == 3 and optionSet["right"] != 0:
                            self._layout[currentY][currentX + 1] = 1
                            currentX = currentX + 1
                            break
                        # If direction is left and left is valid
                        elif direction == 4 and optionSet["left"] != 0:
                            self._layout[currentY][currentX - 1] = 1
                            currentX = currentX - 1
                            break


#Testing runs
"""
x=Map(10,10)
x.populateMap()
x.makeArray()
print(f"{x.getLayout()}")
"""