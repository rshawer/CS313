# Analysis: ... 

# Design: ... 

# Coding: Please indent and format your code properly 
# Copy and paste your code to replace the template below 

def main():
 import random
 you= int(input("scissor (0), rock (1), paper (2): "))
 computer=random.randint(0,2)
 if(computer==0 and you==1):
  print("The computer is scissor. You are rock. You won.")
 elif(computer==0 and you==2):
  print("The computer is scissor. You are paper. You lost.")
 elif(computer==1 and you==0):
  print("The computer is rock. You are scissor. You lost.")
 elif(computer==1 and you==2):
  print("The computer is rock. You are paper. You won.")
 elif(computer==2 and you==0):
  print("The computer is paper. You are scissor. You won.")
 elif(computer==2 and you==1):
  print("The computer is paper. You are rock. You lost.")
 elif(you==computer):
  if(you==0):
   print("The computer is scissor. You are scissor too. It is a draw.")
  elif(you==1):
   print("The computer is rock. You are rock too. It is a draw.")
  else:
   print("The computer is paper. You are paper too. It is a draw.")

main()
