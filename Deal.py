# File: Deal.py

# Description: A code that proves that switching in the Monty Hall game wins 66% of the time.

# Student Name: Changjie Lan

# Student UT EID: cl38442

# Course Name: CS 303E

# Unique Number: 51345

# Date Created: 10/18/17

# Date Last Modified: 10/19/17

#imports the random library

import random

#creates the formatting for the categories 
def main():
    time = int(input("Enter number of times you want to play: "))
    print()
    print(format("  Prize","<13s"),end="")
    print(format("Guess","<12s"),end="")
    print(format("View","<8s"),end="")
    print(format("New Guess","9s"),end="")
    print()

    prize=0
    guess=0
    view=0
    newGuess=0
    counter=0

#code that sets the prize and guess randomly
    
    for i in range (1,time+1):
        prize=random.randint(1,3)
        guess=random.randint(1,3)

#determines what the view and new guess will be based on prize and guess
        
        if(prize==2 and guess==3) or (prize==3 and guess==2) or (prize==3 and guess==3):
            view=1
        elif(prize==1 and guess==1) or (prize==1 and guess==3) or (prize==3 and guess==1):
            view=2
        else:
            view=3
        if((guess==2 and view==3) or (guess==3 and view==2)):
            newGuess=1
        elif((guess==1 and view==3) or (guess==3 and view==1)):
            newGuess=2
        else:
            newGuess=3
        if(newGuess==prize):
            counter+=1

#prints everything out and determines the winning probability 
        print("   ","%-10d"%(prize),"%-10d"%(guess),"%-10d"%(view),"%-5d"%(newGuess))
    print()
    winratio=round(counter/time,2)
    loseratio=round(1-winratio,2)
    print("Probability of winning if you switch =","%0.2f"%(winratio))
    print("Probability of winning if you do not switch =","%0.2f"%(loseratio))
        
        

















main()
