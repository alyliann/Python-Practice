# You are given a list of integers, there is a sliding window of size k which is moving from the very left of the list to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.
# For example:
# [1,3,-1,-3,5,3,6,7]
# k = 3
# Output: [3,3,5,5,6,7]

def sliding_window_max(list_of_nums, k):
  if len(list_of_nums) == 0 or len(list_of_nums) < k:
    return None
  
  pointer1 = 0
  pointer2 = k
  max_window = []

  while pointer2 <= len(list_of_nums):
    temp_max = list_of_nums[pointer1]
    for i in range(pointer1+1, pointer2):
      if list_of_nums[i] > temp_max:
        temp_max = list_of_nums[i]

    max_window.append(temp_max)
    
    pointer1 += 1
    pointer2 += 1

  return max_window

print(sliding_window_max([1,3,-1,-3,5,3,6,7], 3))