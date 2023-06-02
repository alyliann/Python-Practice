# Complete the merge sort implementation in the file to the left. You need to complete the method which merges the two sub-lists.

def combine_sorted_lists(list_one, list_two):
  combined = []
  pointer_1 = 0
  pointer_2 = 0
  while pointer_1 != len(list_one) and pointer_2 != len(list_two):
    if list_one[pointer_1] <= list_two[pointer_2]:
      combined.append(list_one[pointer_1])
      pointer_1 += 1
    else:
      combined.append(list_two[pointer_2])
      pointer_2 += 1
  if pointer_1 != len(list_one):
    while pointer_1 != len(list_one):
      combined.append(list_one[pointer_1])
      pointer_1 += 1
  elif pointer_2 != len(list_two):
    while pointer_2 != len(list_two):
      combined.append(list_two[pointer_2])
      pointer_2 += 1
  return combined

def merge_sort(the_list):
  if len(the_list) <= 1:
      return the_list

  middle_index = len(the_list) // 2
  left  = the_list[:middle_index]
  right = the_list[middle_index:]

  left_sorted  = merge_sort(left)
  right_sorted = merge_sort(right)

  print(left_sorted)
  print(right_sorted)

  return combine_sorted_lists(left_sorted, right_sorted)

nums = list(map(int, input("Enter the list of integers separated by space ").strip().split()))
print(merge_sort(nums))