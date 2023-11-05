from game_states import GameState
from gController import *

#Observer class

#Class handles all actions that need to be taken on the agents behalf
class Action:
    def __init__(self): 
        self.function_map = {
            GameState.EXPLORE: self.explore,
            GameState.ATTACKING: self.attack,
            GameState.HEAL: self.heal,
            GameState.USEBUTTON: self.use,
        }


    #Explore map depending on the terrain 
    def explore(self): 
        gController.goRight()
        gController.climb()
        return gameController.roll()
    #Attack and kill enemy 
    def attack(self): 
        return gameController.weapon1()  
    #health has dropped so we need to heal
    def heal(self): 
        return gameController.health()
    #this handles the leaving of the level and the opening of doors maybe
    def use(self): 
        return gameController.collect()
        