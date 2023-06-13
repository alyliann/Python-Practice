# Implement the heapify function for a max heap in the code file to the left.

def LEFT(i):
    return 2*i + 1
 
def RIGHT(i):
    return 2*i + 2
 
def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
 
def heapify(A, i):
  size = len(A)
  left_index = LEFT(i)
  right_index = RIGHT(i)
  max_index = 0
  
  if left_index < size and right_index < size and A[left_index] < A[right_index]:
    max_index = right_index
  elif left_index < size:
    max_index = left_index

  if max_index != 0 and A[i] < A[max_index]:
    swap(A, i, max_index)
    heapify(A, max_index)
 
A = [int(x) for x in input("Enter integers to insert into heap:").split()]

# Build-heap
i = len(A) // 2 - 1
while i >= 0:
    heapify(A, i)
    i = i - 1
print(A)