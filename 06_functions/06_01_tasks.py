'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean
def four_or_seven(num: int) -> bool:
    if (num % 4 == 0) or (num % 7 == 0):
        return True
    else:
        return False

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean
def four_and_seven(num: int) -> bool:
    if (num % 4 == 0) and (num % 7 == 0):
        return True
    else:
        return False

# take in a number from the user between 1 and 1,000,000,000
while True:
    try:
        x = int(input("\nEnter an integer between 1 and 1,000,000,000: "))
    except:
        print("\nThat is not an integer!")
        continue
    if 1 <= x <= 1000000000:
        break
    else:
        print("\nThat number is out of range!")

# call your functions, passing in the user input as the arguments, and set their output equal to new variables 
a = four_or_seven(x)
b = four_and_seven((x))

# print your new variables to display the results
print(f"{x} is divisible by 4 or 7: {a}")
print(f"{x} is divisble by 4 and 7: {b}")