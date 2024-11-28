# Authors: Joshua R., Grant S.
# Last Updated: 11-28
# Description: Map superclass for map generation

#Importing random library for random room generation
import random

class Room:

    #Constructor
    def __init__(self):
        self._isWood = False
        self. isStone = False
        self._isPuzzle = False
        self._isCombat = False
        self._isTreasure = False
        self._isNothing = False

        #Random texture selection
        texture = random.randint(1,2)

        if texture == 1:
            self._isWood = True
            self._isStone = False
        elif texture == 2:
            self._isWood = False
            self._isStone = True

        #Random Room Selection
        rType = random.randint(1,10)

        if rType <= 3: #3/10 for puzzle (30%)
            self._isPuzzle = True
        elif 3 < rType <=6: #3/10 for empty (30%)
            self._isNothing = True
        elif 6 < rType <= 9: #3/10 for combat (30%)
            self._isCombat = True
        elif rType == 10: #1/10 for treasure (10%)
            self._isTreasure = True

    #GETTERS
    #isWood
    def getisWood(self):
        return self._isWood
    #isStone
    def getisWood(self):
        return self._isStone
    #isPuzzle
    def getisPuzzle(self):
        return self._isPuzzle
    #isNothing
    def getisNothing(self):
        return self._isNothing
    #isCombat
    def getisCombat(self):
        return self._isCombat
    #isTreasure
    def getisTreasure(self):
        return self._isTreasure