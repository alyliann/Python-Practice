# You are given two lists of intervals. Each list of intervals have no overlapping intervals and in sorted order by start time.
# Return the intersection of these two interval lists.
# At an interval level, the intersection is where the two intervals overlap. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

def list_intersection(list1, list2):
  ptr1 = 0
  ptr2 = 0
  intersection = []

  while ptr1 < len(list1) and ptr2 < len(list2):
    print(ptr1, end='')
    print(list1[ptr1], end=' ')
    print(ptr2, end='')
    print(list2[ptr2])

    #check if 1st interval starts during 2nd:
    if list1[ptr1][0] >= list2[ptr2][0] and list1[ptr1][0] <= list2[ptr2][1]:
      if list1[ptr1][0] == list2[ptr2][1]: #1st interval intersects end of 2nd
        intersection.append([list1[ptr1][0], list1[ptr1][0]])
        if (ptr2 == len(list2)-1):
          ptr1 += 1
        else:
          ptr2 += 1
      elif list1[ptr1][1] < list2[ptr2][1]: #1st interval ends before 2nd
        intersection.append(list1[ptr1])
        if (ptr1 == len(list1)-1):
          ptr2 += 1
        else:
          ptr1 += 1
      else: #2nd interval ends before 1st
        intersection.append([list1[ptr1][0], list2[ptr2][1]])
        if (ptr2 == len(list2)-1):
          ptr1 += 1
        else:
          ptr2 += 1
    
    #check if 2nd interval starts during 1st:
    elif list2[ptr2][0] >= list1[ptr1][0] and list2[ptr2][0] <= list1[ptr1][1]:
      if list2[ptr2][0] == list1[ptr1][1]: #2nd interval intersects end of 1st
        intersection.append([list2[ptr2][0], list2[ptr2][0]])
        if (ptr1 == len(list1)-1):
          ptr2 += 1
        else:
          ptr1 += 1
      elif list2[ptr2][1] < list1[ptr1][1]: #2nd interval ends before 1st
        intersection.append(list2[ptr2])
        if (ptr2 == len(list2)-1):
          ptr1 += 1
        else:
          ptr2 += 1
      else: #1st interval ends before 2nd
        intersection.append([list2[ptr2][0], list1[ptr1][1]])
        if (ptr1 == len(list1)-1):
          ptr2 += 1
        else:
          ptr1 += 1
    
    else:
      if (ptr1 == len(list1)-1):
          ptr2 += 1
      else:
        ptr1 += 1

  return intersection


# change the values below to test different cases
test_list_1 = [[0,2], [8,9]]
test_list_2 = [[2,5], [6,8]]
print(list_intersection(test_list_1, test_list_2))