# Write a recursive function called reverse_string that takes a string as a parameter. Return the string in reverse order. Hint, the slice operator will be helpful when solving this problem.

def reverse_string(str):
  if len(str) == 0:
    return ''
  else:
    slice_str = slice(len(str) - 1)
    return str[len(str) - 1] + reverse_string(str[slice_str])

print(reverse_string("house"))