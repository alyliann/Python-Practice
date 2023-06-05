# Complete the code in the file to the left by:
# Writing getter methods for the Node class
# Write the print_list method in the LinkedList class using the Node getter methods which prints each value in the LinkedList on a new line, starting at the head


class Node:
  def __init__(self, value = None, next = None):
    self.value = value
    self.next = next

  def next_node(self):
    return self.next

  def get_value(self):
    return self.value
  

class LinkedList:
  def __init__(self, head_node = None):
    self.head = head_node

  def print_list(self):
    current_node = self.head
    while current_node != None:
      print(current_node.get_value())
      current_node = current_node.next_node()


if __name__=='__main__':
  node_150 = Node(150, None)
  node_10 = Node(10, node_150)
  node_204 = Node(204, node_10)
  node_109 = Node(109, node_204)
  node_90 = Node(90, node_109)

  llist = LinkedList(node_90)

  llist.print_list()