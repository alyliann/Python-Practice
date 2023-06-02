#Write a recursive function called recursive_sum that takes an integer as a parameter. Return the sum of all integers between 0 and the number passed to recursive_sum.

def recursive_sum(num):
  if num == 1:
    return 1
  for i in range(num):
    return num + recursive_sum(num - 1)

print(recursive_sum(10))