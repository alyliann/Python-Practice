# Given the root of a binary tree, return the sum of values of its deepest leaves.
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

def deepest_leaves_sum(root, depth = 0):
  deepest_sum = 0
  queue = Queue()
  queue.enqueue(root)
  queue_size = 0
  condition = False

  while not queue.isEmpty():
    queue_size = len(queue.items)
    deepest_sum = 0
    for i in range(queue_size):
      current_node = queue.dequeue()
      deepest_sum += current_node.value
      if current_node.left_child:
        queue.enqueue(current_node.left_child)
      if current_node.right_child:
        queue.enqueue(current_node.right_child)
        
  return deepest_sum


root = Node(4)
root.left_child = Node(1)
root.right_child = Node(3)
root.left_child.left_child = Node(1)
root.left_child.right_child = Node(1)

print(deepest_leaves_sum(root))