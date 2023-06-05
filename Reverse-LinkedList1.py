# Given the head of a singly linked list, reverse the list in-place, and return the reversed list.
# Complete the function in the given python file

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

  def reverse(self, head):
    new_next_node = None
    current_node = head
    old_next_node = head.get_next()

    while current_node != None:
      current_node.set_next(new_next_node)
      new_next_node = current_node
      current_node = old_next_node
      if (old_next_node != None):
        old_next_node = old_next_node.get_next()
    
    return new_next_node

if __name__=='__main__':
  node_5 = Node(5, None)
  node_4 = Node(4, node_5)
  node_3 = Node(3, node_4)
  node_2 = Node(2, node_3)
  node_1 = Node(1, node_2)

  llist = LinkedList(node_1)
  
  llist.head = llist.reverse(llist.head)
  llist.print_list()

