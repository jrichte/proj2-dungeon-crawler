# Authors: Joshua R., Grant S.
# Last Updated: 11-15
# Description: Stores information and functions about the player.

import pygame

class Player():
    def __init__(self, startingPosition, startingHP, startingInventory):
        self.__currentPosition = startingPosition
        self.__currentHP = startingHP
        self.__currentInventory = startingInventory
    # getter functions
    def GetHP(self):
        return self.__currentHP
    def GetPosition(self):
        return self.__currentPosition
    def GetInventory(self):
        return self.__currentInventory
    # setter functions
    def ApplyHPChange(self, hpChange):
        self.__currentHP += hpChange
    def AddItemToInventory(self, newItem):
        self.__currentInventory.append(newItem)
    def RemoveItemFromInventory(self, removedItem):
        self.__currentInventory.remove(removedItem)
    def MoveCoordinates(self, movement):
        for i in range(len(self.__currentPosition):
            self.__currentPosition[i] += movement[i]

        