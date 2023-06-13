# Given a binary min heap and a value k, return a list of all the binary heap nodes having value less than the given value k.
# Complete the function in the given Python file.

import heapq

# pop removes and returns the root of the heap
def pop(A):
  return heapq.heappop(A)

def less_than_k(A, k):
  ans = []
  num = pop(A)

  for i in range(len(A)):
    if num < k:
      ans.append(num)
    num = pop(A)

  return ans

# test code
A = [1,3,5,7,2,6,4]
heapq.heapify(A)
print(less_than_k(A, 4)) # Expected output: [1, 2, 3]