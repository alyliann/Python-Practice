# Given a string s, find the length of the longest substring without duplicate characters.

def longest_substring(string):
  fast_pointer = 0
  max_length = 0
  seen = []

  while fast_pointer < len(string):
    char = string[fast_pointer]
    if seen.count(char) == 0: # if char has not been found
      seen.append(char)
    else: # if duplicate char found
      max_length = len(seen)

    fast_pointer += 1
  
  if max_length != len(seen):
    max_length = len(seen)
  
  return max_length

print(longest_substring('a'))