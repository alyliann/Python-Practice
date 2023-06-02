# Write a recursive function called get_max that takes a list of numbers as a parameter. Return the largest number in the list.

def get_max(nums):
  if len(nums) == 1:
    return nums[0]
  else:
    nums.remove(min(nums[len(nums) - 1], nums[len(nums) - 2]))
    return get_max(nums)

print(get_max([1, 2, 3, 4, 5]))