#  File: TestBinaryTree.py

#  Description: Creates the binary tree and run various functions about its statistic

#  Student Name: Changjie Lan

#  Student UT EID: cl38422

#  Partner Name: Andy Tien

#  Partner UT EID: at36437

#  Course Name: CS 313E

#  Unique Number: 51340

#  Date Created: 4/12

#  Date Last Modified: 4/14


class Node (object):
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None

class Tree (object):

  def __init__(self):
      self.root= None
      
  def insert (self, val):
    new_node = Node (val)

    if (self.root == None):
      self.root = new_node
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (val < current.data):
          current = current.lchild
        else:
          current = current.rchild
      if (val < parent.data):
        parent.lchild = new_node
      else:
        parent.rchild = new_node
        
  # Returns true if two binary trees are similar
  def is_similar (self, pNode):
      return self.compare(self.root, pNode.root)

  def compare(self, aNode, pNode):
      if aNode == None and pNode==None:
          return True
      elif aNode != None and pNode !=None:
          return aNode.data==pNode.data and self.compare(aNode.rchild, pNode.rchild) and self.compare(aNode.lchild, pNode.lchild)   
      else:
          return False 
  # Prints out all nodes at the given level
  def print_level (self, level):
      if self.root==None:
          return
      else:
          levelstring=""
          return self.print_level_helper(self.root, level,1, levelstring)
  def print_level_helper(self, node, level, current, levelstring):
      if node==None:
          return " "
      elif current==level:
          return str(node.data)+ " "
      else:
          levelstring+= str(self.print_level_helper(node.lchild, level, current+1, levelstring)) + str(self.print_level_helper(node.rchild, level, current+1, levelstring))
          return levelstring
  # Returns the height of the tree
  def get_height (self):
      if self.root==None:
          return 0
      return self.get_height_helper(self.root)

  def get_height_helper(self, nodes):
      if nodes==None:
          return 0
      else:
          return 1+max(self.get_height_helper(nodes.lchild),self.get_height_helper(nodes.rchild))

  # Returns the number of nodes in the left subtree and
  # the number of nodes in the right subtree and the root
  def num_nodes (self):
    if self.root == None:
      return 0
    else:
      left = self.root.lchild
      right = self.root.rchild
      left_sum = self.subtree_num(left)
      right_sum = self.subtree_num(right)
      return left_sum + right_sum + 1

  def subtree_num (self, node):
    if node == None:
      return 0
    else:
      return 1 + self.subtree_num(node.lchild) + self.subtree_num(node.rchild)

def main():
# Create three trees - two are the same and the third is different
  treeone = Tree()
  treeone.insert(50)
  treeone.insert(30)
  treeone.insert(70)
  treeone.insert(10)
  treeone.insert(40)
  treeone.insert(60)
  treeone.insert(80)
  treeone.insert(7)
  treeone.insert(25)
  treeone.insert(38)
  treeone.insert(47)
  treeone.insert(58)
  treeone.insert(65)
  treeone.insert(77)
  treeone.insert(96)

  treetwo = Tree()
  treetwo.insert(50)
  treetwo.insert(30)
  treetwo.insert(70)
  treetwo.insert(10)
  treetwo.insert(40)
  treetwo.insert(60)
  treetwo.insert(80)
  treetwo.insert(7)
  treetwo.insert(25)
  treetwo.insert(38)
  treetwo.insert(47)
  treetwo.insert(58)
  treetwo.insert(65)
  treetwo.insert(77)
  treetwo.insert(96)

  treethree = Tree()
  treethree.insert(50)
  treethree.insert(31)
  treethree.insert(71)
  treethree.insert(11)
  treethree.insert(41)
  treethree.insert(61)
  treethree.insert(81)
  treethree.insert(8)
  treethree.insert(26)
  treethree.insert(37)
  treethree.insert(47)
  treethree.insert(59)
  treethree.insert(62)

  # Test your method is_similar()
  print("is_similar function")
  print("Test for similar trees")
  print(treeone.is_similar(treetwo))
  print("Test for different trees")
  print(treeone.is_similar(treethree))
  print()

  # Print the various levels of two of the trees that are different
  print("print_level function for two different trees")
  print("Test Tree One")
  print("level 1")
  print(treeone.print_level(1))   
  print("level 2")
  print(treeone.print_level(2))
  print("level 3")
  print(treeone.print_level(3))
  print("level 4")
  print(treeone.print_level(4))

  print()
  print("Test Tree Three")
  print("level 1")
  print(treethree.print_level(1))
  print("level 2")
  print(treethree.print_level(2))
  print("level 3")
  print(treethree.print_level(3))
  print("level 4")
  print(treethree.print_level(4))

  # Get the height of the two trees that are different
  print()
  print("Test get_height for two different trees")
  print("height for tree one")
  print(treeone.get_height())
  print("height for tree three")
  print(treethree.get_height())
  
  # Get the total number of nodes in a binary search tree
  print()
  print("Test num_nodes for two different sized trees")
  print("Number of nodes in tree one")
  print(treeone.num_nodes())
  print("Number of nodes in tree three")
  print(treethree.num_nodes())
main()

