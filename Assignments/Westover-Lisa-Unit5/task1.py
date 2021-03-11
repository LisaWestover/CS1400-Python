# Lisa Westover
# CS1400 7 week
# Unit5/Task1

import turtle


class Face:
    def __init__(self):
        self.__smile = True
        self.__happy = True
        self.__darkEyes = True

    def draw_face(self):
        turtle.clear()
        self.__drawHead()
        self.__drawEyes()
        self.__drawMouth()

    def __drawHead(self):
        #code for drawing the head
        turtle.penup()
        turtle.goto(0,0)
        turtle.pendown()
        turtle.color("yellow" if self.__happy else "red")
        turtle.begin_fill()
        turtle.setheading(0)
        turtle.circle(100)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(0,0)
        turtle.setheading(0)

    def __drawEyes(self):
        #code for drwing the eyes
        turtle.penup()
        turtle.goto(0,0)
        turtle.goto(-20, 110)
        turtle.pendown()
        turtle.begin_fill()
        turtle.color("black" if self.__darkEyes else "blue")
        turtle.circle(5)
        turtle.penup()
        turtle.goto(20,110)
        turtle.pendown()
        turtle.circle(5)
        turtle.end_fill()
        turtle.penup()


    def __drawMouth(self):
        #code for drawing mouth
        turtle.penup()
        turtle.goto(0,0)
        turtle.goto(-40, 65) if self.__smile else turtle.goto(40, 45)
        turtle.pendown()
        turtle.width(15)
        turtle.pendown()
        turtle.pencolor("black")
        turtle.setheading(-90) if self.__smile else turtle.setheading(90)
        turtle.circle(40, 180)
        turtle.width(4)
        turtle.penup()
        turtle.goto(0,0)


    def isSmile(self):
        return self.__smile

    def isHappy(self):
        return self.__happy

    def isDarkEyes(self):
        return self.__darkEyes

    def changeMouth(self):
        self.__smile = not self.__smile
        self.draw_face()

    def changeEmotion(self):
        self.__happy = not self.__happy
        self.draw_face()

    def changeEyes(self):
        self.__darkEyes = not self.__darkEyes
        self.draw_face()


def main():
    face = Face()
    face.draw_face()

    done = False

    while not done:
        print("Change My Face")
        mouth = "frown" if face.isSmile() else "smile"
        emotion = "angry" if face.isHappy() else "happy"
        eyes = "blue" if face.isDarkEyes() else "black"
        print("1) Make me", mouth)
        print("2) Make me", emotion)
        print("3) Make my eyes", eyes)
        print("0) Quit")
        print(face.isSmile())

        menu = eval(input("Enter a selection: "))

        if menu == 1:
            face.changeMouth()
        elif menu == 2:
            face.changeEmotion()
        elif menu == 3:
            face.changeEyes()
        else:
            break

    print("Thanks for Playing")

    turtle.hideturtle()
    turtle.done()


main()
