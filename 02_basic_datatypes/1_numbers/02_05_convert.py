'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

# convert an int to a float
x = 10
x = float(x)
print(x, " is a float")

# convert a float to an int
x = int(x)
print(x, " is an int")

# Perform floor division using a float and an int
a = 8
b = 2.4
c = 8 // 2.4
print(c)

# Use two user inputted values to perform multiplication
in1 = int(input("Please enter a number: "))
in2 = int(input("Please enter another number: "))

# multiply user inputs and print out
result = in1*in2
print("The product of your numbers is ", result)