#  File: Triangle.py

#  Description: greatest sum path for a triangle

#  Student's Name: Changjie Lan

#  Student's UT EID: cl38442

#  Partner's Name: 

#  Partner's UT EID:

#  Course Name: CS 313E 

#  Unique Number: 51340

#  Date Created: 3/6/18

#  Date Last Modified: 3/7/18


import time

# returns the greatest path sum using exhaustive search
maximum=0

def exhaustive_search(grid):
    exhaustive_helper(grid,0,0,0,0)
    return maximum
def exhaustive_helper(grid, lo, row, col, ex_sums):
    global maximum
    hi = len(grid)
    if (lo == hi):
      if ex_sums>maximum:
        maximum=ex_sums
    else:
      ex_sums += grid[row][col]
      exhaustive_helper(grid, lo+1, row+1, col+1, ex_sums)
      exhaustive_helper(grid, lo+1, row+1, col, ex_sums)

# returns the greatest path sum using greedy approach
def greedy (grid):

    idx = 0 
    greedysum=0
    for i in range(len(grid)):
        if i ==0:
            greedysum+= grid[i][0]
        else:
            if grid[i][idx]>grid[i][idx+1]:
                greedysum+=grid[i][idx]
            else:
                greedysum+=grid[i][idx+1]
                idx+=1
    return greedysum
# returns the greatest path sum using divide and conquer (recursive) approach
def rec_search (grid):
    return recursive_helper(grid,0,0)
def recursive_helper (grid, i, k):
    #base case
    if i==len(grid)-1:
        return grid[i][k]
    else:
        return grid[i][k]+max(recursive_helper(grid,i+1,k),recursive_helper(grid,i+1,k+1))

# returns the greatest path sum and the new grid using dynamic programming

def dynamic_prog (grid):
    row = len(grid)-1
    for i in range(len(grid)-1):
        for k in range(len(grid[row])-1):
            add_target= grid[row-1][k]
            sum_one=add_target+grid[row][k]
            sum_two=add_target+grid[row][k+1]
            if sum_one>sum_two:
                grid[row-1][k]=sum_one
            else:
                grid[row-1][k]=sum_two
        row-=1
    tupl_dy=(grid[0][0],grid)
    return tupl_dy

# reads the file and returns a 2-D list that represents the triangle
def read_file():
    in_file= open ('./triangle.txt','r')
    line = in_file.readline()
    line = line.strip()
    num_row =int(line)
    triangle=[]
    for i in range (num_row):
        line = in_file.readline()
        line = line.strip()
        row = line.split()
        for i in range (len(row)):
          row[i] = int(row[i])
        triangle.append(row)
    return triangle
                 
def main ():
    # read triangular grid from file
    triangle=read_file()
    ti = time.time()
    # output greates path from exhaustive search
    exhaustive_search(triangle)
    tf = time.time()
    del_t = tf - ti
    # print time taken using exhaustive search
    print("The greatest path sum through exhaustive search is "+str(exhaustive_search(triangle))+".")
    print("The time taken for exhuastive search is "+str(del_t)+" seconds.")
    print()
    ti = time.time()
    # output greates path from greedy approach
    greedy(triangle)
    tf = time.time()
    del_t = tf - ti
    # print time taken using greedy approach
    print("The greatest path sum through greedy approach is "+str(greedy(triangle))+".")
    print("The time taken for greedy approach is "+str(del_t)+" seconds.")
    print()
    ti = time.time()
    # output greates path from divide-and-conquer approach
    rec_search(triangle)
    tf = time.time()
    del_t = tf - ti
    # print time taken using divide-and-conquer approach
    print("The greatest path sum through recursive search is "+str(rec_search(triangle))+".")
    print("The time taken for recursive search is "+str(del_t)+" seconds.")
    print()
    ti = time.time()
    # output greates path from dynamic programming
    tuplemain=dynamic_prog(triangle)
    tf = time.time()
    del_t = tf - ti
    # print time taken using dynamic programming
    print("The greatest path sum through dynamic programming is "+str(tuplemain[0])+".")
    print("The time taken for dynamic programming is "+str(del_t)+" seconds.")
if __name__ == "__main__":

 main()
