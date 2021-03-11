# Lisa Westover
# CS1400 7 week
# Unit2/Task2

#bullseye program

import turtle

# Obtain x,y coodinates for bullseye and radius from user
targetX = int(input("Enter the X axis location of the bullseye:"))
targetY = int(input("Enter the Y axis location of the bullseye:"))
radiusCircle = int(input("Enter the radius of the bullseye:"))
newRadiusCircle = radiusCircle + radiusCircle * 1.3

#Draw target

turtle.penup()

# Draw black circle
turtle.goto(targetX, targetY)
turtle.color("black")
turtle.begin_fill()
turtle.circle(newRadiusCircle)
turtle.end_fill()

# Draw blue circle
newRadiusCircle -= radiusCircle * .30
targetY += int(abs(radiusCircle) * .40)
turtle.penup()
turtle.goto(targetX, targetY)
turtle.pendown()
turtle.color("blue")
turtle.begin_fill()
newRadiusCircle -= (newRadiusCircle * .10)
turtle.circle(newRadiusCircle)
turtle.end_fill()

# Draw red circle
newRadiusCircle -= radiusCircle * .20
targetY += int(abs(radiusCircle) * .35)
turtle.penup()
turtle.goto(targetX, targetY)
turtle.pendown()
turtle.color("red")
turtle.begin_fill()
newRadiusCircle -= (newRadiusCircle * .10)
turtle.circle(newRadiusCircle)
turtle.end_fill()

# Draw yellow circle
turtle.penup()
targetY += int(abs(radiusCircle) * .35)
turtle.goto(targetX, targetY)
turtle.pendown()
turtle.color("yellow")
turtle.begin_fill()
turtle.circle(radiusCircle)
turtle.end_fill()
turtle.hideturtle()

turtle.done()

