# Given the head of a linked list, return the node where the cycle begins.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail’s next pointer is connected to (0-indexed). It is -1 if there is no cycle.
# Do not modify the linked list.
# Complete the function in the given Python file.

class Node:
  def __init__(self, value = None, next = None):
    self.value = value
    self.next = next

  def next_node(self):
    return self.next

  def get_value(self):
    return self.value

def linked_list_cycle(head_node):
  slow_pointer = head_node
  fast_pointer = head_node
  met = False

  while fast_pointer != None and fast_pointer.next_node() != None:
    slow_pointer = slow_pointer.next_node()
    fast_pointer = fast_pointer.next_node().next_node()
    if slow_pointer == fast_pointer:
      met = True
      break
  
  if met == False:
    temp_node = Node(-1)
    return temp_node
  else:
    slow_pointer = head_node
    while slow_pointer != fast_pointer:
      slow_pointer = slow_pointer.next_node()
      fast_pointer = fast_pointer.next_node()
    return slow_pointer


node_5 = Node(5, None)
node_4 = Node(4, node_5)
node_3 = Node(3, node_4)
node_2 = Node(2, node_3)
node_1 = Node(1, node_2)

print(linked_list_cycle(node_1)) # print for no cycle

node_5.next = node_3
print(linked_list_cycle(node_1).get_value()) # print for cycle starting at node_3