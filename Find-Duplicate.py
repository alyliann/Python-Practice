# Given a list of integers containing n+1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number, return this repeated number.
# You must solve the problem without modifying the list and uses only constant extra space.
# Complete the function in the given Python file.

def find_duplicate(list_of_nums):
  slow_pointer = 0
  fast_pointer = 0

  while True:
    slow_pointer = list_of_nums[slow_pointer]
    fast_pointer = list_of_nums[list_of_nums[fast_pointer]]
    if slow_pointer == fast_pointer:
      break
  
  slow_pointer = 0
  while slow_pointer != fast_pointer:
    slow_pointer = list_of_nums[slow_pointer]
    fast_pointer = list_of_nums[fast_pointer]
  
  return slow_pointer
  

print(find_duplicate([1,3,4,2,2]))