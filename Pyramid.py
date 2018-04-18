# Analysis: ... 

# Design: ... 

# Coding: Please indent and format your code properly 
# Copy and paste your code to replace the template below 

def main():

 numbercounter=0
 lines = int(input("Enter the number of lines: "))
 for i in range(1,lines+1):
   for j in range((lines+1)-i):
     print(" ", end=" ")
   for j in range(i,0,-1):
       print(j, end=" ")
   for i in range(2,i+1):
       print(i, end=" ")
   print("\n")

main()
