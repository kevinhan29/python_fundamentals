'''
Take two numbers from the user, one representing the start and one the end of a sequence.
Using a loop, sum all numbers from the first number through to the second number.

For example, if a user enters 1 and 100, the sequence would be all integer numbers from 1 to 100.
The output of your calculation should therefore look like this:

The sum is: 5050
'''
is_int = False          # keeps track of if user input is an integer or not
# ask user for starting integer
while not is_int:
    try:                #check whether input is an integer or not
        start = int(input("Enter a starting integer: "))
        is_int = True
        #print(is_int)
    except:
        print("That's not an integer!\n")

is_int = False
# ask user for ending integer
while not is_int:
    try:                #check whether input is an integer or not
        end = int(input("Enter a ending integer: "))
        is_int = True
        #print(is_int)
    except:
        print("That's not an integer!\n")

sum_ = 0                # holds the sum integers

# sum up all numbers from start to end integer
for i in range(start, end + 1):
    sum_ += i

print("\nThe sum of all numbers from", start, "to", end, "is", sum_)