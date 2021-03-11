# Lisa Westover
# CS1400 7 week
# Unit4/Task3 Pattern.py

import turtle
import random


# Erases all of the patterns and starts overdef reset
def reset():
    turtle.reset()
    turtle.speed(0)

# configures turtle to draw quickly
#congfigures turtle to have a 1000 x 800 window
def setup():
    turtle.speed(0)
    turtle.setup(1000,800)

#draws a single rectangle given appropriate paramenters
def drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation):
    turtle.penup()
    newHeading = 0
    turtle.goto(centerX, centerY)
    for i in range(0, count + 1):
        turtle.penup()
        turtle.setheading(newHeading)
        if offset >= 0:
            turtle.forward(offset)
        else:
            turtle.backward(offset)

        drawRectangle(width, height, rotation)
        #reset the x and y to draw the shape in a new location
        turtle.penup()
        turtle.goto(centerX, centerY)
        turtle.setheading(0)
        newHeading += int(360/count)
        turtle.setheading(newHeading)
        rotation += 360/count

def drawRectangle(width, height, rotation):

    setRandomColor()
    turtle.setheading(rotation)
    turtle.pendown()
    turtle.forward(height)
    turtle.setheading(rotation - 90)
    turtle.forward(width)
    turtle.setheading(rotation - 180)
    turtle.forward(height)
    turtle.setheading(rotation - 270)
    turtle.forward(width)

# draws the circle in a circular pattern
def drawCirclePattern(centerX, centerY, offset, radius, count):
    newHeading = 0
    turtle.penup()
    turtle.goto(centerX, centerY)

    for i in range(int(count) + 1):
        turtle.penup()
        turtle.setheading(newHeading)
        if offset >= 0:
            turtle.penup()
            turtle.forward(offset)

        else:
            turtle.penup()
            turtle.backward(offset)
        turtle.right(90)
        turtle.pendown()
        setRandomColor()
        turtle.circle(radius)
        # reset the x and y to draw the shape in a new location
        turtle.penup()
        turtle.goto(centerX, centerY)
        turtle.setheading(0)
        newHeading += int(360 / count)
        turtle.setheading(newHeading)



# radomly draws Rectangle and Circle patterns, each based on reasonable random values, some negative
def drawSuperPattern(num):
    randomNum = 0
    for i in range(int(num)):
        randomNum = random.randint(1, 2)
        if randomNum == 1:
            for i in range(7):
                randomeNum = random.randint(-300, 300)
                randomNum2 = random.randint(0, 200)
            drawRectanglePattern(randomNum, randomNum, randomNum, randomNum2, randomNum2, randomNum2, randomNum)
        else:
            randomeNum = random.randint(-300, 300)
            randomNum2 = random.randint(0, 200)
            drawCirclePattern(randNum, randNum, randNum, randNum2, randNum2)


# not using any parameters, set turtle to draw in a random color
def setRandomColor():

    num = random.randint(0, 3)
    if num == 0:
        turtle.color("red")
    elif num == 1:
        turtle.color("blue")
    elif num == 2:
        turtle.color("green")
    else:
        turtle.color("orange")

# called when user quits program, keeps turtle window open
def done():
    turtle.done()


