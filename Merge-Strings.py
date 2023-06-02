# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1.
# If a string is longer than the other, append the additional letters onto the end of the merged string. Return the merged string.

def merge_strings_alt(word1, word2):
  if (len(word1) == 0):
    return word2
  elif (len(word2) == 0):
    return word1
  else:
    merged = '' #empty string
    pointer = 0
    while (pointer != len(word1) and pointer != len(word2)):
      merged += word1[pointer]
      merged += word2[pointer]
      pointer += 1
    if len(word1) > len(word2):
      while (pointer != len(word1)):
        merged += word1[pointer]
        pointer += 1
    elif len(word1) < len(word2):
      while (pointer != len(word2)):
        merged += word2[pointer]
        pointer += 1
    return merged

print(merge_strings_alt('123456789', 'ABCDEFG'))