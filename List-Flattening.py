# Write the function flatten which accepts a list (possibly containing other lists) and returns the flattened result of that list.

def flatten(lst):
  if len(lst) == 0:
    return []
  else:
    flat = []
    item = lst.pop(0)
    if isinstance(item, list):
      flat = flatten(item)
    if (item == []):
      return flat + flatten(lst)
    else:
      return [item] + flat + flatten(lst)
  
print(flatten([1, 4, [5, 7, 2, [3, 9], 0], 6, [[]]]))