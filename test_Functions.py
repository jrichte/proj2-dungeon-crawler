# Authors: Joshua R., Grant S.
# Last Updated: 12-3
# Description: Holds test functions.

import pygame

# import pytest and our functions
import pytest
from Map import Map
from Player import Player
from Room import Room

# test that generation guarantees starting room
@pytest.mark.parametrize("x_dim,y_dim", [(4,4),(16,16),(10,16),(50,52)])
def test_startingRoomExists(x_dim,y_dim):
    mapTest = Map(x_dim, y_dim)
    mapTest.populateMap()
    mapTest.createRoomData()
    mapTest.makeArray()
    startingRoom = mapTest.getRoomData()[int(x_dim/2)][int(y_dim/2)]
    assert isinstance(startingRoom,Room)

# test that we can't move outside of the map by making sure position is 0,0 after movement
@pytest.mark.parametrize("movement", [[1,0], [-1,0], [0,1], [0,-1]])
def test_movementEdge(movement):
    X_DIM = 1
    Y_DIM = 1
    mapTest = Map(X_DIM, Y_DIM)
    mapTest._layout = [[1]]
    mapTest.createRoomData()
    mapTest.makeArray()
    playerTest = Player([0,0], 0, 3, [0])
    playerTest.MoveCoordinates(movement, mapTest)
    assert playerTest.GetPosition() == [0,0]

# test that clearing works
def test_clearing():
    X_DIM = 8
    Y_DIM = 8
    mapTest = Map(X_DIM, Y_DIM)
    mapTest.populateMap()
    mapTest.createRoomData()
    mapTest.makeArray()
    playerTest = Player([int(X_DIM/2),int(Y_DIM/2)], 0, 3, [0])
    roomDataTest = mapTest.getRoomData()[int(X_DIM/2)][int(Y_DIM/2)]
    playerTest.setClearedTrue()
    roomDataTest.cleared()
    assert playerTest.GetCleared() and roomDataTest.getisClear()

# test that hp deduction works
@pytest.mark.parametrize("damageValue,hpValue", [(0,3),(1,3),(-1,2),(-3,0),(-4,0)])
def test_damage(damageValue,hpValue):
    playerTest = Player([0,0], 0, 3, [0])
    playerTest.ApplyHPChange(damageValue)
    assert playerTest.GetHP() == hpValue

# test rotation logic
@pytest.mark.parametrize("rotations,direction,final", [(2,'left',2),(3,'right',3),(3,'left',1),(5,'right',1),(6,'left',2)])
def test_rotation(rotations,direction,final):
    playerTest = Player([0,0], 0, 3, [0])
    for i in range(rotations):
        if direction == 'left':
            playerTest.RotateLeft()
        elif direction == 'right':
            playerTest.RotateRight()
    assert playerTest.GetFacing() == final

# allows pytest to run just by running this file
retcode = pytest.main()