# Given a list of integers of length n where all the integers are in the range [0, n] and each integer appears once or twice, return a list of all the integers that appears twice.

def find_duplicates(arr):
  duplicates = []

  for i in range(1, len(arr)):
    if arr.count(arr[i]) > 1 and duplicates.count(arr[i]) == 0:
      duplicates.append(arr[i])
  
  duplicates.sort(reverse=True)
  return duplicates

test_list = [2, 2, 4, 5, 5, 1, 3]
print(find_duplicates(test_list))