'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''

# prompt user to enter numbers to be added into a list
user_input = None
num_list = []               # list to store user input numbers
while user_input != "x":
    user_input = input("Please enter an integer to add into the list (enter x to finish): ")
    if user_input.isdigit():
        num_list.append(int(user_input))
    print("Current List:", num_list, "\n")

# sort and print list
num_list.sort()
print("Sorted List:", num_list)

# add a 0 to the end of the list if there are an odd number of objects
if len(num_list)/2 != len(num_list)//2:
    num_list.append(0)
#print(num_list)

tuple_list = []         # list to store pairs of tuples
# pop number pairs into tuples and store into tuple_list
while len(num_list) != 0:
    temp = (num_list.pop(0), num_list.pop(0))
    tuple_list.append(temp)
    #print(tuple_list)

# print results
print(tuple_list)