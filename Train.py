#  File: Train.py

#  Description: Draws a train using turtle

#  Student Name: Changjie Lan

#  Student UT EID: cl38442

#  Course Name: CS 313E

#  Unique Number: 51340

#  Date Created: 2/13/18

#  Date Last Modified: 2/14/18

import turtle

def draw_line(ttl, x1, y1, x2, y2, color):
    ttl.penup()
    ttl.pensize(2)
    ttl.color(color)

    ttl.goto(x1,y1)
    ttl.pendown()
    ttl.goto(x2,y2)
    ttl.penup()


def draw_wheels(ttl, x, y, larger_r, smaller_r):
    spk = turtle.Turtle()
    spk.speed(0)
    spk.penup()
    spk.goto(x, y + larger_r - smaller_r)

    spk.color("red")
    ttl.color("red")
	
    ttl.penup()
    ttl.setheading(0)
	
    ttl.goto(x, y)
    ttl.pendown()
    ttl.circle(larger_r)
    ttl.penup()

    spoke_angle = 5
    for r in range(2):
	    for q in range(9):
		    spk.goto(x, y + larger_r - smaller_r)
		    spk.pendown()
		    spk.circle(smaller_r, q * 45)
		    ttl.goto(x, y + smaller_r)
		    ttl.pendown()
		    ttl.circle(larger_r - smaller_r, spoke_angle)
		    ttl.goto(spk.position())
		    spk.penup()
		    ttl.penup()
		    spoke_angle += 45
		    spk.setheading(0)
		    ttl.setheading(0)
	    spoke_angle = -5

    spk.ht()
    ttl.ht()

def draw_dots(ttl,linelength, dotsize, lengthspace):
    ttl.pencolor("black")
    ttl.forward(6)
    for i in range(linelength):
        ttl.pendown()
        ttl.forward(dotsize)
        ttl.penup()
        ttl.forward(lengthspace)

def Rectangle(ttl, x1, y1, x2, y2, x3, y3, x4, y4, tilt):
    ttl.penup()
    ttl.pensize(2)
    ttl.color("blue")
    ttl.goto(x1,y1)
    ttl.pendown()
    ttl.goto(x2,y2)
    ttl.penup()
    ttl.tilt(90)
    ttl.goto(x2,y2)
    ttl.pendown()
    ttl.goto(x3, y3)
    ttl.penup()
    ttl.tilt(90)
    ttl.goto(x3,y3)
    ttl.pendown()
    ttl.goto(x4, y4)
    ttl.penup()
    ttl.tilt(90)
    ttl.goto(x4,y4)
    ttl.pendown()
    ttl.goto(x1, y1)
    ttl.penup()
    
def windows(ttl,x1,y1,x2,y2,x3,y3,x4,y4,tilt):
    ttl.penup()
    ttl.pensize(2)
    ttl.color("blue")
    ttl.fillcolor("gray")
    ttl.begin_fill()
    ttl.goto(x1,y1)
    ttl.pendown()
    ttl.goto(x2,y2)
    ttl.penup()
    ttl.tilt(90)
    ttl.goto(x2,y2)
    ttl.pendown()
    ttl.goto(x3,y3)
    ttl.penup()
    ttl.tilt(90)
    ttl.goto(x3,y3)
    ttl.pendown()
    ttl.goto(x4,y4)
    ttl.penup()
    ttl.tilt(90)
    ttl.goto(x4,y4)
    ttl.pendown()
    ttl.goto(x1,y1)
    ttl.penup()
    ttl.end_fill()

def ridges(ttl, x1, y1, x2, y2, x3, y3, x4, y4, color):
    for i in range (0,13):
        ttl.penup()
        ttl.pensize(2)
        ttl.color(color)
        ttl.goto(x1,y1)
        ttl.pendown()
        ttl.goto(x2,y2)
        ttl.penup()
        ttl.goto(x2,y2)
        ttl.pendown()
        ttl.goto(x3,y3)
        ttl.penup()
        ttl.goto(x3,y3)
        ttl.pendown()
        ttl.goto(x4,y4)
        ttl.penup()
        ttl.goto(x4,y4)
        ttl.pendown()
        ttl.goto(x1,y1)
        ttl.penup()
        x1+=52.5
        x2+=52.5
        x3+=52.5
        x4+=52.5
        

def main():
    #screen size
    turtle.setup(800,800,0,0)
    ttl=turtle.Turtle()
    #draw the four lines in the body of the train
    draw_line(ttl, -395, 115, -175, 115,"blue")
    draw_line(ttl, -175, 115, -175, 125, "blue")
    draw_line(ttl, -175,125,-395,125,"blue")
    draw_line(ttl, -395,125, -395, 115, "blue")
    ttl.goto(-375, 115)
    ttl.pendown()
    ttl.goto(-375, -100)
    ttl.goto(-350, -100)
    ttl.left(90)
    #draw the first half circle
    ttl.circle(-60, 180)
    ttl.goto(-200, -100)
    ttl.goto(-200, 115)
    ttl.goto(-200, -100)
    ttl.goto(-150, -100)
    ttl.circle(50,-180)
    ttl.goto(10, -100)
    #draw the second half circle
    ttl.circle(-50,180)
    ttl.goto(175, -100)
    ttl.penup()
    ttl.goto(-200, 65)
    ttl.pendown()
    #finish drawing general shape of the body
    ttl.goto(175, 65)
    ttl.goto(175,-100)
    ttl.goto(175, -10)
    ttl.goto(-200,-10)
    ttl.goto(-200,-20)
    ttl.goto(175, -20)
    ttl.goto(175, -85)
    ttl.goto(215,-85)
    ttl.goto(250,-125)
    ttl.goto(175,-125)
    ttl.goto(175,-85)
    #draw the rectangle and the bottom curved nose area
    Rectangle(ttl, 175, -70, 200, -70, 200, 45, 175, 45, 90)
    Rectangle(ttl, 200, -35, 210, -35, 210, 15, 200, 15, 90)
    #draw the windows
    windows(ttl, -350, 90, -300,90, -300, 30, -350, 30, 90)
    windows(ttl, -275, 90, -225,90, -225, 30, -275, 30, 90)
    #draw the top hat of the train
    ttl.penup()
    ttl.goto(65,65)
    ttl.pendown()
    ttl.goto(45,125)
    ttl.goto(55, 145)
    ttl.penup()
    ttl.goto(55, 145)
    ttl.pendown()
    ttl.goto(110, 145)
    ttl.goto(120, 125)
    ttl.goto(100, 65)
    ttl.penup()
    ttl.goto(45,125)
    ttl.heading()
    ttl.pendown()
    ttl.goto(120,125)
    ttl.penup()
    #draw the samller rectangle hat on top of the train
    Rectangle(ttl, -75, 90, -25, 90, -25, 65, -75, 65, 90)
    Rectangle(ttl, -65, 100, -35, 100, -35, 90, -65, 90, 90)
    #draw the lines that are inside the train
    draw_line(ttl,-100,65,-90, 65, "blue")
    draw_line(ttl,-90, 65, -90, -10, "blue")
    draw_line(ttl, -90, -10, -100, -10, "blue")
    draw_line(ttl, -100, -10, -100, 65, "blue")
    ttl.penup()
    ttl.goto(75,-25)
    ttl.pendown()
    #draw the other small lines in the train 
    draw_line(ttl, 75, 65, 85, 65, "blue")
    draw_line(ttl, 85, 65, 85, -10, "blue")
    draw_line(ttl, 85, -10, 75, -10, "blue")
    draw_line(ttl, 75, -10, 75, 65, "blue")
    ttl.penup()
    ttl.goto(-200,-15)
    ttl.left(90)
    ttl.pensize(5)
    #draw the samll dots inside the stripes
    draw_dots(ttl, 46, 1, 7)
    ttl.penup()
    ttl.goto(-95,70)
    ttl.setheading(-90)
    ttl.pensize(5)
    draw_dots(ttl, 10, 1, 7)
    ttl.penup()
    ttl.goto(80,70)
    ttl.setheading(-90)
    ttl.pensize(5)
    #draw the small dots in the other stripe, right most
    draw_dots(ttl, 10, 1, 7)
    ttl.penup()
    ttl.pensize(2)
    #draw all the wheels
    draw_wheels(ttl,-288,-150, 50, 10)
    draw_wheels(ttl,-100,-150, 45, 9)
    draw_wheels(ttl,60,-150, 45, 9)
    ttl.penup()
    ttl.pencolor("black")
    #draw the tracks
    ttl.pensize(2)
    draw_line(ttl, -395,-150,310,-150,"black")
    draw_line(ttl, -395,-160,310,-160,"black")
    #draw the ridges
    ridges(ttl, -380, -160, -380, -165, -355, -165, -355, -160, "black")
    turtle.done()


main()
