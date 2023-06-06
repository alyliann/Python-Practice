# Given a string and an integer k, return the maximum number of vowel letters in any substring with length k.
# Vowel letters in English are 'a’, 'e’, 'i’, 'o’, and 'u’.

def max_vowels_substring(string, k):
  vowels = 'aeiou'

  pointer1 = 0
  pointer2 = k

  max_vowels = 0

  while pointer2 <= len(string):
    temp = 0
    for i in range(pointer1, pointer2):
      if vowels.count(string[i]) != 0:
        temp += 1
    
    if temp > max_vowels:
      max_vowels  = temp

    pointer1 += 1
    pointer2 += 1

  return max_vowels

print(max_vowels_substring("aeiou", 2))