# Write a program that takes a list called my_list (it could be a list of any data type) and prints the list three times if the length of the list is less than 5. If the length of my_list is greater than or equal to 5, then print the list one time.

# FREEZE CODE BEGINS
import sys

my_list = sys.argv[1:]
# FREEZE CODE ENDS

if len(my_list) < 5:
  print(my_list + my_list + my_list)
else:
  print(my_list)