#  File: Goldbach.py

#  Description: Goldbach's conjecture to find the prime sums of any even number greater than or equal to four

#  Student Name: Changjie Lan

#  Student UT EID: cl38442

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created: 10/11/2017

#  Date Last Modified: 10/13/2017

# code to determine if a number is prime
import math

def is_prime (n):
  if (n == 1):
    return False
  limit = int (n ** 0.5) + 1
  div = 2
  while (div < limit):
    if (n % div == 0):
      return False
    div += 1
  return True

#code to prompt the user to submit a valid upper and lower limit

def main():
    lower = int(input("Enter the lower limit: "))
    upper = int(input("Enter the upper limit: "))
    while(upper<=lower or upper%2!=0 or lower%2!=0 or lower<4):
        lower = int(input("Enter the lower limit: "))
        upper = int(input("Enter the upper limit: "))

#code to determine the sums of even numbers above 4, and print them out
    
    for i in range(lower,upper+1):
     n=i
     if n%2==0:
         print (i, end=" ")
         for c in range(2,n):
                  if is_prime (c):
                    if is_prime (n-c) and (n-c)>=c:
                      print("=", c, "+", (n-c), end=" ")
         print()
     
 
main()
