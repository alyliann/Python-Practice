# Given a list of integers that may contain duplicates, return all possible subsets (the power set).

def subsets2(nums, helper=[], subset=[]):
  
  subset.append(helper)

  for i in range(len(nums)):
    if i > 0 and nums[i] == nums[i-1]:
      continue
    subsets2(nums[i+1:], helper+[nums[i]], subset)

  return subset

print(subsets2([1,2,2])) # Expected output: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]