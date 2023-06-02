# Write a recursive function called bunny_ears that takes the number of bunnies (an integer) as a parameter. Return the number of bunny ears (2 per bunny). Do not use multiplication; instead use addition.

def bunny_ears(num):
  if num == 0:
    return 0
  else:
    return 2 + bunny_ears(num-1)

print(bunny_ears(0))