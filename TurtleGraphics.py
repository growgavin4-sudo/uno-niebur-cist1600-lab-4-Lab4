#TurtleGraphics.py
#Name:Gavin Grow
#Date:2/15/26
#Assignment:

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)
def drawPolygon(pat, sides):
    for s in range(sides):
        pat.forward(50)
        pat.right(360/sides)
def fillCorner(lisa, corner):

    if corner == 1:  # top left
        lisa.begin_fill()
        drawSquare(lisa, 40)
        lisa.end_fill()

    elif corner == 2:  # top right
        lisa.forward(40)
        lisa.begin_fill()
        drawSquare(lisa, 40)
        lisa.end_fill()
        lisa.backward(40)

    elif corner == 3:  # bottom right
        lisa.forward(40)
        lisa.right(90)
        lisa.forward(40)
        lisa.left(90)
        lisa.begin_fill()
        drawSquare(lisa, 40)
        lisa.end_fill()
        
        # move turtle back to original position
        lisa.left(90)
        lisa.backward(40)
        lisa.right(90)
        lisa.backward(40)

    elif corner == 4:  # bottom left
        lisa.right(90)
        lisa.forward(40)
        lisa.left(90)
        lisa.begin_fill()
        drawSquare(lisa, 40)
        lisa.end_fill()

        lisa.left(90)
        lisa.backward(40)
        lisa.right(90)
def squaresInSquares(t, number):
    size = 200          # starting size of biggest square
    shrink = 20         # how much smaller each square gets

    for i in range(number):
        drawSquare(t, size)

        # move inward to keep squares centered
        t.penup()
        t.forward(shrink / 2)
        t.right(90)
        t.forward(shrink / 2)
        t.left(90)
        t.pendown()

        size -= shrink
def main():
    myTurtle = turtle.Turtle()
    # drawPolygon(myTurtle, 5) #draws a pentagon
    drawSquare (myTurtle, 80)
    # drawPolygon(myTurtle, 8) #draws an octogon

    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    fillCorner(myTurtle, 2)
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.
    
    #squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
