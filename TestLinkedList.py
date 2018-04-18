#  File: TestLinkedList.py

#  Description: Test multiple manipulations of linked lists

#  Student Name: Changjie Lan

#  Student UT EID: cl38442

#  Partner Name: 

#  Partner UT EID: 

#  Course Name: CS 313E

#  Unique Number: 51340

#  Date Created: 3/30/18

#  Date Last Modified: 3/30/18

class Link (object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next

class LinkedList (object):
  def __init__ (self):
    self.first = None
# number of links in a linkedlist
  def get_num_links(self):
   
      current=self.first
      counter=0
      if current==None:
          return 0
      while current!=None:
          current=current.next
          counter+=1
      return counter
          

  # add an item at the beginning of the list
  def insert_first (self, item):
    new_link = Link (item)

    new_link.next = self.first
    self.first = new_link
    
  # add an item to the end of the list
  def insert_last (self, item):
    new_link = Link (item)

    current = self.first
    if (current == None):
      self.first = new_link
      return 

    while (current.next != None):
      current = current.next

    current.next = new_link
  # add an item in an order list in ascending order
  def insert_in_order(self, item):
    new_link=Link(item)
    current=self.first
    if self.first==None:
        self.first=new_link
        return 
    previous=self.first
    while current.data<item:
        previous=current
        current=current.next
        if current==None:
            self.insert_last(item)
            return
      
    if current== self.first:
      new_link.next = self.first
      self.first=new_link
      return 
    if current.data>=item:
        previous.next=new_link
        new_link.next=current
  #search in an unordered list, return None if not found
  def find_unordered (self, item):
      current=self.first
      if self.first==None:
          return None
      while(current.data!=item):
          current=current.next
          if current==None:
              return None
      return current
  # Search in an ordered list, return None if not found 
  def find_ordered (self, item):
      current=self.first
      if self.first==None:
          return None
      if current.data>item:
          return None
      while item>current.data:
          if current.next==None:
              return None
          else:
              current=current.next
      if current.data!=item:
          return None
      return current
    
  # delete a link containing the item
  def delete_link (self, item):
    previous = self.first
    current = self.first

    if (current == None):
      return None

    while (current.data != item):
      if (current.next == None):
        return None
      else:
        previous = current
        current = current.next

    if (current == self.first):
      self.first = self.first.next
    else:
      previous.next = current.next
    return current
  # String representation of data 10 items to a line, 2 spaces between data  
  def __str__(self):
      if self.first==None:
          return ''
      string=''
      counter=0
      current=self.first
      while(current!=None):
          if counter<10:
             string+= str(current.data)+"  "
             counter+=1
          elif counter==10:
             string+="\n"+str(current.data)+"  "
             counter=0
             counter+=1
          current=current.next
      return string
  # Copy the contents of a list and return new list
  def copy_list (self):
      current =self.first
      new_list=LinkedList()
      if self.first== None:
          return None
      while current!=None:
          new_list.insert_last(current.data)
          current=current.next
      return new_list
  # Reverse the contents of a list and return new list
  def reverse_list (self):
      current = self.first
      new_list=LinkedList()
      if self.first==None:
          return None
      while current!=None:
          new_list.insert_first(current.data)
          current=current.next
      return new_list
  # sort the list in ascending order
  def sort_list (self):
      d=[]
      current=self.first
      if self.first==None:
          return None
      sorted_list=LinkedList()
      while current!=None:
          d.append(current.data)
          current=current.next
      d.sort()
      for i in d:
          sorted_list.insert_in_order(i)
      return sorted_list
  # return true if the list is sorted in ascending order, return False otherwise, empty lists are sorted
  def is_sorted(self):
      current=self.first
      previous=self.first
      if self.first==None:
          return True
      while current!=None:
          if current.data<previous.data:
              return False 
          if previous.data<=current.data:
              previous=current
              current=current.next
      return True
  # return true if linked list is empty
  def is_empty(self):
      return self.first==None
  # Merge two sorted lists and return new list in ascending order
  def merge_list (self, other):
      current1=self.first
      current2=other.first
      mergedlist=LinkedList()
      if other.first==None:
          return self
      if self.first==None:
          return other
      while(current1!=None):
          mergedlist.insert_in_order(current1.data)
          current1=current1.next
      while(current2!=None):
          mergedlist.insert_in_order(current2.data)
          current2=current2.next
      return mergedlist
          

  # Test if two lists are equal, item by item and return True
  def is_equal (self, other):
      current1=self.first
      current2=other.first
      if self.get_num_links()!=other.get_num_links():
          return False
      elif self.is_empty() and other.is_empty():
          return True
      elif self.get_num_links()==other.get_num_links():
          while(current1!=None):
              if current1.data!=current2.data:
                  return False
              current1=current1.next
              current2=current2.next
          return True
      return True 

  # Return a new list, keeping only the first occurence of an element
  # and removing all duplicates. Do not change the order of the elements.
  def remove_duplicates (self):
      no_duplicates=LinkedList()
      current=self.first
      nodupl=set()
      while current!=None:
          if current.data not in nodupl:
              no_duplicates.insert_last(current.data)
              nodupl.add(current.data)
          current=current.next

      return no_duplicates

def main():
  # Test methods insert_first() and __str__() by adding more than
  # 10 items to a list and printing it.
  test_lst=LinkedList()
  test_lst.insert_first(3)
  test_lst.insert_first(4)
  test_lst.insert_first(4)
  test_lst.insert_first(4)
  test_lst.insert_first(4)
  test_lst.insert_first(4)
  test_lst.insert_first(4)
  test_lst.insert_first(11)
  test_lst.insert_first(12)
  test_lst.insert_first(9)
  print(test_lst)

  # Test method insert_last()
  test_lst2=LinkedList()
  test_lst2.insert_last(3)
  test_lst2.insert_last(4)
  test_lst2.insert_last(4)
  test_lst2.insert_last(4)
  test_lst2.insert_last(4)
  test_lst2.insert_last(4)
  test_lst2.insert_last(4)
  test_lst2.insert_last(9)
  test_lst2.insert_last(11)
  test_lst2.insert_last(12)
  print(test_lst2)
  # Test method insert_in_order()
  test_lst3=LinkedList()
  for i in range (1,10):
    test_lst3.insert_last(i)
  test_lst3.insert_in_order(5)
  print(test_lst3)
  # Test method get_num_links()
  print(test_lst3.get_num_links())
  # Test method find_unordered()
  # Consider two cases - item is there, item is not there 
  print(test_lst.find_unordered(11))
  print(test_lst.find_unordered(133))
  # Test method find_ordered()
  # Consider two cases - item is there, item is not there 
  print(test_lst3.find_ordered(3))
  print(test_lst3.find_ordered(11))  
  # Test method delete_link()
  # Consider two cases - item is there, item is not there 
  print(test_lst3.delete_link(5))
  print(test_lst3.delete_link(11))
  # Test method copy_list()
  copied=test_lst.copy_list()
  print(copied)
  # Test method reverse_list()
  reversedlist=test_lst.reverse_list()
  print(reversedlist)
  # Test method sort_list()
  sortedlist=test_lst.sort_list()
  print(sortedlist)
  # Test method is_sorted()
  # Consider two cases - list is sorted, list is not sorted
  emptylist=LinkedList()
  print(sortedlist.is_sorted())
  print(test_lst.is_sorted())
  # Test method is_empty()
  print(emptylist.is_empty())
  print(test_lst.is_empty())
  # Test method merge_list()
  merged=test_lst2.merge_list(test_lst)
  print(merged)
  # Test method is_equal()
  # Consider two cases - lists are equal, lists are not equal
  print(test_lst.is_equal(copied))
  print(test_lst.is_equal (reversedlist))
  # Test remove_duplicates()
  print(test_lst2.remove_duplicates())
  
if __name__ == "__main__":
  main()
    



