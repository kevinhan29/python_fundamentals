'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''

user_input = input("Type a sentence: ")
user_input = list(user_input)
letter_count = {}

while len(user_input) != 0:
    letter = user_input[0]              # stores current first letter in sentence
    temp = user_input.count(letter)          # number occurrences of first letter in sentence
    letter_count[letter] = temp
    # print("Dictionary:", letter_count)
    for i in range(temp):               # deletes all occurrences of the first letter in the sentence from sentence
        user_input.remove(letter)
        # print("input:", user_input)

# print number of characters in input
print("\nThe following characters appear in your sentence:")
for i in letter_count:
    print(i, ": ", letter_count[i], " times", sep="")