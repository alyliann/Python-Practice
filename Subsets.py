# Given a list of unique integers, return all possible subsets (the power set).

def subsets(nums, start=0, current=[[]]):
  if start == len(nums):
    if current.count(nums) == 0:
      current.append(nums)
    return current
  else:
    subsets(nums, start+1, current)
    if current.count([nums[start]]) == 0:
      current.append([nums[start]])
    subsets(nums, start+1, current)

  return current

print(subsets([]))