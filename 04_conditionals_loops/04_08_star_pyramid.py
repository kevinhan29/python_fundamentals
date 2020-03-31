'''
Write a script that takes in a number from the user as input and prints the following structure.

Suppose the input is 5, you will output
*
* *
* * * 
* * * *
* * * * * 
i.e. number of rows will be 5, 1st row will have 1 star, 2nd row will have 2 stars, 3rd row 3 stars, 4th row will have 4 stars and 5th row will have 5 stars.

Another example: if input is 3, you will output
*
* *
* * *

Hint: Think of nested for loops

'''

# asks user to input integer and checks if input is an int
while True:
    try:
        x = int(input("\nEnter an integer: "))
        break
    except:
        print("\nThat is not an integer!")

for i in range(1, x + 1):
    print(i*"*")