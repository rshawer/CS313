#  File: Hailstone.py

#  Description: The Hailstone pattern that turns all number to 1 eventually

#  Student Name: Changjie Lan

#  Student UT EID: cl38442

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created: 9/27

#  Date Last Modified: 9/29


def main():

    #Prompts the user for the range

    start= int(input("Enter starting number of the range: "))
    print()
    end= int(input("Enter ending number of the range: "))
    while((start<0 or end<0) or (start>end)):
     start= int(input("Enter starting number of the range: "))
     print()
     end= int(input("Enter ending number of the range: "))
     
    #The code that counts cycle lengths and implements the hailstone formula by converting numbers to 1
    cycle=0
    for n in range(start, end+1):
     i=n
     counter=0
     while(i>1):
      if(i%2==0):
       i=i//2
       counter=counter+1
      else:
       i=3*i+1
       counter=counter+1
      if(counter>=cycle):
       cycle=counter
       number=n
    
     
    #The print statement

    print()
    print("The number", number,"has the longest cycle length of", str(cycle)+".")
      


main() 
