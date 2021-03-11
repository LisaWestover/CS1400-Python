# Lisa Westover
# CS1400 7 week
# Unit2/Task3

#Calculate area of a regular polygon program

import turtle
import math

# Obtain polygon length and number of sides from user
polygonLength = float(turtle.numinput("Length", "Please enter the length of each side of the polygon:"))
polygonSides = float(turtle.numinput("Sides", "Please enter the number of sides for this polygon:"))

# Calculate Area
polygonArea = polygonSides * math.pow(polygonSides, 2) / 4 * math.tan(math.pi / polygonSides)

print("The area for your polygon with a length of", polygonLength, " and ", polygonSides, "is: ", round(polygonArea, 5))

