# Implement Binary Search

def binary_search(search, find, first_index, last_index):
  if len(search) == 0:
    return -1
  else:
    middle_index = (last_index - first_index)//2 + first_index
    if find == search[middle_index]:
      return middle_index
    elif find < search[middle_index]:
      return binary_search(search, find, first_index, middle_index)
    else:
      return binary_search(search, find, middle_index, last_index)

# FREEZE CODE BEGINS
nums = list(map(int, input("Enter the list of integers separated by space ").strip().split()))
find = int(input("Enter the integer to search for: "))
nums.sort() #make sure the list is sorted!
print(binary_search(nums, find, 0, len(nums)-1))
# FREEZE CODE ENDS