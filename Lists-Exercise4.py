#Write a program that takes a list called numbers that contains integers in a sequence (the sequence is always increasing, never decreasing). Your program should add the next two numbers in the sequence, and then print the list.

# FREEZE CODE BEGINS
import sys

numbers = sys.argv [1:]
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
# FREEZE CODE ENDS

num = numbers[len(numbers) - 1]
numbers.append(num + 1)
numbers.append(num + 2)

print(numbers)