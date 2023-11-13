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

#####################################################################################################################################3
import pyautogui
import time
import keyboard
import random

# Wait for a few seconds to ensure the game has loaded
time.sleep(5)

def goRight():
    pyautogui.keyDown('right')
    time.sleep(2)
    pyautogui.keyUp('right')

def goLeft():
    pyautogui.keyDown('left')
    time.sleep(2)
    pyautogui.keyUp('left')

def jump():
    pyautogui.keyDown('space')
    time.sleep(1)
    pyautogui.keyUp('space')

def crouch():
    pyautogui.keyDown('down')
    time.sleep(1)
    pyautogui.keyUp('down')


def doubleJump():
    jump()
    jump()

def quickRight():
    goRight()
    time.sleep(0.1)
    goRight()

def quickLeft():
    goLeft()
    time.sleep(0.1)
    goLeft()

def dashRight():
    quickRight()
    quickRight()
    
def dashLeft():
    quickLeft()
    quickLeft()

    
def climb():
    pyautogui.keyDown('up')
    time.sleep(1)
    pyautogui.keyUp('up')

def roll():
    pyautogui.keyDown('ctrl')
    time.sleep(1)
    pyautogui.keyUp('ctrl')

def weapon1():
    pyautogui.keyDown('1')
    time.sleep(1)
                #left-click
    pyautogui.keyUp('1')

def weapon2():
    pyautogui.keyDown('2')
                            #right-click
    time.sleep(1)

pyautogui.keyUp('2')

def health():
    pyautogui.keyDown('h')
    time.sleep(1)
    pyautogui.keyUp('h')

def collect():
    pyautogui.keyDown('r')
    time.sleep(1)
    pyautogui.keyUp('r')

def jump():
    pyautogui.keyDown('space')
    time.sleep(1)
    pyautogui.keyUp('space')

def Quickjump():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    pyautogui.keyUp('space')

def doubleJump():
    Quickjump()
    Quickjump()
    
def hardStomp():
    pyautogui.keyDown('down')
    time.sleep(0.05)
    doubleJump()
    pyautogui.keyUp('down')

def jumpDown():
    pyautogui.keyDown('down')
    time.sleep(0.05)
    jump()
    pyautogui.keyUp('down')
    
while not keyboard.is_pressed('backspace'):
    time.sleep(3)
    dashRight()
    time.sleep(3)
    jumpDown()
    time.sleep(3)
    doubleJump()
    time.sleep(3)
    hardStomp()
    roll()

while not keyboard.is_pressed('backspace'):
    doubleJump()
    roll()
    doubleJump()
    doubleJump()
    doubleJump()
    doubleJump()
    doubleJump() 
    crouch()
    dashRight()
    goLeft()
    dashRight()
    goLeft()
    dashRight()
    goLeft()    
    doubleJump()
    roll()
    doubleJump()
    doubleJump()
    doubleJump()
    doubleJump()
    doubleJump()
    doubleJump()
    
      
    climb()
    roll()
    doubleJump()
     
    weapon1()
    weapon2()
    #doubleJump()
    
    health()
    collect()

    goRight()
    #doubleJump()
    
    goRight()
    goRight()
    jump()
    jump()
    goLeft()
    jump()
    goRight()

# Q-learning parameters
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.1  # Epsilon-greedy parameter

Q = {}  # Initialize Q-values

# Function to choose an action based on epsilon-greedy policy
def choose_action(state):
    if random.uniform(0, 1) < epsilon:
        return random.choice(["jump", "move_right", "move_left", "crouch", "dash_right", "dash_left", "climb", "roll", "weapon1", "weapon2", "health", "collect"])
    else:
        if state not in Q:
            Q[state] = {'jump': 0, 'move_right': 0, 'move_left': 0, 'crouch': 0, 'dash_right': 0, 'dash_left': 0, 'climb': 0, 'roll': 0, 'weapon1': 0, 'weapon2': 0, 'health': 0, 'collect': 0}
        return max(Q[state], key=Q[state].get)

# Training loop
total_episodes = 100  # Number of episodes for training

for episode in range(total_episodes):
    state = start_state

    while not keyboard.is_pressed('backspace'):
        # Choose action using epsilon-greedy policy
        action = choose_action(state)

        # Update Q-values based on the Bellman equation
        next_state = "new_state"  # Define the new state based on the action performed
        reward = 0  # Define a reward based on the action performed and the new state

        if state not in Q:
            Q[state] = {'jump': 0, 'move_right': 0, 'move_left': 0, 'crouch': 0, 'dash_right': 0, 'dash_left': 0, 'climb': 0, 'roll': 0, 'weapon1': 0, 'weapon2': 0, 'health': 0, 'collect': 0}

        # Update Q-value based on the Bellman equation
        Q[state][action] += alpha * (reward + gamma * max(Q.get(next_state, {'jump': 0, 'move_right': 0, 'move_left': 0, 'crouch': 0, 'dash_right': 0, 'dash_left': 0, 'climb': 0, 'roll': 0, 'weapon1': 0, 'weapon2': 0, 'health': 0, 'collect': 0}), key=Q.get(next_state, {'jump': 0, 'move_right': 0, 'move_left': 0, 'crouch': 0, 'dash_right': 0, 'dash_left': 0, 'climb': 0, 'roll': 0, 'weapon1': 0, 'weapon2': 0, 'health': 0, 'collect': 0}).get) - Q[state][action])

        state = next_state 


        