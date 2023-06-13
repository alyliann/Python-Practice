# Implement heapify, pop, and heap sort in the file to the left.

def LEFT(i):
  return 2*i + 1
 
def RIGHT(i):
  return 2*i + 2
 
def swap(A, i, j):
  temp = A[i]
  A[i] = A[j]
  A[j] = temp

def heapify(A, i, size):
  if i >= size:
    return

  left_index = LEFT(i)
  right_index = RIGHT(i)
  min_index = 0
  
  if left_index < size and right_index < size and A[left_index] > A[right_index]:
    min_index = right_index
  elif left_index < size:
    min_index = left_index

  if min_index != 0 and A[i] > A[min_index]:
    swap(A, i, min_index)
    heapify(A, min_index, size)

def pop(A, size):
  if size > 0:
    A[0], A[-1] = A[-1], A[0] # swap root with last element
    return A.pop(-1) # pop and return old root
  else:
    return None

def heapsort(A):
  # build heap
  i = len(A) // 2 - 1
  while i >= 0:
    heapify(A, i, len(A))
    i = i - 1

  sorted = []
  size = len(A)

  # sort
  for i in range(len(A)):
    sorted.append(pop(A, size))
    size -= 1
    heapify(A, 0, size)

  # modify A to match sorted heap
  for i in range(len(sorted)):
    A.append(sorted[i])

A = [int(x) for x in input("Enter integers to sort: ").split()]
heapsort(A)
print(A)