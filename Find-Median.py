# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.
# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:
# MedianFinder() initializes the MedianFinder object.
# addNum(int num) adds the integer num from the data stream to the data structure.
# findMedian() returns the median of all elements so far.

import heapq

class MedianFinder:
  def __init__(self):
    self.heap = []
       
  def addNum(self, num: int) -> None:
    median = self.findMedian()
    if median == None:
      median = num
    
    heapq.heappush(self.heap, num)

  def findMedian(self) -> float:
    if len(self.heap) == 0:
      return None

    i = 0
    j = len(self.heap)-1
    
    while i < j:
      i += 1
      j -= 1
    
    if i == j:
      return float(self.heap[i])
    else:
      return float((self.heap[i] + self.heap[j]) / 2)


## test inputs
input_commands = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
input_values = [[], [1], [2], [], [3], []]
# driver code
output = []
obj = None

for i in range(len(input_commands)):
  if input_commands[i] == "MedianFinder":
    obj = MedianFinder()
    output.append(None)
  elif input_commands[i] == "addNum":
    obj.addNum(input_values[i][0])
    output.append(None)
  elif input_commands[i] == "findMedian":
    output.append(obj.findMedian())

print(output)