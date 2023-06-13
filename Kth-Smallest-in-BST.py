# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
# Complete the function in the given Python file.

import heapq

def smallest_in_bst(root, k):
  max_heap = []

  for i in range(len(root)):
    if root[i]:
      root[i] *= -1 # make numbers negative to take advantage of heapq min heap properties
      if len(max_heap) < k or root[i] > max_heap[0]:
        heapq.heappush(max_heap, root[i])
      if len(max_heap) > k:
        heapq.heappop(max_heap)
    
  return max_heap[0] * -1

root = [5,3,6,2,4,None,None,1]
k = 3

print(smallest_in_bst(root, k)) # expected output: 3