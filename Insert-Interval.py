# You are given an array of non-overlapping intervals sorted in ascending order by start time. You are also given an interval that represents the start and end of another interval.
# Insert the new interval into the list of intervals such that the intervals are still sorted in ascending order by start time and the intervals still do not have any overlap (merge overlapping intervals if necessary).
# Return the intervals after the insertion

def check_merged(arr):
  for i in range(len(arr)-1, 1, -1):
    j = 0
    while j != i:
      if (arr[i][0] == arr[j][0] and i != j):
        arr.pop(j)
        i -= 1
      else:
        j += 1
  return arr

def merge_intervals(arr):
  if (len(arr) == 0):
    return []
  elif (len(arr) == 1):
    return arr

  merged = []
  merged_interval = []
  check = 1
  starting_interval = arr[0]

  while check < len(arr):
    checking_interval = arr[check]
    interval = starting_interval[1] - starting_interval[0]
    if checking_interval[0] <= starting_interval[0] + interval:
      starting_interval = [starting_interval[0], max(starting_interval[1], checking_interval[1])]
      merged.append(starting_interval)
    else:
      starting_interval = checking_interval
    check += 1

  if (len(merged) > 1):
    return check_merged(merged)
  elif (len(merged) == 0):
    return arr
  else:
    return merged

def insert_interval(arr, new):
  if len(arr) == 0:
    return new
  elif len(new) == 0:
    return arr

  arr.append(new)
  arr.sort()
  return merge_intervals(arr)

# change the values below to test different cases
test_list = [[1,3], [5,6]]
print(insert_interval(test_list, [2,4]))