'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''

# prompt user to enter 10 integers and store into a list
num_list = []
for x in range(10):
    temp = int(input("Please enter an integer: "))
    num_list.append(temp)
print(num_list)

product = 1                         # holds product of all numbers
for x in num_list:                  # iterate through list and multiplies with above product
    product *= x
    #print(product)

# print results
print("The largest number is", max(num_list))
print("The product of all numbers is", product)