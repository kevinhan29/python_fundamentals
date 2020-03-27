'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''

# asks for user inputs
a = input("Enter a string: ")
b = input("Enter another string: ")
c = input("Enter one last string: ")

# gets length of each string and prints result
a_len = len(a)
b_len = len(b)
c_len = len(c)
print(a_len, ", ", a, "\n", b_len, ", ", b, "\n", c_len, ", ", c, sep='')

# print the string with the most characters
if (a_len > b_len) and (a_len > c_len):
    print(a, "has the most characters")
elif (b_len > a_len) and (b_len > c_len):
    print(b, "has the most characters")
elif (c_len > a_len) and (c_len > b_len):
    print(c, "has the most characters")
else:
    print("all your strings have the same characters")