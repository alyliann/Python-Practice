# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array.
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

def average_levels(root):
    averages = []
    queue = Queue()
    queue.enqueue(root)

    while queue.isEmpty() != True:
        num_nodes = 0.0
        sum = 0.0
        temp_queue = Queue()

        while queue.isEmpty() != True:
            node = queue.dequeue()
            sum += node.value
            num_nodes += 1

            if node.left_child != None:
                temp_queue.enqueue(node.left_child)
            if node.right_child != None:
                temp_queue.enqueue(node.right_child)
        
        queue = temp_queue
        averages.append(sum/num_nodes)
    
    return averages


root = Node(4)
root.left_child = Node(1)
root.right_child = Node(3)
root.left_child.left_child = Node(1)
root.left_child.right_child = Node(1)

print(average_levels(root))