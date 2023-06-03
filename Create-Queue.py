# Fill in the following class DIYQueue to create a fully functional queue.
# For the .dequeue() and .peek() methods, ensure that your code will return a None value if the queue is empty.
# For the .allNodesString() method, ensure that you BOTH RETURN AND PRINT a visual representation of the queue (i.e. a newline between each element such that the next element to be popped is on the "bottom".
# For this implementation, users must be able to queue either fully formed Nodes or values – if a value is not input as a Node, encapsulate it in a Node before queueing it.

class Node:
  def __init__(self, val):
    self.value = val
    self.next = None
    self.prev = None

class DIYQueue:
  
  first_node = None
  last_node = None
  
  def __init__(self):
    first_node = None
    last_node = None
    
  def queue(self, value):
    new_node = Node(value)
    if isinstance(value, Node) == True:
      new_node = value
    
    if self.first_node == None and self.last_node == None:
      self.first_node = new_node
      self.last_node = new_node
    else:
      new_node.prev = self.first_node
      self.first_node.next = new_node
      self.first_node = new_node

      
  def dequeue(self):
    if self.last_node == None:
      return None
    else: # Remove & return the next element on the queue
      return_node = self.last_node
      self.last_node = self.last_node.next
      self.last_node.prev = None
      return return_node.value

  
  def peek(self):
    if self.last_node == None:
      return None
    else: # Return next element on queue without dequeueing it
      return self.last_node.value


  def allNodesString(self):
    queue_str = ''
    if self.first_node == None and self.last_node == None:
      return queue_str
    else:
      curr_node = self.first_node
      while curr_node != None:
        queue_str += str(curr_node.value) + '\n'
        curr_node = curr_node.prev
    
    print(queue_str, end='')
    return queue_str


# Instantiate + test your code here
my_queue = DIYQueue()
print(my_queue)

my_queue.queue(1)
my_queue.allNodesString()

my_queue.queue(2)
my_queue.allNodesString()

my_queue.queue(3)
my_queue.allNodesString()

my_queue.dequeue()
my_queue.allNodesString()