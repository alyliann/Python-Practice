# Implement a recursive list intersection algorithm. It accepts two lists and returns a list consisting of all elements that are in both lists.

def intersection(list1, list2):
  if len(list1) == 0 or len(list2) == 0:
    return []
  else:
    item = list1.pop(0)
    if (list2.count(item) != 0):
      return [item] + intersection(list1, list2)
    else:
      return [] + intersection(list1, list2)

print(intersection(['a','b','c'], ['c','d','e']))