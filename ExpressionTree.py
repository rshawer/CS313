#  File: ExpressionTree.py

#  Description: Expression Tree, puts an infix into a tree and create postfix and prefix

#  Student's Name: Changjie Lan

#  Student's UT EID: cl38442

#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E 

#  Unique Number: 51340

#  Date Created: 4/12/18

#  Date Last Modified: 4/12/18

class Stack (object):
    def __init__ (self):
        self.stack = []

    # add an item to the top of the stack
    def push (self, item):
        self.stack.append (item)

    # remove an item from the top of the stack
    def pop (self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek (self):
        return self.stack[len(self.stack)-1]

    # check if the stack is empty
    def is_empty (self):
        return (len(self.stack) == 0)

    # return the number of elements in the stack
    def size (self):
        return (len(self.stack))
    
 

class Node (object):
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None
    

class Tree (object):
  def __init__ (self):
      self.root= None

      
  #create the tree 
  def createTree (self, expr):
      the_Stack=Stack()

      operations = ["+", "-", "*", "/"]

      tokens = expr.split()

      new_node = Node(None)
      self.root = new_node

      current = self.root

      for item in tokens:
          if item=="(":
              current.lchild = Node(None)
              the_Stack.push(current)
              current = current.lchild

          elif item in operations:
              current.data = item
              the_Stack.push(current)
              current.rchild = Node(None)
              current = current.rchild
          elif item==")":
              if (not the_Stack.is_empty()):
                  current=the_Stack.pop()
          else:
              current.data=item
              current = the_Stack.pop()

  #recursion to check till you get to the very end of the tree, then operate on the tree   
  def evaluate (self, aNode):
      if (aNode.lchild==None) and (aNode.rchild==None):
          return aNode.data
      else:
          left = self.evaluate(aNode.lchild)
          right = self.evaluate(aNode.rchild)
          result = self.operate(left, right, aNode.data)
          return result
  #convert in-order expression to pre
  def preOrder (self, aNode):
    if (aNode != None):
      print (aNode.data, end = " ")
      self.preOrder (aNode.lchild)
      self.preOrder (aNode.rchild)
  # convert in-order expression to postorder    
  def postOrder (self, aNode):
    if (aNode != None):
      self.postOrder (aNode.lchild)
      self.postOrder (aNode.rchild)
      print (aNode.data, end = " ")
      
  def operate (self, oper1, oper2, token):
      if (token == "+"):
        return float(oper1) + float(oper2)
      elif (token == "-"):
        return float(oper1) - float(oper2)
      elif (token == "*"):
        return float(oper1) * float(oper2)
      elif (token == "/"):
        return float(oper1 / oper2)

def main():
    # read the file
    in_file = open("./expression.txt","r")
    expr = in_file.readline()
    expr = expr.strip()
    print()
    # create expression tree
    new_tree = Tree()
    new_tree.createTree(expr)
    result=new_tree.evaluate(new_tree.root)
    # print the output
    print(expr,"=",result)
    print()
    print("Prefix Expression: ", end="")
    new_tree.preOrder(new_tree.root)
    print()
    print()
    print("Postfix Expression: ", end="")
    new_tree.postOrder(new_tree.root)
    print()
    print()
    in_file.close()
    

main()
