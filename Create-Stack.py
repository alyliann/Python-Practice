# Fill in the following class DIYStack to create a fully functional stack.
# For the .pop() and .peek() methods, ensure that your code will return a None value if the stack is empty.
# For the .allNodesString() method, ensure that you print a visual representation of the stack (i.e. a newline between each element such that the next element to be popped is on “top”).
# For this implementation, you will need to store each element in a Node so that users can push either fully formed Nodes or other data types onto the stack.

# You are given the below Node class to assist in your implementation.
class Node:
  def __init__(self, val):
    self.value = val
    self.next = None
    self.prev = None

class DIYStack:
  
  top_node = None
  
  def __init__(self):
    top_node = None
    
  def push(self, value):
    new_node = Node(value)
    if isinstance(value, Node) == True:
      new_node = value
    
    if self.top_node == None:
      self.top_node = new_node
    else:
      new_node.prev = self.top_node
      self.top_node.next = new_node
      self.top_node = new_node

      
  def pop(self):
    if self.top_node == None:
      return None
    else: # Remove & return the next element on the stack
      return_node = self.top_node
      self.top_node = self.top_node.prev
      return return_node.value

  
  def peek(self):
    if self.top_node == None:
      return None
    else: # Return the value of the next element to be popped
      return self.top_node.value


  def allNodesString(self):
    curr_node = self.top_node
    while (curr_node != None):
      print(curr_node.value)
      curr_node = curr_node.prev
  

# Instantiate + test your code here
my_stack = DIYStack()
print(my_stack)

my_stack.push(1)
my_stack.push(2)
my_stack.allNodesString()

new_node = Node(3)
my_stack.push(new_node)
print(my_stack.peek())

my_stack.pop()
my_stack.allNodesString()