# Given a list of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0). A helper function called distance_to_origin has been provided which takes the coordinates of the point and returns the distance to the origin.
# Complete the function in the given Python file.

import heapq, math

def distance_to_origin(x,y):
  return math.sqrt( pow(x,2) + pow(y,2) )

def k_closest(points, k):
  min_heap = []

  for point in points:
    if len(min_heap) < k or distance_to_origin(point[0], point[1]) < distance_to_origin(min_heap[-1][0],min_heap[-1][1]):
      heapq.heappush(min_heap, point)
    if len(min_heap) > k:
      max_index = 0
      for i in range(1, len(min_heap)):
        if distance_to_origin(min_heap[i][0], min_heap[i][1]) > distance_to_origin(min_heap[max_index][0], min_heap[max_index][1]):
          max_index = i
      min_heap.pop(max_index)
    
  return min_heap
  

points = [[1,3],[-2,2]]
k = 1

print(k_closest(points, k)) # expected output: [[-2, 2]]