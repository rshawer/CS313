# File: TestSparseMatrix.py

# Description: Sparse matrix representation has a 1-D list where each
#              element in that list is a linked list having the column
#              number and non-zero data in each link

#  Student Name: Changjie Lan

#  Student UT EID: cl38442

#  Partner Name: Andy Tien

#  Partner UT EID: at36437

#  Course Name: CS 313E

#  Unique Number: 51340

#  Date Created: 4/7/18

#  Date Last Modified: 4/8/18

class Link (object):
  def __init__ (self, col = 0, data = 0, next = None):
    self.col = col
    self.data = data
    self.next = next

  # return a String representation of a Link (col, data)
  def __str__ (self):
    s = ''
    s += "("+str(self.col) +","+ str(self.data) +")"
    return s

class LinkedList (object):
  # create linked lists
  def __init__ (self):
    self.first = None

  def insert_last (self, col, data):
    new_link = Link (col, data)
    current = self.first

    if (current == None):
      self.first = new_link
      return

    while (current.next != None):
      current = current.next

    current.next = new_link
  # insert a link into the linked list
  def insert_link(self, col, data):
    new_link = Link(col, data)
    current = self.first
    if current == None:
      self.first =new_link
      return
    while current.next!=None:
      if current.next.col>col:
        break
      current = current.next
    if current.next == None:
      current.next = new_link
    else:
      temp = current.next
      current.next = new_link
      new_link.next = temp
  def delete_link(self,col):
    current = self.first
    previous = self.first
    if current == None:
      return None
    while(current.col!=col):
      if(current.next==None):
        return None
      else:
        previous = current
        current = current.next
    if (current == self.first):
      self.first = self.first.next
    else:
      previous.next = current.next

    return current
  
  # return a String representation of a LinkedList
  def __str__ (self):
    if self.first!=None:
      
      current=self.first
      s = str(current)
      while current.next!=None:
        s+=","+str(current.next)
        current=current.next
    else:
      return None
    
    return s

class Matrix (object):
  def __init__ (self, row = 0, col = 0):
    self.row = row
    self.col = col
    self.matrix = []

  # perform assignment operation: matrix[row][col] = data
  def set_element (self, row, col, data):
    if data==0:
      self.matrix[row].delete_link(col)
      return
    if (row>len(self.matrix)-1):
      return None
    link=self.matrix[row].first
    bol=False
    while link!=None:
      if link.col== col:
        break
      link = link.next
    if link == None:
      self.matrix[row].insert_link(col, data)
    elif link.col == col:
      link.data = data
  # convert a list into a sparse matrix
  def convert(self, lists):
    
    row = len(lists)
    col = len(lists[0])
    mat = Matrix (row, col)

    for i in range (row):
      line=lists[i]
      new_row = LinkedList()
      for j in range (col):
        elt = int (line[j])
        if (elt != 0):
          new_row.insert_last(j, elt)
      mat.matrix.append (new_row)
    return mat

  # add two sparse matrices
  def __add__ (self, other):
    if ((self.row != other.row) or (self.col != other.col)):
      return None

    lists = []
    for i in range (self.row):
      temp=self.get_row(i)
      new_row = []
      for j in range (self.col):
        temp_row2=other.get_row(i)
        new_row.append (temp[j] + temp_row2[j])
      lists.append (new_row)
    matrix=self.convert(lists)
    return matrix
  
  # multiply two sparse matrices
  def __mul__ (self, other):
    if (self.col != other.row):
      return None
    lists = []
    for i in range (self.row):
      temp_row = self.get_row(i)
      #print(temp_row)
      new_row = []
      for j in range (other.col):
        temp_col = other.get_col(j)
        sum_mult = 0
        #print(temp_col)
        for k in range (other.row):
          sum_mult += temp_row[k] * temp_col[k]
        new_row.append(sum_mult)
      lists.append(new_row)
    matrix=self.convert(lists)
    return matrix

  # return a list representing a row with the zero elements inserted
  def get_row (self, n):
    if n>self.row-1:
      return None
    first_row=self.matrix[n].first
    returned=[]
    for i in range (self.col):
      returned.append(0)
    while first_row!=None:
      returned[first_row.col]=first_row.data
      first_row=first_row.next
    return returned
    
  # return a list representing a column with the zero elements inserted
  def get_col (self, n):
    if n>self.col-1:
      return None
    column=[]
    for row in range(self.row):
      current=self.matrix[row].first
      if current==None:
        return None
      while(current.col!=n):
        current=current.next
        if current ==None:
          break
      if current==None:
        column.append(0)
      else:
        column.append(current.data)


    return column
    

  # return a String representation of a matrix
  def __str__ (self):
    lst=[]
    for i in range(self.row):
      a=self.get_row(i)
      lst.append(a)
    s=""
    for x in lst:
      for y in x:
        s+=str(y).rjust(4)+" "
      s+="\n"
    return s 
#read the matrix and populate an empty matrix
def read_matrix (in_file):
  line = in_file.readline().rstrip("\n").split()
  row = int (line[0])
  col = int (line[1])
  mat = Matrix (row, col)

  for i in range (row):
    line = in_file.readline().rstrip("\n").split()
    new_row = LinkedList()
    for j in range (col):
      elt = int (line[j])
      if (elt != 0):
        new_row.insert_last(j, elt)
    mat.matrix.append (new_row)
  line = in_file.readline()

  return mat

def main():
  in_file = open ("./matrix.txt", "r")

  print ("Test Matrix Addition")
  matA = read_matrix (in_file)
  print (matA)
  matB = read_matrix (in_file)
  print (matB)

  matC = matA + matB
  print (matC)

  print ("\nTest Matrix Multiplication")
  matP = read_matrix (in_file)
  print (matP)
  matQ = read_matrix (in_file)
  print (matQ)

  matR = matP * matQ
  print (matR)

  print ("\nTest Setting a Zero Element to a Non-Zero Value")
  matA.set_element (1, 1, 5)
  print (matA)

  print ("\nTest Setting a Non-Zero Elements to a Zero Value")
  matB.set_element (1, 1, 0)
  print (matB)

  print ("\nTest Getting a Row")
  row = matP.get_row(1)
  print (row)

  print ("\nTest Getting a Column")
  col = matQ.get_col(0)
  print (col)
  
  in_file.close()

main()
