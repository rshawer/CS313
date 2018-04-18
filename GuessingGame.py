#  File: GuessingGame.py

#  Description: A guessing game based on the number you think of

#  Student Name: Changjie Lan

#  Student UT EID: cl38442

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created: 11/13/17

#  Date Last Modified: 11/13/15

def main():
    lo=1
    hi=100
    mid=(lo+hi)//2
    guess=0
    response=100
#print the heading of the game and asks if user wants to play
    print("Guessing Game")
    print()
    print("Think of a number between 1 and 100 inclusive.")
    print("And I will guess what it is in 7 tries of less.")
    answer = str(input("Are you ready? (y/n): "))
#starts the sequence of guessing
    if answer=="y":
        while(response!="0"):
         guess+=1
#stops the game after the 7th failed guess
         if (response =="1" or response=="-1") and guess>7:
          print("Either you guessed a number out of range or you had an incorrect entry.")
          break
         if mid==0:
             print("Thank you for playing the Guessing Game.")
             break
         print("Guess",str(guess)+": The number you thought was", mid)
#asks for a valid submission of only -1, 0 ,1
         response = (input("Enter 1 if my guess was high, -1 if low, and 0 if correct: "))
         while response!="0" and response!="-1" and response!="1":
            response = (input("Enter 1 if my guess was high, -1 if low, and 0 if correct: "))
#implements binary search 
         if response == "1":
            hi=mid-1
            mid=(lo+hi)//2
         elif response == "-1":
            lo=mid+1
            mid=(lo+hi)//2
        if response== "0":
           print("Thank you for playing the Guessing Game.")
    else:
        print("Bye")





main()
    
    
