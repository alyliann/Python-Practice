# Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.
# The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
# The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A.
# Complete the function in the given Python file.

class Node:
  def __init__(self, val):
    self.value = val
    self.left_child = None
    self.right_child = None

def height(node):
  if not node:
      return 0
  return max(height(node.left_child), height(node.right_child)) + 1

def common_ancestor(node, current_depth = 0, max_depth = 0):
  if max_depth == 0:
    max_depth = height(node) - 1

  if node == None:
    return None
  if current_depth == max_depth:
    return node

  left = common_ancestor(node.left_child, current_depth + 1, max_depth)
  right = common_ancestor(node.right_child, current_depth + 1, max_depth)

  if left != None and right != None:
    return node
  elif left != None:
    return left
  else:
    return right
  

root = Node(4)
root.left_child = Node(2)
root.right_child = Node(6)
root.left_child.left_child = Node(1)
root.left_child.right_child = Node(3)
root.right_child.left_child = Node(5)
root.right_child.right_child = Node(7)

print(common_ancestor(root).value)