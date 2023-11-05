from game_states import GameState

class Action:
    def __init__(self): 
        self.function_map = {
            GameState.EXPLORE: self.explore,
            GameState.ATTACKING: self.attack,
            GameState.HEAL: self.heal,
            GameState.USEBUTTON: self.use,
        }
    def explore(self): 
        return "explore"
    def attack(self): 
        return "attack"   
    def heal(self): 
        return "heal"
    def use(self): 
        return "use"