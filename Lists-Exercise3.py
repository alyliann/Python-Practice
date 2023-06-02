#Write a program that takes a list called strings that contains a random selection of strings. Your program should print the first string when arranged in alphabetical order.

# FREEZE CODE BEGINS
import sys

strings = sys.argv [1:]
# FREEZE CODE ENDS

strings.sort()
print(strings[0])