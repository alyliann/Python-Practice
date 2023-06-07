# Given the root of a binary tree, return the inorder traversal of its nodes’ values.
# Complete the function in the given Python file.

class Node:
  def __init__(self, val):
    self.value = val
    self.left_child = None
    self.right_child = None

def inorder(node):
  if node:
    return (inorder(node.left_child) + str(node.value) + ' ' + inorder(node.right_child))
  else:
    return ''

root = Node(4)
root.left_child = Node(2)
root.right_child = Node(6)
root.left_child.left_child = Node(1)
root.left_child.right_child = Node(3)
root.right_child.left_child = Node(5)
root.right_child.right_child = Node(7)

print(inorder(root))