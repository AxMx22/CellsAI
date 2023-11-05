from enum import Enum

class GameState(Enum):
    EXPLORE = 1
    ATTACKING = 2
    HEAL = 3
    USEBUTTON = 4
    END = 5