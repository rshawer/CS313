#  File: Boxes.py

#  Description: Nesting boxes with recursion

#  Student Name: Changjie Lan

#  Student UT EID: cl38442

#  Partner Name: 

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51340

#  Date Created: 2/23/18

#  Date Last Modified: 2/23/18

def does_fit (box1, box2):
  return (box1[0] < box2[0]) and (box1[1] < box2[1]) and (box1[2] < box2[2])
global answerlist
answerlist=[]
# This function computes all subsets of a list
def subsets (a, b, lo):
  truth=0
  hi = len(a)
  if (lo == hi):
      for i in range (len(b)-1):
          if does_fit(b[i], b[i+1]):
              truth+=1
      if truth==len(b)-1:
          answerlist.append(b)
  else:
    c = b[:]
    b.append (a[lo])
    subsets (a, c, lo + 1)
    subsets (a, b, lo + 1)
def main():
  # open file for reading
  in_file = open ('boxes.txt', 'r')

  # read the number of boxes
  line = in_file.readline()
  line = line.strip()
  num_boxes = int(line)

  # create empty list of boxes
  box_list = []

  # read the list of boxes from file
  for i in range (num_boxes):
    line = in_file.readline()
    line = line.strip()
    box = line.split()
    for i in range (len(box)):
      box[i] = int (box[i])
    box.sort()
    box_list.append (box)

  # close the file
  in_file.close()
  # sort the box list
  box_list.sort()
  # create a list that will hold the nested boxes
  b=[]
  # get all subsets of boxes
  subsets(box_list,b,0)
  # sort all the longest subsets only
  maxlength=0
  newlist=[]
  for i in answerlist:
      if len(i)>maxlength:
         maxlength=len(i)
  # if no subset has anything bigger than 1; no nesting boxes
  if maxlength==1:
      print("No Nesting Boxes")
  else:
      for i in answerlist:
          if len(i)==maxlength:
             newlist.append(i)
      newlist.sort()
      print("Largest Subset of Nesting Boxes")
  #print from 2d list
      for i in range (len(newlist)):
          print()
          for j in range (len(newlist[i])):
              print(newlist[i][j])
  
main()
