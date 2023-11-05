import pyautogui
import time
import keyboard

class Controller:
    def __init__(self):
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

    # """
    # def doubleJump():
    #     pyautogui.keyDown('space')
    #     pyautogui.keyDown('space')
    #     time.sleep(1)
    #     pyautogui.keyUp('space')
    #     pyautogui.keyUp('space')
    # """

        

    def climb(self):
        pyautogui.keyDown('up')
        time.sleep(1)
        pyautogui.keyUp('up')

    def roll(self):
        pyautogui.keyDown('ctrl')
        time.sleep(1)
        pyautogui.keyUp('ctrl')

    def weapon1(self):
        pyautogui.keyDown('1')
        time.sleep(1)
                    #left-click
        pyautogui.keyUp('1')

    def weapon2(self):
        pyautogui.keyDown('2')
                                #right-click
        time.sleep(1)
        pyautogui.keyUp('2')

    def health(self):
        pyautogui.keyDown('h')
        time.sleep(1)
        pyautogui.keyUp('h')

    def collect(self):
        pyautogui.keyDown('r')
        time.sleep(1)
        pyautogui.keyUp('r')


    def test(self):
        return 0 
        # while not keyboard.is_pressed('backspace'):
            
        #     self.crouch()
        #     # doubleJump()
        #     # doubleJump()
        #     # doubleJump()
            
        #     self.climb()
        #     self.roll()
        #     # doubleJump()

        #     self.weapon1()
        #     self.weapon2()
        #     # doubleJump()

        #     self.health()
        #     self.collect()
            
        #     self.goRight()
        #     # doubleJump()

        #     self.goRight()
        #     self.goRight()
        #     self.jump()
        #     self.jump()
        #     self.goLeft()
        #     self.jump()
        #     self.goRight()
        #     pass
