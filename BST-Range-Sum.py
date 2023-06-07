# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].
# Complete the function in the given Python file.

class Node:
  def __init__(self, val):
    self.value = val
    self.left_child = None
    self.right_child = None

def range_sum(node, low, high):
  if node == None:
    return 0
  elif node.value >= low and node.value <= high:
    return (range_sum(node.left_child, low, high) + node.value + range_sum(node.right_child, low, high))
  else:
    return (range_sum(node.left_child, low, high) + 0 + range_sum(node.right_child, low, high))
    

root = Node(4)
root.left_child = Node(2)
root.right_child = Node(6)
root.left_child.left_child = Node(1)
root.left_child.right_child = Node(3)
root.right_child.left_child = Node(5)
root.right_child.right_child = Node(7)

print(range_sum(root, 3, 5))