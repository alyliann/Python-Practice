# Given a list of distinct integers, return all the possible permutations.
# For example:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

def permutations(nums, index=0, current=[]):
  if len(nums) < 2:
    return [nums]
  if index == len(nums):
    return current
  
  for i in range(len(nums)):
    if i == index:
      continue
    temp = []
    temp.append(nums[index])
    temp.append(nums[i])
    current.append(temp)

  return permutations(nums, index+1, current)

print(permutations([1,2]))