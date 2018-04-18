#  File: Spiral.py

#  Description: A number spiral and a way to see parts of a spiral 

#  Student Name: Changjie Lan

#  Student UT EID: cl38442

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created: 11/20/17

#  Date Last Modified: 11/20/17
def printer1():

    return "Number on Outer Edge"

def printer2():
    
    return "Number not in range"

def main():
# prompts the user to put in a correct number
    dim= int(input("Enter dimension: "))
    num= int(input("Enter number in spiral: "))
    if dim%2==0:
        dim=dim+1

# start the loops that fills the 2d lists with 0
    if num<=dim**2 and num>=1:
        depth=dim//2+1
        outer=[]
        inner=[]

        for x in range(dim):
            inner=[]
            for i in range(dim):
                inner.append(0)

            outer.append(inner)

        dimclone=dim
        original=0
        fake=0
#goes through each loop and star adding in the numbers

        for i in range(depth):
            for j in range(dimclone-1, original-1, -1):
                if  outer[i][j]==0 and j== dimclone-1 and i==0:
                    outer[i][j]=(dim**2)
                elif outer[i][j]==0:
                    outer[i][j]=outer[i][j+1]-1
            for l in range (original,dimclone):
                if outer[l][i]==0:
                    outer[l][i]=outer[l-1][i]-1

            for a in range(original,dimclone):
                if outer[dimclone-1][a]==0:
                    outer[dimclone-1][a]=outer[dimclone-1][a-1]-1

            for b in range(dimclone-1, original-1, -1):
                if outer[b][dimclone-1]==0:
                    outer[b][dimclone-1]=outer[b+1][dimclone-1]-1

            original=original+1
            dimclone=dimclone-1


        column=0
        row=0
#find the number in the spiral, locates the index
        for e in outer:
            if num in e:
                column=e.index(num)
                break
            row=row+1

        if row==dim-1 or column==dim-1 or column==0 or row==0:
            print()
            print(printer1())
        else:
#prints the three results
            print()
            print(str(outer[row-1][column-1])+" "+str(outer[row-1][column])+" "+str(outer[row-1][column+1]))
            print(str(outer[row][column-1])+" "+str(outer[row][column])+" "+str(outer[row][column+1]))
            print(str(outer[row+1][column-1])+" "+str(outer[row+1][column])+" "+str(outer[row+1][column+1]))
    else:

         print()
         print(printer2())
                    
            
                    
                
   
        
    





main()
