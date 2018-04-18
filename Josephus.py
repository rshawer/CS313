#  File: Josephus.py

#  Description: Circular linked list representation of Josephus problem

#  Student Name: Changjie Lan

#  Student UT EID: cl38442

#  Partner Name: Andy Tien

#  Partner UT EID: at36437

#  Course Name: CS 313E

#  Unique Number: 51340

#  Date Created: 4/2/18

#  Date Last Modified: 4/2/18


class Link (object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next

class CircularList(object):
  # Constructor
  def __init__ ( self ):
      self.first= None

  # Insert an element (value) in the list
  def insert ( self, item ):
      if (self.first ==None):
        self.first=Link(item)
        self.first.next=self.first
      else:
        newLink = Link(item)
        current = self.first
        while(current.next!=self.first):
          current=current.next
        current.next=newLink
        newLink.next=self.first
  # Find the link with the given key (value)
  def find ( self, key ):
      current=self.first
      if self.first ==None:
          return None
      while current.data!=key:
          current=current.next
          if current==self.first:
              return None
      return current

  # Delete a link with a given key (value)
  def delete ( self, key ):
      previous = self.first
      current=self.first
      last= self.first
      while last.next!=self.first:
          last=last.next
      if current==None:
          return None
      while current.data!=key:
          if current.next==self.first:
              return None
          else:
              previous = current
              current=current.next
      if current == last:
          previous.next = current
          previous.next = self.first
          return
      if current == self.first:
          if current.next==self.first:
              self.first=None
              return 
          self.first = self.first.next
          last.next = self.first
      else:
          previous.next=current.next
      
          

  # Delete the nth link starting from the Link start 
  # Return the next link from the deleted Link
  def delete_after ( self, start, n ):
      current=self.find(start)
  # goes through iterations of the linked lists that would be deleted

      for i in range (1,n):
          current = current.next
      copy=current
      self.delete(current.data)

      
      return copy, current.next

  # Return a string representation of a Circular List
  def __str__ ( self ):
      strings=""
      current = self.first

      while (current.next!=self.first):
          strings+=str(current.data)+" "
          current=current.next
      strings+=str(current.data)+" "
      return strings

def main():
    in_file = open("./josephus.txt", "r")

    num_soldiers= int(in_file.readline())

    count_start = int(in_file.readline())

    n= int(in_file.readline())

    in_file.close()

    soldiers_first = CircularList()
    # creates soldiers list
    for i in range (1,num_soldiers+1):
        soldiers_first.insert(i)
    #goes through the soldiers and delete
    for i in range (1, num_soldiers+1):
        deleted, count_start = soldiers_first.delete_after(count_start, n)
        count_start = count_start.data
        deleted = deleted.data
        print(deleted)


main()
