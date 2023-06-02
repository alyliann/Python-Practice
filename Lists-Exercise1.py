# Write a program that takes a list of integers called numbers and replaces each element greater than 10 with a '*'. Print the new version of numbers.

# FREEZE CODE BEGINS
import sys

numbers = sys.argv [1:]
for i in range (len (numbers)):
    numbers[i] = int(numbers[i])
# FREEZE CODE ENDS

for i in range(len(numbers)):
    if numbers[i] > 10:
        numbers[i] = '*'
            
print (numbers)