# Write a program that accepts a 2D list of zeros. Print the 2D list in rows and columns without the square brackets and commas. Moving diagonally from the top-left to the bottom right, replace each 0 with a 1. The IDE already declares the variable number and the 2D list data. Use number to represent the number of rows and columns, and data to represent the 2D list of zeros.

# FREEZE CODE BEGINS
import sys

number = int(sys.argv[1])
data = [[O for i in range(number)] for j in range(number)]
# FREEZE CODE ENDS

for i in range(len(data)):
  for j in range(len(data[i])):
    if i == j:
      data[i][j] = 1
    print(f"{data[i][j]} ", end="")
  print()