# Given a list of integers and an integer k, return the kth largest element in the list.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Complete the function in the given Python file.

import heapq

def kth_largest(nums, k):
  min_heap = []
  
  for num in nums:
    if len(min_heap) < k or num > min_heap[0]:
      min_heap.append(num)
    if len(min_heap) > k:
      min_heap.pop(0)
    
  return min_heap[0]

nums = [3,2,1,5,6,4]
k = 2

print(kth_largest(nums, k)) # expected output: 5