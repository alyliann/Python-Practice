# A simplistic implementation of quick sort is on the left. Improve the pivot picking strategy by choosing the median of the first, middle and last element. Please calculate the middle using floor division.

import numpy

def partition(list_of_data, low, high):
  if (list_of_data[low] <= list_of_data[high] and list_of_data[low] >= list_of_data[high//2]) or (list_of_data[low] >= list_of_data[high] and list_of_data[low] <= list_of_data[high//2]):
    pivot = low
  elif (list_of_data[high] <= list_of_data[low] and list_of_data[high] >= list_of_data[high//2]) or (list_of_data[high] >= list_of_data[low] and list_of_data[high] <= list_of_data[high//2]):
    pivot = high
  else:
    pivot = high//2

  # You don't need to change anything below this point
  # FREEZE CODE BEGINS
  i = (low-1)
  for j in range(low, high):
    if list_of_data[j] <= list_of_data[pivot]: #pivot:
      i = i+1
      list_of_data[i], list_of_data[j] = list_of_data[j], list_of_data[i]

  list_of_data[i+1], list_of_data[high] = list_of_data[high], list_of_data[i+1]
  return (i+1)

def quick_sort(list_of_data, low, high):
  if len(list_of_data) == 1:
    return list_of_data
  if low < high:
    pivot_index = partition(list_of_data, low, high)
    print(list_of_data)
    quick_sort(list_of_data, low, pivot_index-1)
    quick_sort(list_of_data, pivot_index+1, high)

nums = list(map(int, input("Enter the list of integers separated by space ").strip().split()))
quick_sort(nums, 0, len(nums)-1)
# FREEZE CODE ENDS