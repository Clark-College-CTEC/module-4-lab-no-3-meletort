# Lab No. 3
# CTEC 121
# Vika Crossland

from graphics import *

def snowman():
    # create the graphics window
    win = GraphWin('Lab 3 - Snowman',800,800)
    
    # your code to draw the snowman goes here
    # draw three circles for the body
    # name the three circles circle1, circle2 and circle3

    circle1 = Circle(Point(400,550),150)
    circle1.setFill("white")
    circle1.draw(win)

    circle2 = Circle(Point(400,320),90)
    circle2.setFill("white")
    circle2.draw(win)

    circle3 = Circle(Point(400,165),70)
    circle3.setFill("white")
    circle3.draw(win)

    # I gave him arms, give me extra credit plz
    
    line1 = Line(Point(315,300),Point(205,400))
    line1.draw(win)

    line2 = Line(Point(488,296),Point(585,392))
    line2.draw(win)
    

    # draw two eyes on the top circle
    # name the two eyes using variables eye1 and eye2

    eye1 = Circle(Point(375, 140),10)
    eye1.setFill("black")
    eye1.draw(win)

    eye2 = Circle(Point(425, 140),10)
    eye2.setFill("black")
    eye2.draw(win)


    # draw a nose using the polygon method and make it orange
    # name the nose using the variable nose

    nose = Polygon(Point(405,161),Point(402,173),Point(429,171))
    nose.setFill("orange")
    nose.draw(win)


    # draw a hat using a rectangle and fill it with black
    # name the hat using the variable hat


    hat = Rectangle(Point(350,26),Point(450,93))
    hat.setFill("black")
    hat.draw(win)

    # draw a line to represent the rim of the hat using a line
    # name the line using the variable hatline

    line = Line(Point(300,95),Point(500,95))
    line.setWidth(15)
    line.draw(win)

    # close the program
    input('Press enter to quit the program ')
    # close the graphics window
    win.close()


# Call the snowman() function to start the program
snowman()