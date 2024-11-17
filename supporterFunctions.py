# Authors: Joshua R., Grant S.
# Last Updated: 11-17
# Description: Supporter functions for other code

#List index checker
def indexExists(list, y, x):
    try:
        list[y][x]
        return True
    except IndexError:
        return False