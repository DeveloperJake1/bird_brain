from BirdBrain import Finch # Imports the Finch Library

bird = Finch('A') # Needed to declare the Finch object

print("")
centimeters = float(input("Centimeters: "))
print("Inches: " + str(bird.convertToInch(centimeters)))
