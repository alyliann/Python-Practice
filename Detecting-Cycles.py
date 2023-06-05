# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
# Return true if there is a cycle in the linked list. Otherwise, return false.
# Complete the function in the given Python file.

class Node:
  def __init__(self, value = None, next = None):
    self.value = value
    self.next = next

  def next_node(self):
    return self.next

  def get_value(self):
    return self.value

def detect_cycles(head_node):
  slow_pointer = head_node
  fast_pointer = head_node
  i = -1
  condition = False

  while condition == False:
    fast_pointer = fast_pointer.next_node()
    if i > 0 and i % 2 == 0:
      slow_pointer = slow_pointer.next_node()
    i += 1
    if fast_pointer == None or fast_pointer == slow_pointer:
      condition = True
  
  if fast_pointer == None:
    return False
  else:
    return True


node_150 = Node(150, None)
node_10 = Node(10, node_150)
node_204 = Node(204, node_10)
node_109 = Node(109, node_204)
node_90 = Node(90, node_109)
# node_150.next = node_10 #creates cycle, un-comment to test

print(detect_cycles(node_90))