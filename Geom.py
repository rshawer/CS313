#  File: Geom.py

#  Description: Code to figure out basic features of two gemoetric shapes 

#  Student Name: Changjie Lan

#  Student UT EID: cl38442

#  Partner Name: Samuel Gutierrez

#  Partner UT EID: sfg384

#  Course Name: CS 313E

#  Unique Number: 51340

#  Date Created: 2/1/18

#  Date Last Modified: 2/1/18

import math

class Point (object):
  # constructor 
  def __init__ (self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get distance
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # get a string representation of a Point object
  def __str__ (self):
    return '(' + str(self.x) + ", " + str(self.y) + ")"

  # test for equality
  def __eq__ (self, other):
    tol = 1.0e-16
    return ((abs (self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

class Circle (object):
  # constructor
  def __init__ (self, radius = 1, x = 0, y = 0):
    self.radius = radius
    self.center = Point (x, y)

  # compute cirumference
  def circumference (self):
    return 2.0 * math.pi * self.radius

  # compute area
  def area (self):
    return math.pi * self.radius * self.radius

  # determine if point is strictly inside circle
  def point_inside (self, p):
    return (self.center.dist(p) < self.radius)

  # determine if a circle is strictly inside this circle
  def circle_inside (self, c):
    distance = self.center.dist (c.center)
    return (distance + c.radius) < self.radius

  # determine if a circle c intersects this circle (non-zero area of overlap)
  def does_intersect (self, c):
    distance = self.center.dist (c.center)
    return (distance<(self.radius+c.radius))
  # determine the smallest circle that circumscribes a rectangle
  # the circle goes through all the vertices of the rectangle
  def circle_circumscribes (self, r):
    x=(r.ul.x+r.lr.x)/2
    y=(r.ul.y+r.lr.y)/2
    center=Point(x,y)
    radius=round(center.dist(r.ul),2)
    new_circle=Circle(radius,x,y)
    return new_circle
  # string representation of a circle
  def __str__ (self):
    return "("+str(self.center.x)+","+str(self.center.y)+") : "+str(self.radius)

  # test for equality of radius
  def __eq__ (self, other):
    tol = 1.0e-16
    return (abs (self.radius-other.radius)<tol)
class Rectangle (object):
  # constructor
  def __init__ (self, ul_x = 0, ul_y = 1, lr_x = 1, lr_y = 0):
    if ((ul_x < lr_x) and (ul_y > lr_y)):
      self.ul = Point (ul_x, ul_y)
      self.lr = Point (lr_x, lr_y)
    else:
      self.ul = Point (0, 1)
      self.lr = Point (1, 0)

  # determine length of Rectangle (distance along the x axis)
  def length (self):
      return abs(self.lr.x - self.ul.x)

  # determine width of Rectangle (distance along the y axis)
  def width (self):
      return abs(self.ul.y - self.lr.y)
  # determine the perimeter
  def perimeter (self):
    return 2*self.width()+2*self.length()
  # determine the area
  def area (self):
    return self.width()*self.length()

  # determine if a point is strictly inside the Rectangle
  def point_inside (self, p):
    return (self.ul.x<p.x and p.x<self.lr.x) and (self.lr.y<p.y and p.y<self.ul.y)
  # determine if another Rectangle is strictly inside this Rectangle
  def rectangle_inside (self, r):
    return self.point_inside(r.ul) and self.point_inside(r.lr)
  # determine if two Rectangles overlap (non-zero area of overlap)
  def does_intersect (self, other):
    outside=(other.ul.x>=self.lr.x) or (other.lr.x<=self.ul.x) or (other.ul.y<=self.lr.y) or (other.lr.y>=self.ul.y)
    return not (outside)
  # determine the smallest rectangle that circumscribes a circle
  # sides of the rectangle are tangents to circle c
  def rect_circumscribe (self, c):
    ul_x=c.center.x-c.radius
    ul_y=c.center.y+c.radius
    lr_x=c.center.x+c.radius
    lr_y=c.center.y-c.radius
    new_rectangle=Rectangle(ul_x,ul_y,lr_x,lr_y)
    return new_rectangle
  # give string representation of a rectangle
  def __str__ (self):
    return "("+str(self.ul.x)+","+str(self.ul.y)+") : ("+str(self.lr.x)+","+str(self.lr.y)+")"
  # determine if two rectangles have the same length and width
  def __eq__ (self, other):
     tol=1.0e-16
     return (abs(self.length()-other.length())<tol) and (abs(self.width()-other.width())<tol)
def main():
  # open the file geom.txt
  file_data = open('geom.txt', 'r')
  # create Point objects P and Q
  line = file_data.read()
  line = line.split()
  y = []
  for x in line:
    if x[0:1].isdigit() or x[0:1]=="-":
      y.append(float(x))
    
  p_coordinates = (y[0]) ,(y[1])
  q_coordinates = (y[2]) ,(y[3])
  c_center_radius = y[4] , y[5] , y[6]
  d_center_radius = y[7] , y[8] , y[9]
  G_ul_lr = y[10] ,  y[11] , y[12] , y[13]
  H_ul_lr = y[14] , y[15] , y[16] , y[17]

  
  #create point objects P and Q
  object_p = Point(p_coordinates[0],p_coordinates[1])
  object_q = Point(q_coordinates[0],q_coordinates[1])
  
  # print the coordinates of the points P and Q
  print("Coordinates of P:",object_p)
  print("Coordinates of Q:",object_q)
  
  # find the distance between the points P and Q
  distance =object_p.dist(object_q)
  print("Distance between P and Q:",round(distance,2))
  # create two Circle objects C and D
  object_c = Circle(c_center_radius[2],c_center_radius[0],c_center_radius[1])
  object_d = Circle(d_center_radius[2],d_center_radius[0],d_center_radius[1])
  # print C and D
  print("Circle C:",object_c)
  print("Circle D:",object_d)
  # compute the circumference of C
  circumference_c = object_c.circumference()
  print("Circumference of C:",round(circumference_c,2))
  # compute the area of D
  area_d = object_d.area()
  print("Area of D:",round(area_d,2))
  # determine if P is strictly inside C
  p_inside_c = object_c.point_inside(object_p)
  if p_inside_c==True:
   print("P is inside C")
  else:
   print("P is not inside C")
  # determine if C is strictly inside D
  c_inside_d = object_d.circle_inside(object_c)
  if c_inside_d==True:
    print("C is inside D")
  else:
    print("C is not inside D")
  # determine if C and D intersect (non zero area of intersection)
  c_intersect_d = object_d.does_intersect(object_c)
  if c_intersect_d==True:
    print("C does intersect D")
  else:
    print("C does not intersect D")
  # determine if C and D are equal (have the same radius)
  if object_c.radius == object_d.radius:
    print("C is equal to D")
  else:
    print("C is not equal to D")
  # create two rectangle objects G and H
  rectangle_g=Rectangle(G_ul_lr[0],G_ul_lr[1],G_ul_lr[2],G_ul_lr[3])
  rectangle_h=Rectangle(H_ul_lr[0],H_ul_lr[1],H_ul_lr[2],H_ul_lr[3])
  # print the two rectangles G and H
  print("Rectangle G:",rectangle_g)
  print("Rectangle H:",rectangle_h)
  # determine the length of G (distance along x axis)
  print("Length of G:",rectangle_g.length())
  # determine the width of H (distance along y axis)
  print("Width of H:",rectangle_h.width())
  # determine the perimeter of G
  print("Perimeter of G:",rectangle_g.perimeter())
  # determine the area of H
  print("Area of H:",rectangle_h.area())
  # determine if point P is strictly inside rectangle G
  if(rectangle_g.point_inside(object_p)):
    print("P is inside G")
  else:
    print("P is not inside G")
  # determine if rectangle G is strictly inside rectangle H
  if(rectangle_h.rectangle_inside(rectangle_g)):
    print("G is inside H")
  else:
    print("G is not inside H")
  # determine if rectangles G and H overlap (non-zero area of overlap)
  if(rectangle_h.does_intersect(rectangle_g)):
    print("G does overlap H")
  else:
    print("G does not overlap H")
  # find the smallest circle that circumscribes rectangle G
  my_circle = object_c.circle_circumscribes(rectangle_g)
  print("Circle that circumscribes G:",my_circle)
  # goes through the four vertices of the rectangle
  # find the smallest rectangle that circumscribes circle D
  my_rectangle= rectangle_g.rect_circumscribe(object_d)
  print("Rectangle that circumscribes D:", my_rectangle)
  # all four sides of the rectangle are tangents to the circle
  # determine if the two rectangles have the same length and width
  if(rectangle_g.__eq__(rectangle_h)):
    print("Rectangle G is equal to H")
  else:
    print("Rectangle G is not equal to H")
  # close the file geom.txt
  file_data.close()
main()
