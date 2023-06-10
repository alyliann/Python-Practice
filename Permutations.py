# Given a list of distinct integers, return all the possible permutations.
# For example:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

def permutations(nums, helper=[], current=[]):
  if not nums:
    current.append(helper[::])

  for i in range(len(nums)):
    helper.append(nums[i])
    permutations(nums[:i] + nums[i+1:], helper, current)
    helper.pop(-1)
    
  return current

print(permutations([1,2,3]))