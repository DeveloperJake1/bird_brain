from BirdBrain import Finch
import time

myFinch = Finch('A')

<<<<<<< HEAD
for i in range(0,10):
    myFinch.setBeak(100, 0, 0)
    myFinch.setDisplay(1,2)
    time.sleep(2)
    myFinch.setBeak(0, 200, 0)
=======
for i in range(0,3):
    myFinch.setBeak(100, 25, 0)
    time.sleep(.5)
    myFinch.setBeak(100, 15, 0)
    time.sleep(.5)
    myFinch.playNote(50,1)
    time.sleep(.7)
    myFinch.stopAll()
    myFinch.playNote(50,1)
    time.sleep(.2)
    myFinch.playNote(70,1)
    time.sleep(.2)
    myFinch.playNote(75,1)
>>>>>>> f85370e (Added some lessons)


myFinch.playNote(79,1)
time.sleep(1)
myFinch.playNote(70,1)
time.sleep(2)
myFinch.stopAll()
