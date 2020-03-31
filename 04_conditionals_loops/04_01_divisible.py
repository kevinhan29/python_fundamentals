'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''

# get user input
while True:
    x = input("Enter an integer between 1 and 1,000,000,000: ")
    if x.isdigit() and (1 <= int(x) <= 1000000000):      # check to see if user input is an integer and between 1 and 1000000000
        x = int(x)
        break
    else:
        print("Invalid entry!\n")

# check if input is divisible by 3 by using modulo.  A number divisible by 3 will have a modulo of 0
if x % 3 == 0:
    print("\n", x, "IS divisible by 3!\n")
else:
    print("\n", x, "is NOT divisible by 3\n")