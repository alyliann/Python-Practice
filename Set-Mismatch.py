# You have a set of integers s, which originally contains all the numbers from 0 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
# You are given an integer list representing the data status of this set after the error.
# Find the number that occurs twice and the number that is missing and return them in the form of a list.

def set_mismatch(arr):
  if len(arr) == 0:
    return []
  
  duplicate = int()
  index = int()
  for i in range(len(arr)):
    correct_index = arr[i]
    while correct_index != i and i < len(arr):
      if correct_index == arr[correct_index]:
        index = i
        duplicate = correct_index
        i += 1
      else:
        arr[i], arr[correct_index] = arr[correct_index], arr[i]
      if i < len(arr):
        correct_index = arr[i]
  
  return [duplicate, index]

test_list = [2, 7, 4, 6, 5, 1, 8, 0, 6]
print(set_mismatch(test_list))