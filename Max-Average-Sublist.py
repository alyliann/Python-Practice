# You are given a list consisting of n elements, and an integer k.
# Find a contiguous sublist whose length is equal to k that has the maximum average value and return this value.

def max_sublist(list_of_nums, k):
  if len(list_of_nums) == 0 or len(list_of_nums) < k:
    return None
  
  pointer1 = 0
  pointer2 = k
  max_avg = 0

  while pointer2 <= len(list_of_nums):
    sub_avg = 0.0
    for i in range(pointer1, pointer2):
      sub_avg += list_of_nums[i]

    sub_avg /= k
    if sub_avg > max_avg:
      max_avg = sub_avg
    
    pointer1 += 1
    pointer2 += 1

  return max_avg

print(max_sublist([1,12,-5,-6,50,3], 4)) # expected output 12.75