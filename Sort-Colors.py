# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

def sort_red_white_blue(arr):
  if (len(arr) == 0):
    return arr

  pointer_1 = 0
  pointer_2 = 0
  pointer_3 = len(arr) - 1
  while (pointer_2 != pointer_3 + 1):
    if (arr[pointer_2] == 0):
      arr[pointer_1], arr[pointer_2] = arr[pointer_2], arr[pointer_1]
      pointer_1 += 1
      pointer_2 += 1
    elif (arr[pointer_2] == 1):
      pointer_2 += 1
    else: #arr[pointer_2] == 2
      arr[pointer_2], arr[pointer_3] = arr[pointer_3], arr[pointer_2]
      pointer_3 -= 1
  
  return arr
  
# change the values below to test different cases
test_list = [0,1,2,0,1,2,0,1,2]
print(sort_red_white_blue(test_list))