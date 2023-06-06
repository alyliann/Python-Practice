# Implement pre-order and post-order traversal in the code file.

class Node:
  def __init__(self, val):
    self.value = val
    self.left_child = None
    self.right_child = None

def preorder(node):
  if node:
    print(node.value, end=' ')
    preorder(node.left_child)
    preorder(node.right_child)

def inorder(node):
  if node:
    inorder(node.left_child)
    print(node.value, end=' ')
    inorder(node.right_child)

def postorder(node):
  if node:
    postorder(node.left_child)
    postorder(node.right_child)
    print(node.value, end=' ')

# FREEZE CODE BEGINS
root = Node(5)
root.left_child = Node(3)
root.right_child = Node(8)
root.left_child.left_child = Node(1)
root.left_child.right_child = Node(4)
root.right_child.left_child = Node(7)
root.right_child.right_child = Node(9)

print('Preorder:')
preorder(root)
print('\nInorder:')
inorder(root)
print('\nPostorder:')
postorder(root)
# FREEZE CODE ENDS