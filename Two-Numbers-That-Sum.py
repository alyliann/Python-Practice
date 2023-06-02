# Given an array of integers (already sorted in ascending order) find and return the indices of the two elements that, when added together, are equal to the provided target value.

def nums_that_sum(arr, sum):
  if len(arr) == 0:
    return 0, 0
  pointer_1 = 0
  pointer_2 = len(arr) - 1
  while (pointer_1 != pointer_2):
    pointer_sum = arr[pointer_1] + arr[pointer_2]
    if pointer_sum == sum:
      return pointer_1, pointer_2
    elif pointer_sum < sum:
      pointer_1 += 1
    else: #if pointer_sum > sum
      pointer_2 -= 1
  return 0, 0

# change the values below to test different cases
test_list = [1]
print(nums_that_sum(test_list, 1))