# Given a list of integers that might contain duplicates, return all possible unique permutations.
# For example:
# Input: nums = [1,1,2]
# Output:[[1,1,2], [1,2,1], [2,1,1]]

def permutations2(nums, helper=[], current=[]):
  if not nums:
    if current.count(helper[::]) == 0:
      current.append(helper[::])

  for i in range(len(nums)):
    helper.append(nums[i])
    permutations2(nums[:i] + nums[i+1:], helper, current)
    helper.pop(-1)

  return current

print(permutations2([1,1,2]))