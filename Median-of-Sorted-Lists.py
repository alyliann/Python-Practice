# Given k sorted lists, return the median of all the lists.

import heapq

def median_of_sorted(list_of_lists):
  min_heap = []
  merged = []
  n = 0

  for i in range(len(list_of_lists)):
    n += len(list_of_lists[i])
    heapq.heappush(min_heap, [list_of_lists[i][0], i, 0])

  while len(merged) < n:
    tupl = heapq.heappop(min_heap)
    heapq.heappush(merged, tupl[0]) # pop min_heap into merged
    liist = tupl[1]
    index = tupl[2]
    
    if len(list_of_lists[liist]) > index + 1:
      heapq.heappush(min_heap, [list_of_lists[liist][index+1], liist, index+1])

  i = 0
  j = len(merged)-1
  while i < j:
    i += 1
    j -= 1
  
  if i == j:
    return merged[i]
  else:
    return float((merged[i] + merged[j]) / 2)

print(median_of_sorted([[1,2,3,4],[5,6,7,8]]))