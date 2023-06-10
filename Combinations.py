# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
# For example:
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

def combinations(n, k, start=1, current=[]):
  if n == 1:
    return [[n]]
  if start == n:
    return current
  
  for i in range(n - start):
    temp = []
    temp.append(start)
    temp.append(start+i+1)
    current.append(temp)

  return combinations(n, k, start+1, current)

print(combinations(4, 2))