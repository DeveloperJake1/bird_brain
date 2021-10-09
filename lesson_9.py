# Lesson 9 - Line Tracking
from BirdBrain import Finch 
import time

def PrintSequence(id):
    bird.playNote(79,16)
    time.sleep(.1)
    bird.playNote(81,16)
    time.sleep(.1)
    bird.playNote(88,16)
    time.sleep(.2)

    print("-------------------------------------------------------------------------------------")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    if id == "1":
        bird.setBeak(2, 2, 2)
        print("Running program 1 ---> ('Lesson9'). Please wait.")
    elif id == "2":
        bird.setBeak(2, 2, 2)
        print("Running program 2 ---> (''). Please wait.")
    elif id == "3":
        bird.setBeak(2, 2, 2)
        print("Running program 2 ---> (''). Please wait.")
    else:
        bird.setBeak(100, 2, 2)
        print("Failed to run program. " + id + " is an unknown module id!")
        print("            - You may need to assign this ID to the PrintSequence function if it is not already assigned.")
        print("            - Try again, or check spelling of id. It should be a 1 character long integer.")
        print("            - You may have an error in the script. Check script for bugs.")
    time.sleep(1.5)
    print("")
    print("")
    print("")
    bird.stopAll()
    print("-------------------------------------------------------------------------------------")


bird = Finch()


def Start():

    bird.playNote(79,16)
    time.sleep(.2)
    bird.playNote(81,16)
    time.sleep(.2)
    bird.playNote(82,16)
    time.sleep(.2)
    bird.playNote(81,16)
    time.sleep(.2)
    bird.playNote(79,4)
    time.sleep(.05)
    session = str(input("Which Module would you like to run: "))

    if session == "1":
        PrintSequence(session)
        Lesson9()
    elif session == "2":
         PrintSequence(session)
    else:
        PrintSequence(session)


def Lesson9():

    # Designed to sense whether or not an object is close dependent on the User Input's threshold number.
    # Program stops when the 'A' button is pressed.

    bird.getLine('R')

    threshold = float(input("Threshold (0.01 - 1.00): "))

    while not bird.getButton('A'):
        if (bird.getLine('L') < threshold) or (bird.getLine('R') < threshold):
            print("No items in range.")
            bird.setBeak(100, 0, 0)

        else:
            print("Item Detected.")
            bird.setBeak(0, 30, 100)
            bird.playNote(79,4)

        while bird.getButton('B'):
            bird.setBeak(0,0,0)
            Start()
    else:
        bird.stopAll()




Start()



