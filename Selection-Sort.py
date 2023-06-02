# Implement Selection Sort. Print out the list after each swap has occurred.

def selection_sort(arr):
  if len(arr) < 2:
    return arr
  start = 0
  while start < len(arr):
    min_index = start
    for i in range(start, len(arr)):
      if arr[i] < arr[min_index]:
        min_index = i
    arr[start], arr[min_index] = arr[min_index], arr[start]
    print(arr)
    start += 1
    
nums = list(map(int, input("Enter the list of integers separated by space ").strip().split()))
selection_sort(nums)