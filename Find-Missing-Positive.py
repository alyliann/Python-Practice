# Given an unsorted integer list, return the smallest missing positive integer.
# Note: The integers are not necessarily within a certain range and may include negative values.


def missing_positive(arr):
  if len(arr) == 0:
    return None
  elif arr.count(0) == 0:
    return 0

  original_len = len(arr)

  i = 0
  while i < len(arr):
    if (arr[i] < 0):
      arr.pop(i) #remove negative integers from list
    i += 1

  found = False
  min = 0
  while found != True: 
    for i in range(len(arr)):
      if arr[i] < arr[min]:
        min = i

    if arr.count(arr[min]+1) == 0: #missing number found
      found = True
    else:
      arr.pop(min)
      min = 0
  
  if (arr[min]+1 >= original_len):
    return None
  else:
    return arr[min]+1
    
test_list = [3,2,1,0,6,5]
print(missing_positive(test_list))