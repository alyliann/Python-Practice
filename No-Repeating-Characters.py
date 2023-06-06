# Given a string, return the number of substrings of length three​​​ where there are no repeated characters.
# Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

def length_three_substrings(string):
  if len(string) < 3:
    return 0
  
  pointer1 = 0
  pointer2 = 3
  count = 0
  condition = False

  while pointer2 <= len(string):
    temp = ''
    for i in range(pointer1, pointer2):
      if temp.count(string[i]) > 0:
        condition = True
      temp += string[i]
    
    if condition == False:
      count += 1

    pointer1 += 1
    pointer2 += 1

  return count

print(length_three_substrings("abcdef"))