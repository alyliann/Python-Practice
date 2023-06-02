# Remove duplicates from sorted array

def remove_duplicates(arr):
  if (len(arr) < 2):
    return arr
  
  pointer_1 = 0
  pointer_2 = 1
  while (pointer_2 != len(arr)):
    if (arr[pointer_1] == arr[pointer_2]): #duplicate found
      arr.remove(arr[pointer_1])
    else:
      pointer_1 += 1
      pointer_2 += 1
  return arr 
  
# change the values below to test different cases
test_list = [2]
print(remove_duplicates(test_list))