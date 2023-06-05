# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node. 
# Complete the function in the given Python file.

class Node:
  def __init__(self, value = None, next = None):
    self.value = value
    self.next = next

  def next_node(self):
    return self.next

  def get_value(self):
    return self.value

def middle_of_linkedlist(head_node):
  size = 0
  current_node = head_node

  while current_node != None:
    current_node = current_node.next_node()
    size += 1

  middle = size//2
  count = 0
  current_node = head_node

  while count != middle:
    current_node = current_node.next_node()
    count += 1

  return current_node

node_6 = Node(6, None)
node_5 = Node(5, node_6)
node_4 = Node(4, node_5)
node_3 = Node(3, node_4)
node_2 = Node(2, node_3)
node_1 = Node(1, node_2)

print(middle_of_linkedlist(node_1).get_value())