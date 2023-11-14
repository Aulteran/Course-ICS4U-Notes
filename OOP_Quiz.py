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
    def __init__(self):
        self.power = False #True is on and False is off
        self.volume = 50 # can be between 0 and 100
        self.mute = False
        self.status = f'SPEAKER STATUS:\nPower On:{self.power}\nMuted:{self.mute}\nVolume:{self.volume}'
    
    def check_status(self):
        print(self.status)
    
    
