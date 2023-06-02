#Reverse the passed list "in place".

def reverse_list(arr):
  if (len(arr) < 2):
    return arr
  
  pointer_1 = 0
  pointer_2 = len(arr) - 1
  while (pointer_1 < pointer_2):
    arr[pointer_1], arr[pointer_2] = arr[pointer_2], arr[pointer_1]
    pointer_1 += 1
    pointer_2 -= 1
  return arr
  
test_list = [1,2,3,4]
print(reverse_list(test_list))