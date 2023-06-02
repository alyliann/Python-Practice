# Implement insertion sort. Print out the list after each swap has occurred.

def insertion_sort(arr):
  if len(arr) < 2:
    return arr
  print(arr)
  for i in range(1, len(arr)):
    curr = i
    while curr != 0 and (arr[curr] < arr[curr-1]):
      arr[curr], arr[curr-1] = arr[curr-1], arr[curr]
      curr -= 1
    print(arr)

nums = list(map(int, input("Enter the list of integers separated by space ").strip().split()))
insertion_sort(nums)