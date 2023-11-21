'''
Author: Aadil Hussain
Built on: Python 3.10.11
'''
# Assignment 8: Modeling a TV Remote
# To keep track of its state, a TV class
# would have to maintain the following data:
    # - Power state (on or off)
    # - Mute state (is it muted?)
    # - Listof channels available
    # - Current channel setting
    # - Current volume setting
    # - Range of volume levels available

# And the actions that the TV must provide include:
    # - Turn the power on and off
    # - Raise and lower the volume
    # - Change the channel up and down
    # - Mute and unmute the sound
    # - Getinformation about the current settings
    # - Go to a specified channel

# START CHANNEL = 2 (or index = 0)
# START VOLUME = 5 // MIN VOLUME = 0 // MAX_VOLUME = 10

class TV():
    def __init__(self):
        self.channelList = [2, 4, 5, 7, 9, 11, 20, 36, 44, 54, 65]
        self.isOn = False
        self.isMuted = False
        self.channelIndex = 0
        self.volume = 5
        self.volumes = range(0,11) # From 0 to 10

        print(f'TV has been created with volume {self.volume} and on channel {self.channelList[self.channelIndex]}')
    
    def power(self):
        if self.isOn:
            self.isOn = False
            print('TV turning off')
        else:
            self.isOn = True
            print('TV turned on')

    def show_info(self):
        power = 'OFF'
        if self.isOn:
            power = 'ON'
        muted = 'UNMUTED'
        if self.isMuted:
            muted = 'MUTED'
        info = (
f'''TV Information
Power: {power}
Mute: {muted}
Channel: {self.channelList[self.channelIndex]}
Volume: {self.volume}/{max(self.volumes)}
Channels Available: {', '.join([str(x) for x in self.channelList])}
'''
        )
        print(info)

    def channelUp(self):
        if self.channelIndex == max(self.channelList):
            print(f"Cannot go higher than Channel {max(self.channelList)}")
            return
        self.channelIndex += 1
        print(f'TV now on channel {self.channelList[self.channelIndex]}')

    def channelDown(self):
        if self.channelIndex == min(self.channelList):
            print(f"Cannot go lower than Channel {min(self.channelList)}")
            return
        self.channelIndex -= 1
        print(f'TV now on channel {self.channelList[self.channelIndex]}')

    def volumeUp(self):
        if self.volume == max(self.volumes):
            print(f'TV Volume at maximum')
            return
        self.volume += 1
        print(f'TV volume set to {self.volume}/{max(self.volumes)}')

    def volumeDown(self):
        if self.volume == min(self.volumes):
            print(f'TV Volume at minimum')
            return
        self.volume -= 1
        print(f'TV volume set to {self.volume}/{max(self.volumes)}')

    def mute(self):
        if not self.isMuted:
            self.isMuted = True
            print('TV Muted')
        else:
            self.isMuted = False
            print('TV Un-Muted')

    def setChannel(self, new_channel:int):
        while True:
            try:
                if self.channelList.count(new_channel) != 0:
                    break
                else:
                    print("Invalid Channel Number")
            except ValueError:
                print("Please enter an integer value.")
        self.channelIndex = self.channelList.index(new_channel)
        print(f'TV now on channel {self.channelList[self.channelIndex]}')
