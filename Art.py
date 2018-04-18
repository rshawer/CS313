#  File: Art.py

#  Description: Recursive Art, star, cross, balls

#  Student Name: Changjie Lan

#  Student UT EID: cl38442

#  Course Name: CS 313E

#  Unique Number: 51340

#  Date Created: 3/1/18

#  Date Last Modified: 3/2/18

import os
import math
import turtle
def draw_line(ttl, x1, y1, x2, y2, color):
    ttl.penup()
    ttl.color(color)

    ttl.goto(x1,y1)
    ttl.pendown()
    ttl.goto(x2,y2)
    ttl.penup()
def drawPolygon (ttl, x, y, num_side, radius):
  sideLen = 2 * radius * math.sin (math.pi / num_side)
  angle = 360 / num_side
  ttl.penup()
  ttl.goto (x, y)
  ttl.pendown()
  for iter in range (num_side):
    ttl.forward (sideLen)
    ttl.left (angle)
def stars(ttl,length):
  for i in range(5):
    ttl.forward(length)
    ttl.right(144)
def web(ttl,order):
  if order>0:
    for i in range (0,10):
      ttl.forward(600)
      ttl.left(123)
    web(ttl,order-1)
#gasket
# draw a line from point p1 to point p2
def drawLine (ttl, p1, p2):
  x1 = p1[0]
  y1 = p1[1]
  x2 = p2[0]
  y2 = p2[1]
  ttl.penup()
  ttl.goto (x1, y1)
  ttl.pendown()
  ttl.goto (x2, y2)
  ttl.penup()

# returns the midway between two points
def midpoint (p1, p2):
  p = [0, 0]
  p[0] = (p1[0] + p2[0]) // 2
  p[1] = (p1[1] + p2[1]) // 2
  return p

# draw gasket recursively
def draw_gasket (ttl, order, p1, p2, p3):
  drawLine (ttl, p1, p2)
  drawLine (ttl, p2, p3)
  drawLine (ttl, p3, p1)

  if (order > 0):
    # find mid points of each of the sides
    q1 = midpoint (p1, p2)
    q2 = midpoint (p2, p3)
    q3 = midpoint (p3, p1)
    # recursively draw the other triangles
    draw_gasket (ttl, order - 1, p1, q1, q3)
    draw_gasket (ttl, order - 1, p2, q1, q2)
    draw_gasket (ttl, order - 1, p3, q2, q3)
#recursive draw circles that stack like a tower
def drawCircle (ttl, order):
  if order>0:
    ttl.color("red")
    ttl.begin_fill()
    ttl.circle(15)
    ttl.end_fill()
    ttl.right(36)
    ttl.forward(10+order*2)
    ttl.color("orange")
    ttl.begin_fill()
    ttl.circle(15)
    ttl.end_fill()
    ttl.right(36)
    ttl.forward(10+order*2)
    ttl.color("green")
    ttl.begin_fill()
    ttl.circle(15)
    ttl.end_fill()
    ttl.right(36)
    ttl.forward(10+order*2)
    ttl.color("navy blue")
    ttl.begin_fill()
    ttl.circle(15)
    ttl.end_fill()
    ttl.right(36)
    ttl.forward(10+order*2)
    ttl.color("indigo")
    ttl.begin_fill()
    ttl.circle(15)
    ttl.end_fill()
    ttl.right(36)
    ttl.forward(10+order*2)
    ttl.color("magenta")
    ttl.begin_fill()
    ttl.circle(15)
    ttl.end_fill()
    ttl.right(36)
    ttl.forward(10+order*2)
    ttl.color("yellow")
    ttl.begin_fill()
    ttl.circle(15)
    ttl.end_fill()
    ttl.right(36)
    ttl.color("red")
    ttl.begin_fill()
    ttl.circle(15)
    ttl.end_fill()
    ttl.right(36)
    ttl.forward(10+order*2)
    ttl.color("orange")
    ttl.begin_fill()
    ttl.circle(15)
    ttl.end_fill()
    ttl.right(36)
    ttl.forward(10+order*2)
    ttl.color("green")
    ttl.begin_fill()
    ttl.circle(15)
    ttl.end_fill()
    ttl.right(36)
    ttl.forward(10+order*2)
    drawCircle(ttl, order-1)

def main():
  # prompt the user to enter an order for the gasket
  print("Recursive Art")
  print()
  order = int (input ('Enter a level of recursion between 1 and 6: '))
  while(order>6 or order<1):
      order = int (input ('Enter a level of recursion between 1 and 6: '))
  turtle.tracer(10000)
  # put label on top of page
  turtle.title ('Recursive Art Cross and Star')

  # setup screen size
  turtle.setup (800, 800, 0, 0)

  # create a turtle object
  ttl = turtle.Turtle()
  ttl.speed("fastest")
  background=turtle.Screen()
  background.bgcolor("blue")
  # draw a circle
  ttl.penup()
  ttl.goto (0, -50)
  ttl.pendown()
  ttl.color("DarkRed")
  ttl.begin_fill()
  ttl.circle (150)
  ttl.end_fill()
  ttl.penup()
  ttl.goto(0,-40)
  ttl.pendown()
  #draw a cricle make it white
  ttl.color("white")
  ttl.begin_fill()
  ttl.circle(140)
  ttl.end_fill()
  ttl.penup()
  ttl.goto(0,-30)
  ttl.pendown()
  #draw orange circle
  ttl.color("orange")
  ttl.begin_fill()
  ttl.circle(130)
  ttl.end_fill()
  #draw octagon
  ttl.color("orange red")
  ttl.begin_fill()
  drawPolygon(ttl,-45,-15,8,120)
  ttl.end_fill()
  #draw star
  ttl.color("yellow")
  ttl.penup()
  ttl.goto(-75,125)
  ttl.pendown()
  ttl.begin_fill()
  stars(ttl,150)
  ttl.end_fill()
  ttl.pensize(8)
  #draw cross
  draw_line(ttl,-50,-400,-50,-40, "black")
  draw_line(ttl,50,-400,50,-40, "black")
  draw_line(ttl,-50,245,-50,400, "black")
  draw_line(ttl,50,245,50,400, "black")
  draw_line(ttl,-400,50,-145,50, "black")
  draw_line(ttl,-400,150,-145,150, "black")
  draw_line(ttl,145,50,400,50, "black")
  draw_line(ttl,145,150,400,150, "black")
  ttl.color("violet")
  #draw recursive web
  ttl.pensize(4)
  ttl.penup()
  ttl.goto(-300,-50)
  ttl.pendown()
  web(ttl,order)
  ttl.pensize(1)
  #draw gasket in star
  ttl.color("red")
  p1 = [0, 105]
  p2 = [-12, 88]
  p3 = [12, 88]
  draw_gasket(ttl, 2, p1, p2, p3)
  ttl.penup()
  ttl.goto(-300,-300)
  ttl.pendown()
  #draw stacking circles like a tower recursively
  drawCircle(ttl, order)
  ttl.penup()
  ttl.goto(0,-200)
  ttl.pendown()
  drawCircle(ttl, order)
  ttl.penup()
  ttl.goto(250,-250)
  ttl.pendown()
  drawCircle(ttl,order)
  ttl.penup()
  ttl.goto(-280,100)
  ttl.pendown()
  drawCircle(ttl,order)
  ttl.penup()
  ttl.goto(-230,300)
  ttl.pendown()
  drawCircle(ttl,order)
  ttl.penup()
  ttl.goto(0,300)
  ttl.pendown()
  drawCircle(ttl,order)
  ttl.penup()
  ttl.goto(250,300)
  ttl.pendown()
  drawCircle(ttl,order)
  ttl.penup()
  ttl.goto(250,20)
  ttl.pendown()
  drawCircle(ttl,order)
  ttl.penup()
  ttl.goto(-150,-100)
  ttl.pendown()
  drawCircle(ttl,order)
  ttl.penup()
  # persist drawing
  outName = os.path.basename(__file__)[:-2]+'eps'
  turtScrn = turtle.getscreen()
  turtScrn.getcanvas().postscript(file=outName)

main()
