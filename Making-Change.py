# Given an amount of cents, what is the minimum number of coins you can use that add up to that amount of money?

amount_of_change = int(input("Enter an amount of cents: "))

quarters = 0
dimes = 0
nickels = 0
pennies = 0

# WRITE YOUR CODE HERE
while amount_of_change >= 25:
    quarters += 1
    amount_of_change -= 25
while amount_of_change >= 10:
    dimes += 1
    amount_of_change -= 10
while amount_of_change >= 5:
    nickels += 1
    amount_of_change -= 5
while amount_of_change >= 1:
    pennies += 1
    amount_of_change -= 1
# WRITE YOUR CODE HERE

print(str(quarters) + " quarter(s)")
print(str(dimes) + " dime(s)")
print(str(nickels) + " nickel(s)")
print(str(pennies) + " pennies")