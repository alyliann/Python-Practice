# Write a program in the file to the left that defines a linked list node that holds a name. Your program should do the following:
# Define a Node class
# Define a constructor that accepts a name and next parameters in that order.
# Create a linked list of one node that holds the name "Maria".
# Print the name of the node.

class Node:
  def __init__(self, node_name, next_node = None):
    self.name = node_name
    self.next = next_node

node = Node("Maria")
print(node.name)