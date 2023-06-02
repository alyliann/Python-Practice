#Write a recursive function called list_sum that takes a list of numbers as a parameter. Return the sum of all of the numbers in the list. Hint, the slice operator will be helpful in solving this problem.

def list_sum(nums):
  if len(nums) == 1:
    return nums[0]
  else:
    return nums.pop() + list_sum(nums)

print(list_sum([1, 2, 3, 4, 5]))