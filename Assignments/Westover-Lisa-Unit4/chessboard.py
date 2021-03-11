# Lisa Westover
# CS1400 7 week
# Unit4/Task2- chessboard.py

import turtle

# draw the main outline of the board and call drawAllRectangles to do the inside squares
def drawChessboard(startX, startY, width=250, height=250):
    turtle.getturtle()
    turtle.showturtle()
    turtle.penup()
    turtle.goto(startX, startY)
    turtle.pendown()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)



    #call drawAllRectangles to loop to the squares
    drawAllRectangles(startX, startY, width, height)

# calculate and loop the location for each rectangle then shift and loop again
def drawAllRectangles(startX, startY, width, height):
    squareHeight = float(height / 8)
    squareWidth = float(width / 8)
    newStartX = float(startX)
    newStartY = float(startY)
    turtle.goto(startX, startY + squareHeight)
    for j in range(4):

        for i in range(4):
            # begin drawing squares

            drawRectangle(newStartX, newStartY, squareWidth, squareHeight)

            newStartX = newStartX + squareWidth + squareWidth
        newStartY = newStartY + squareHeight * 2
        newStartX = startX

    newStartX = startX + squareWidth
    newStartY = startY + squareHeight

    for j in range(4):
        for i in range(4):
            drawRectangle(newStartX, newStartY, squareWidth, squareHeight)
            newStartX = newStartX + squareWidth + squareWidth
        newStartY = newStartY + squareHeight * 2
        newStartX = startX + squareWidth

     #turtle.forward(squareWidth * 2)

    print("should be done drawing squares")
    turtle.done

# pass coordinates to create individual rectangle
def drawRectangle(newStartX, newStartY, squareWidth, squareHeight):
    turtle.penup()
    turtle.goto(newStartX, newStartY)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("black")
    turtle.setheading(0)
    turtle.forward(squareWidth)
    turtle.setheading(90)
    turtle.forward(squareHeight)
    turtle.setheading(180)
    turtle.forward(squareWidth)
    turtle.setheading(270)
    turtle.forward(squareHeight)
    turtle.end_fill()
    turtle.left(90)


    # tell turtle to draw a square starting from new xy and square height and width