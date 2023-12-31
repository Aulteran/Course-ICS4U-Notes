'''
Author: Aadil Hussain
Built on: Python 3.10.11
'''

# A fellow programmer has asked that you help them code their game. 
# They have asked that you model a real world object using OOP in order 
# that they may use the class over and over.

# Please create class for a speaker. He needs the speaker to :
    # turn on and off
    # have 2 inputs (that be toggled between)
    # have volume levels from 1 to 5
    # must be able to check all of this information using a
    # have a mute button (independant of volume level)
# NOTE: make sure to do some planning!!! HINT: ask yourself 
# what PROPERTIES the speaker will have, and what BEHAVIOURS it should have.

# There is a set of test code that is attached to this git. You will run the test code on your class

class Speaker():
    def __init__(self, volume, input):
        self.power = False #True is on and False is off
        self.volume = volume # can be between 1 and 5
        self.muted = False
        self.input = input # can be either 1 or 2
    
    def show(self):
        status = f'SPEAKER STATUS:\nPower On:{self.power}\nMuted:{self.muted}\nVolume:{self.volume}'
        print(status)
    
    def toggle_power(self):
        if self.power == True:
            self.power = False
            print("speaker turned off.")
        else:
            self.power = True
            print("The speaker has turned on")
    
    def volume_up(self):
        if self.volume < 5:
            self.volume+=1
        print(f"now set to volume [{self.volume}]")

    def volume_down(self):
        if self.volume > 1:
            self.volume-=1
        print(f"now set to volume [{self.volume}]")
    
    def toggle_mute(self):
        if self.muted == True:
            self.muted = False
            print("speaker unmuted")
        else:
            self.muted = True
            print("speaker muted")
    
    def toggle_input(self):
        if self.input == 1:
            self.input = 2
            print("input now [2]")
        else:
            self.input = 1
            print("input now [1]")
