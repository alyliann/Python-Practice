# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
# Example:
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# Complete the function in the given Python file.

class Node:
  def __init__(self, value = None, next = None):
    self.value = value
    self.next = next

  def get_next(self):
    return self.next

  def set_next(self, nxt):
    self.next = nxt

  def get_value(self):
    return self.value

  def set_value(self, val):
    self.value = val

class LinkedList:
  def __init__(self, head_node = None):
    self.head = head_node

  def print_list(self):
    temp = self.head
    while(temp!=None):
      print(temp.get_value(), end=' ')
      temp = temp.get_next()
    print()

  def reverse(self, head, left, right):
    if left == right:
      return head

    left_node = head
    right_node = head

    for i in range(1, left):
      left_node = left_node.get_next()

    for i in range(1, right):
      right_node = right_node.get_next()

    while right_node.get_next() != left_node and right_node != left_node:
      old_right_val = right_node.get_value()
      right_node.set_value(left_node.get_value())
      left_node.set_value(old_right_val)

      left_node = left_node.get_next()
      right_node = head
      right -= 1
      for i in range(1, right):
        right_node = right_node.get_next()

    return head

if __name__=='__main__':
  node_5 = Node(5, None)
  node_4 = Node(4, node_5)
  node_3 = Node(3, node_4)
  node_2 = Node(2, node_3)
  node_1 = Node(1, node_2)

  llist = LinkedList(node_1)
  llist.print_list()
  
  llist.head = llist.reverse(llist.head, 2, 4)
  llist.print_list()
