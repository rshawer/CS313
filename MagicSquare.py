  #File: MagicSquare.py

  #Description: create a magic square of a odd number

  #Student's Name: Changjie Lan

  #Student's UT EID: cl38442
 
  #Partner's Name:

  #Partner's UT EID:

  #Course Name: CS 313E 

  #Unique Number: 51340

  #Date Created: 1/22/2018

  #Date Last Modified: 1/26/2018

# Populate a 2-D list with numbers from 1 to n2
def make_square ( n ):
# arrange the numbers in order to be a magic square
   magic_square=[]
   new=[]
   for a in range (0,n):
       for b in range (0,n):
         new.append(0)
       magic_square.append(new)
       new=[]
   k=1
   i=n-1
   j=n//2
   for k in range (1,n**2+1):
      if magic_square[i][j]!=0:
         i=i-2
         j=j-1
      if magic_square[i][j]==0:
          magic_square[i][j]=k
          i=i+1
          j=j+1
          if i>=n and j<n:
            i=0
          if i<n and j>=n:
            j=0
          if i>=n and j>=n:
             i=i-2
             j=j-1
   return magic_square
# Print the magic square in a neat format where the numbers
# are right justified
def print_square (magic_square):
   l= len(magic_square)
   print("Here is a "+str(l)+" X "+ str(l)+" magic square:")
   print()
   for x in magic_square:
      for y in x:
         print("{:>3}".format(y),end= " ")
      print()

# Check that the 2-D list generated is indeed a magic square
def check_square ( magic_square ):
   
#get the first value to test against
   length=len(magic_square)
   sums=length*(length**2+1)/2
   row=0
   col=0
   magic=True
#test value to row and column
   for a in range (length):
      for b in range (length):
         row+=magic_square[a][b]
         col+=magic_square[b][a]
      if row==sums and col==sums:
         row=0
         col=0
      else:
         magic=False
   if magic==True:
      row=int(sums)
      col=int(sums)
      
# test value for diagonals
   lr_diagonals=0
   rl_diagonals=0
   i=0
   j=0
   k=length-1
   l=0
   for c in range (length):
      lr_diagonals+=magic_square[i][j]
      i+=1
      j+=1
   for c in range (length):
      rl_diagonals+=magic_square[k][l]
      k-=1
      l+=1
   if lr_diagonals!=sums or rl_diagonals!=sums:
      magic=False
# print every sum
   print()
   print("Sum of row =",row)
   print("Sum of column =",col)
   print("Sum diagonal (UL to LR) =",lr_diagonals)
   print("Sum diagonal (UR to LL) =",rl_diagonals)
   
def main():
  # Prompt the user to enter an odd number 3 or greater
 n= int(input("Please enter an odd number: "))
  # Check the user input
 while n%2==0 or n<3:
    n= int(input("Please enter an odd number: ")) 
  # Create the magic square
 print()
 make_square(n)
  # Print the magic square
 print_square(make_square(n))
  # Verify that it is a magic square
 check_square(make_square(n))

main()
