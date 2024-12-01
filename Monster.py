# Authors: Joshua R., Grant S.
# Last Updated: 11-15
# Description: Basic superclass for monsters.

import pygame

class Monster():
    def __init__(self, maxHP, attackType, defenseType, position, name, sprite):
        self._currentPosition = position
        self._currentHP = maxHP
        self._attackType = attackType # list of player dodges that monster hits
        self._defenseType = defenseType # list of player attacks that get blocked
        # figure out logic later for showing names/sprites
        self._monsterName = name
        self._monsterSprite = sprite
    # getter functions
    def GetHP(self):
        return self._currentHP
    def GetPosition(self):
        return self._currentPosition
    def GetAttackType(self):
        return self._attackType    
    def GetDefenseType(self):
        return self._defenseType

    # setter functions
    def ApplyHPChange(self, hpChange):
        self._currentHP += hpChange
    def MoveCoordinates(self, movement):
        for i in range(len(self._currentPosition)):
            self._currentPosition[i] += movement[i]

    # combat test functions - return false for player failure, true for player success
    def PlayerAttack(self, attackInput):
        # if player attack coincides with monster defense, return false
        for i in range(len(self._defenseType)):
            if attackInput == self._defenseType[i]:
                return False
        return True

    def PlayerDefense(self, defenseInput):
        # if player defense coincides with monster attack, return false
        for i in range(len(self._attackType)):
            if defenseInput == self._attackType[i]:
                return False
        return True