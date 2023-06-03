# Write a function called paren_balanced() that takes in a string of parentheses and returns True if the parentheses are balanced, and False if they are not.
# Note: the string will only consist of ( and ) characters.

# Starter code #
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()
# Starter code #


def paren_balanced(string_s):
  if len(string_s) == 0:
    return True
  elif len(string_s) == 1:
    return False
  
  parentheses = Stack()
  for char in string_s:
    if char == '(':
      parentheses.push(char)
    else:
      if parentheses.isEmpty() == True:
        return False
      else:
        top_char = parentheses.pop()
        if top_char != '(':
          return False

  return True
            

# Testing section #
# Balanced: should return True
print(paren_balanced('(())'))
print(paren_balanced('(())()(())'))
print(paren_balanced(''))
print(paren_balanced('()'))
                
# Unbalanced: should return False
print(paren_balanced(')'))
print(paren_balanced('('))
print(paren_balanced('))'))
print(paren_balanced('(()))(())'))