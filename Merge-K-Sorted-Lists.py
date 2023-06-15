# You are given a list of k sorted lists. Each list is sorted in ascending order.
# Merge all the sorted lists into one sorted list and return it.

import heapq

def merge_sorted(list_of_lists):
  min_heap = []
  merged = []
  n = 0

  for i in range(len(list_of_lists)):
    n += len(list_of_lists[i])
    heapq.heappush(min_heap, [list_of_lists[i][0], i, 0]) # push element, list index, and element index in list as a 3-element list

  while len(merged) < n:
    tupl = heapq.heappop(min_heap)
    heapq.heappush(merged, tupl[0]) # pop min_heap into merged
    liist = tupl[1]
    index = tupl[2]
    
    if len(list_of_lists[liist]) > index + 1:
      heapq.heappush(min_heap, [list_of_lists[liist][index+1], liist, index+1])

  return merged

print(merge_sorted([[1,4,5],[1,3,4],[2,6]]))