from Assignment8_TV_Remote import *
# from <FILENAME> import *

oTv = TV()

oTv.power()
oTv.show_info()

def test_run1():
    try:
        assert oTv.isOn == True
        assert oTv.channelList[oTv.channelIndex] == 2
        assert oTv.volume == 5
        print ('test1 succeeds')
    except:
        print ('test1 failed')

test_run1()

oTv = TV()

oTv.power()
oTv.channelUp()
oTv.channelUp()
oTv.volumeUp()
oTv.volumeUp()
oTv.show_info()

def test_run2():
    try:
        assert oTv.isOn == True
        assert oTv.channelList[oTv.channelIndex] == 5
        assert oTv.volume == 7
        print ('test2 succeeds')
    except:
        print ('test2 failed')

test_run2()

oTv = TV()

oTv.power()
oTv.show_info()
oTv.power()
oTv.show_info()

def test_run():
    try:
        assert oTv.isOn == False
        print ('test2 succeeds - part 1')
    except:
        print ('test2 failed - part 1')

test_run()

oTv.power()

for i in range (6):
    oTv.volumeUp()

def test_run3():
    try:
        assert oTv.isOn == True
        assert oTv.volume == 10
        print ('test3 succeeds - part 2')
    except:
        print ('test3 failed - part 2')

test_run3()

oTv = TV()

oTv.power()
oTv.show_info()

oTv.channelUp()
oTv.channelUp()
oTv.volumeUp()
oTv.volumeUp()
oTv.show_info()

oTv.power()
oTv.show_info()
oTv.power()
oTv.show_info()

oTv.volumeDown()
oTv.mute()
oTv.show_info
oTv.setChannel(11)

def test_run4():
    try:
        assert oTv.isOn == True
        assert oTv.channelList[oTv.channelIndex] == 11
        assert oTv.volume == 6
        assert oTv.isMuted == True
        print ('test4 succeeds')
    except:
        print ('test4 failed')

test_run4()