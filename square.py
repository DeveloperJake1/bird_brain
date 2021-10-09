from BirdBrain import Finch # Imports the Finch Library

bird = Finch('A') # Needed to declare the Finch object

# Creates 2 squares

for i in range (2):
    for i in range(4):
        bird.setBeak(0,100,0)
        bird.setMove('F',5,10)
        bird.setBeak(100,80,0)
        bird.setTurn('L',90,100)
bird.setBeak(0,0,0)

