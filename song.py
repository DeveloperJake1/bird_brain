from BirdBrain import Finch
import time

myFinch = Finch('A')

# Plays a good song made by Developer Jake

myFinch.playNote(79,16)
time.sleep(.25)
myFinch.playNote(81,16)
time.sleep(.25)
myFinch.playNote(82,16)
time.sleep(.25)
myFinch.playNote(81,16)
time.sleep(.25)
myFinch.playNote(79,4)
time.sleep(.25)

for i in range(20):
    myFinch.playNote(i+71,5)
    time.sleep(.2)
    if (i == 19):
        myFinch.playNote(i+72,5)
        time.sleep(1)
        myFinch.playNote(i+71,5)
        time.sleep(1)
        myFinch.playNote(i+72,5)
        time.sleep(1)
        myFinch.playNote(i+68,5)
        time.sleep(1)
        myFinch.playNote(i+71,5)
        time.sleep(1)
        myFinch.playNote(i+72,5)









myFinch.stopAll()