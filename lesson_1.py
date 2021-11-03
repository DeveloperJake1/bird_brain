# First Lession of the Finch unit
# setMove(F|B, Distance (cm), speed m.100)
# setTurn(R|L, Angle to turn, speed m.100)

from BirdBrain import Finch # Imports the Finch Library

bird = Finch() # Needed to declare the Finch object

bird.setMove('F',bird.convertToCm(5),100) # Moves forward 5 inches quickly



# bird.setMove('B',25,30)  Moves backwards 25 cm slowly

# bird.setTurn('R',90,50) Rotates 90 degrees cm slowly

