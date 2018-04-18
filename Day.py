
#  File: Day.py

#  Description: A program to determine the day of the week for a certain date

#  Student Name: Changjie Lan

#  Student UT EID: cl38442

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created: 9/23/17

#  Date Last Modified: 9/25/17

def main():
    
    # prompt the user to enter the year

    year=int(input("Enter year: "))
    while(year<1900 or year>2100):
     year=int(input("Enter year: "))

    # prompt the user to enter the month

    month=int(input("Enter month: "))
    while(month<1 or month>12):
     month=int (input("Enter month: "))
         
    #prompt the user to enter the day
     
    day= int(input("Enter day: "))
    while(((month==2 and day>29) or (month==4 and day>30) or (month==6 and day>30) or (month==9 and day>30) or (month==11 and day>30)) or (year%4!=0 and month==2 and day>28) or (year%100==0 and year%400!=0 and month==2 and day>28)):
     day=int(input("Enter day: "))

    #code to calculate the day of the week

 
    b=day
    d=year//100
    if(month>10):
     a=month-2
     c=year%100
    elif(month==1 or month==2):
     a=month+10
     c=year%100-1
     if(year%100==0):
         d=year//100-1
         c=99
    elif(month==3 or month ==4 or month==5 or month==6 or month==7 or month==8 or month==9 or month==10):
     a=month-2
     c=year%100
    

    w = (13 * a - 1 ) // 5 

    x = c // 4 

    y = d // 4 

    z = w + x + y + b + c - 2 * d 

    r = z % 7 

    r = (r + 7) % 7

    

    #code to print the day of the week

    if(r==0):
     r="Sunday"+"."
    elif(r==1):
     r="Monday"+"."
    elif(r==2):
     r="Tuesday"+"."
    elif(r==3):
     r="Wednesday"+"."
    elif(r==4):
     r="Thursday"+"."
    elif(r==5):
     r="Friday"+"."
    elif(r==6):
     r="Saturday"+"."

    print("The day is", r)

main()
