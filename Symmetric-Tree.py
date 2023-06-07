# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
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

def symmetric_tree(root):
    queue1 = Queue()
    queue2 = Queue()

    queue1.enqueue(root)
    queue2.enqueue(root)

    while queue1.isEmpty() != True and queue2.isEmpty() != True:
        node1 = queue1.dequeue()
        node2 = queue2.dequeue()

        if node1.value != node2.value:
          return False
        # if node1's structure does not match node2
        elif (node1.left_child == None and node2.right_child != None) or (node1.right_child == None and node2.left_child != None):
          return False
        # if node2 has no child where node1 does:
        elif (node2.left_child == None and node1.right_child != None) or (node2.right_child == None and node1.left_child != None):
          return False
    
        if node1.left_child != None:
          queue1.enqueue(node1.left_child)
        if node1.right_child != None:
          queue1.enqueue(node1.right_child)
        if node2.right_child != None:
          queue2.enqueue(node2.right_child)
        if node2.left_child != None:
          queue2.enqueue(node2.left_child)

    if queue1.isEmpty() != True or queue2.isEmpty() != True: # if one of the queues is not empty
        return False
    else:
        return True
        

root = Node(4)
root.left_child = Node(2)
root.right_child = Node(2)
root.left_child.left_child = Node(1)
root.right_child.right_child = Node(1)

print(symmetric_tree(root)) # expected output: True