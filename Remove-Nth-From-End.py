# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# Example:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]


class Node:
  def __init__(self, value = None, next = None):
    self.value = value
    self.next = next

  def next_node(self):
    return self.next

  def get_value(self):
    return self.value

def remove_n_from_end(head_node, n):
  if head_node.next_node() == None: #if head_node is the only node in Linked List
    return None
  
  last_node = head_node
  prev_node = head_node
  count = 0
  delete_head = True
  
  # Set prev_node equal to node pointing to nth node from end,
  # and set last_node equal to the last node in Linked List:
  while last_node.next_node() != None:
    if count >= n-1 and delete_head != False:
      delete_head = False
    if count >= n:
      prev_node = prev_node.next_node()
    count += 1
    last_node = last_node.next_node()

  print(prev_node.get_value())

  # Remove desired node from Linked List:

  if delete_head == True: #if the head_node is the node to delete
    head_node = head_node.next_node()
  else:
    prev_node.next = prev_node.next_node().next_node()

  return head_node

# TESTING CODE

# Build LL
node_150 = Node(150, None)
node_10 = Node(10, node_150)
node_204 = Node(204, node_10)
node_109 = Node(109, node_204)
node_90 = Node(90, node_109)
# print LL
head = node_90
temp = head
while(temp!=None):
  print(temp.get_value(), end=" ")
  temp = temp.next_node()
print()
# remove and re-print
head = remove_n_from_end(node_90, 1) #remove 150
temp = head
while(temp!=None):
  print(temp.get_value(), end=" ")
  temp = temp.next_node()