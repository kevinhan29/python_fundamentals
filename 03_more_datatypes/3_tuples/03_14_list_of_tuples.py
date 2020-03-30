'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''

# prompt user for input
user_input = input("Enter a sentence: ")
word_list = user_input.rsplit(sep=" ")
# print(word_list)

result_list = []
temp = []               # placeholder list to hold list of letters in each word

# read through each list word
for word in word_list:
    for letter in word:             # read through each letter in word and put the entire word into another list consisting of characters only
        temp.append(letter)
        #print(temp)
    result_list.append(tuple(temp)) # conver temp into a tuple and add it to the result list
    temp = []                       # reset temp list back to empty
    #print(result_list)

print(result_list)
