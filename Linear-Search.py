# Implement Linear Search

def search(search, find):
  for i in range(len(search)):
    if search[i] == find:
      return i
  return -1

# FREEZE CODE BEGINS
nums = list(map(int, input("Enter the list of integers separated by space ").strip().split()))
find = int(input("Enter the integer to search for: "))
print(search(nums, find))
# FREEZE CODE ENDS