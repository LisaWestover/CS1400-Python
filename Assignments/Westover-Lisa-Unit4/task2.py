# Lisa Westover
# CS1400 7 week
# Unit4/Task2


# Chess Board
from chessboard import drawChessboard

def main():
    # Add Code to get input from user
    startX, startY = eval(input("Enter the location to draw the chessboard (x, y):"))
    height = input("Enter height:")
    width = input("Enter width:")
    #### End Add Import Statement(s) ####

    if width == "" and height == "":
        drawChessboard(startX, startY)
    elif height == "":
        drawChessboard(startX, startY, width=eval(width))
    elif width == "":
        drawChessboard(startX, startY, height=eval(height))
    else:
        drawChessboard(startX, startY, eval(width), eval(height))

main()