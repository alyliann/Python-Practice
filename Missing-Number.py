# Given a list containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the list.

def missing_number(arr):
  if len(arr) == 0:
    return None
  
  index = -1
  for i in range(len(arr)):
    correct_index = arr[i]
    while correct_index != i:
      correct_index = arr[i]
      if correct_index > len(arr)-1:
        index = i
        i += 1
      else:
        arr[i], arr[correct_index] = arr[correct_index], arr[i]
  
  if index >= 0:
    return index
  else:
    return None

test_list = [2, 7, 4, 6, 5, 1, 0]
print(missing_number(test_list))