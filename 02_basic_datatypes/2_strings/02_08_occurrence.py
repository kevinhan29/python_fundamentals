'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''

# prompts user for inputs
sentence = input("Please enter a sentence or word: ")
letter = input("Please enter a letter: ")

# finding first occurrence of the letter
x = sentence.find(letter)
print(x)