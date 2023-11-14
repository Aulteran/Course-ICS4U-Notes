from speaker import *

speaker1 = Speaker(3,1)
speaker2 = Speaker(2,2)

speaker1.show()
speaker2.show()
speaker1.toggle_power()
speaker1.volume_up()
speaker1.volume_up()   
speaker1.volume_up()

speaker1.show()

speaker2.toggle_power()
speaker2.volume_down()
speaker2.toggle_mute()
speaker2.toggle_input()
speaker2.show()  

def test_speaker():
    assert speaker1.power == True
    assert speaker1.volume == 5
    assert speaker1.muted == False
    assert speaker1.input == 1

    assert speaker2.power == True
    assert speaker2.volume == 1
    assert speaker2.muted == True
    assert speaker2.input == 1
    
test_speaker()

print ('success')
