# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
# Complete the function in the given Python file.

class Queue:
  def __init__(self):
      self.items = []

  def isEmpty(self):
      return self.items == []

  def enqueue(self, item):
      self.items.append(item)

  def dequeue(self):
      return self.items.pop(0)

class Node:
  def __init__(self, val):
    self.value = val
    self.left_child = None
    self.right_child = None

def same_tree(root1, root2):
  queue1 = Queue()
  queue2 = Queue()

  queue1.enqueue(root1)
  queue2.enqueue(root2)

  while queue1.isEmpty() != True and queue2.isEmpty() != True:
    node1 = queue1.dequeue()
    node2 = queue2.dequeue()

    if node1.value != node2.value:
      return False
    # if node1 has no child where node2 does:
    elif (node1.left_child == None and node2.left_child != None) or (node1.right_child == None and node2.right_child != None):
      return False
    # if node2 has no child where node1 does:
    elif (node2.left_child == None and node1.left_child != None) or (node2.right_child == None and node1.right_child != None):
      return False
    
    if node1.left_child != None:
      queue1.enqueue(node1.left_child)
    if node1.right_child != None:
      queue1.enqueue(node1.right_child)
    if node2.left_child != None:
      queue2.enqueue(node2.left_child)
    if node2.right_child != None:
      queue2.enqueue(node2.right_child)

  if queue1.isEmpty() != True or queue2.isEmpty() != True: # if one of the queues is not empty
    return False
  else:
    return True


root1 = Node(4)
root1.left_child = Node(2)
root1.right_child = Node(6)
root1.left_child.left_child = Node(1)
root1.left_child.right_child = Node(3)

root2 = Node(4)
root2.left_child = Node(2)
root2.right_child = Node(6)
root2.left_child.left_child = Node(1)
root2.left_child.right_child = Node(3)

print(same_tree(root1, root2))