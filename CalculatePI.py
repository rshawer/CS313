#  File: CalculatePI.py

#  Description: Calculate Pi with random numbers based on a conjecture of throwing darts on a dartboard.

#  Student Name: Changjie Lan

#  Student UT EID: cl38442

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created: 10/16/17

#  Date Last Modified: 10/17/17

#import math and random library

import math
import random

# function to compute the throws on the dartboard and see if it fall within the circle. This computation will return a calculated PI.
def computePI ( numThrows ):
 counter=0
 for i in range (1,numThrows+1):
     xPos = random.uniform (-1.0, 1.0)
     yPos = random.uniform (-1.0, 1.0)
     result=math.hypot(xPos, yPos)
     if result<1:
         counter+=1
 calculatedpi = counter/numThrows
 Calculated_Pi = calculatedpi*4
 return Calculated_Pi

#computes the throws based on inputted amount of tries. Prints the calculated Pi and difference.
def main():

    numberthrow=0
    calculatedpi=0
    difference=0
    print("Computation of PI using Random Numbers")
    print()
    for x in range (2,8):
        numberthrow=10**x
        calculatedpi=computePI(numberthrow)
        difference=calculatedpi-math.pi
        print("num = %-10d"%(numberthrow),"Calculated PI = %-10.6f"%(calculatedpi),"Difference = %+.6f"%(difference))
    print()    
    print("Difference = Calculated PI - math.pi")



main()
     
 
