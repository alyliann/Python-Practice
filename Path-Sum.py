# Given the root of a binary tree and an integer target_sum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals target_sum.
# Complete the function in the given Python file.

class Node:
  def __init__(self, val):
    self.value = val
    self.left_child = None
    self.right_child = None

def path_sum(node, sum):
  sum_found = False
  new_sum = sum - node.value

  if new_sum == 0 and node.left_child == None and node.right_child == None:
    return True
  else:
    if node.left_child != None:
      sum_found = sum_found or path_sum(node.left_child, new_sum)
    if node.right_child != None:
      sum_found = sum_found or path_sum(node.right_child, new_sum)

  return sum_found


root = Node(4)
root.left_child = Node(2)
root.right_child = Node(6)
root.left_child.left_child = Node(1)
root.left_child.right_child = Node(3)
root.right_child.left_child = Node(5)
root.right_child.right_child = Node(7)

print(path_sum(root, 9))