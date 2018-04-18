#  File: EasterSunday.py

#  Description: Gauss' formula to figure out the day of Easter Sunday

#  Student Name: Changjie Lan

#  Student UT EID: cl38442

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created: 9/17/17

#  Date Last Modified: 9/17/17

def main():

#the code to prompt the user for the year
    y=int(input("Enter the Year: "))
          


#the code to determine Easter Sunday according to Gauss
    a=y%19
    b=y//100
    c=y%100
    d=b//4
    e=b%4
    g=(8*b+13)//25
    h=(19*a+b-d-g+15)%30
    j=c//4
    k=c%4
    m=(a+11*h)//319
    r=(2*e+2*j-k-h+m+32)%7
    n=(h-m+r+90)//25
    p=(h-m+r+n+19)%32
    
#the code to print out the year and month
    print()
    if(n==3):
          print("In", y, "Easter Sunday is on", p, "March.")
    if(n==4):
          print("In", y, "Easter Sunday is on", p, "April.")

main()
