#  File: Grid.py

#  Description: Finds the greatest product of 4 numbers

#  Student Name: Changjie Lan

#  Student UT EID: cl38442

#  Partner Name: none

#  Partner UT EID: none

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created: 11/1/17

#  Date Last Modified: 11/3/17

# function to print the result
def printresult(highest_product):
    print("The greatest product is",str(highest_product)+".")

def main():
    #open file for coding
    in_file=open("./grid.txt","r")
    #read the dimension of the grid
    dim= in_file.readline()
    dim = dim.strip()
    dim= int(dim)
    #create an empty grid
    grid=[]

    #populate the grid
    for i in range(dim):
        line = in_file.readline()
        line = line.strip()
        row = line.split()
        for j in range(dim):
            row[j] = int(row[j])
        grid.append(row)

    #find the highest product through rows and columns
    highest_product=0
    row_product=0
    for y in range (dim):
        for x in range (dim-3):
            row_product= grid[y][x]*grid[y][x+1]*grid[y][x+2]*grid[y][x+3]
            if row_product>highest_product:
                highest_product=row_product
            column_product = grid[x][y]*grid[x+1][y]*grid[x+2][y]*grid[x+3][y]
            if column_product>highest_product:
                highest_product=column_product


    #find the highest product through diagonals, left
    for i in range(dim-3):
        for j in range(dim-3):
            left_diagonal= grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3]
            if(left_diagonal>highest_product):
                highest_product=left_diagonal
    #find the highest product through diagonals, right
    for a in range (dim-3):
        for b in range( dim-1, 2,-1):
            right_diagonal= grid[a][b]*grid[a+1][b-1]*grid[a+2][b-2]*grid[a+3][b-3]
            if(right_diagonal>highest_product):
                highest_product=right_diagonal

    #print the highest product
    printresult(highest_product)
    
    #close the file
    in_file.close
main()
    
