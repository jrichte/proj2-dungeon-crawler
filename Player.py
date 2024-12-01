# Authors: Joshua R., Grant S.
# Last Updated: 11-15
# Description: Stores information and functions about the player.

import pygame
from Map import Map
import supporterFunctions

class Player():
    def __init__(self, startingPosition, startingFacing, startingHP, startingInventory):
        # note that position is stored as [y,x]
        self.__currentPosition = startingPosition
        self.__currentFacing = startingFacing
        self.__maxHP = startingHP
        self.__currentHP = startingHP
        self.__currentInventory = startingInventory
    # getter functions
    def GetHP(self):
        return self.__currentHP
    def GetMaxHP(self):
        return self.__maxHP
    def GetPosition(self):
        return self.__currentPosition
    def GetFacing(self):
        return self.__currentFacing
    def GetInventory(self):
        return self.__currentInventory
    # setter functions
    def ApplyHPChange(self, hpChange):
        self.__currentHP += hpChange
    def ChangeMaxHP(self, hpAdjust):
        self.__maxHP += hpAdjust
    def AddItemToInventory(self, newItem):
        self.__currentInventory.append(newItem)
    def RemoveItemFromInventory(self, removedItem):
        self.__currentInventory.remove(removedItem)
    def MoveCoordinates(self, movement, mapObject):
        mapLayout = mapObject.getLayout()
        for i in range(len(movement)):
            if movement[i]:
                # check if we'd go out of bounds above or left
                if self.__currentPosition[0] + movement[0] < 0 or self.__currentPosition[1] + movement[1] < 0:
                    return
                # check if we'd go out of bounds right or below
                else:
                    try:
                        if mapLayout[(self.__currentPosition[0] + movement[0]),(self.__currentPosition[1] + movement[1])] != 0:
                                self.__currentPosition[i] += movement[i]
                    except IndexError:
                        return
    def RotateLeft(self):
        # let 0 be north, 1 be east, 2 be south, 3 be west
        # left rotation is west->south->east->north->west
        self.__currentFacing -= 1
        if self.__currentFacing < 0:
            self.__currentFacing = 3
    def RotateRight(self):
        # let 0 be north, 1 be east, 2 be south, 3 be west
        # right rotation is west->north->east->south->west
        self.__currentFacing += 1
        if self.__currentFacing > 3:
            self.__currentFacing = 0