from BirdBrain import Finch # Imports the Finch Library

bird = Finch('A') # Needed to declare the Finch object

print("")
inches = float(input("Inches: "))
print("Centimeters: " + str(bird.convertToCm(inches))) # Returned the converted value of centimeters 
