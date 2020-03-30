'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

user_input = input("Type in a sentence: ")

word_list = user_input.split(sep=" ")           # separate word into list
#print(word_list)

most_occurence = [word_list[0]]     # initalize list to store words with most occurrences
total_count = 0                     # variable to save total count of highest occurring word

# read through each object in the word list
for i in word_list:
    temp = word_list.count(most_occurence[0])               # word count of current highest word occurrence
    if word_list.count(i) > temp:                           # if current word in list has higher occurrence
        for j in range(word_list.count(most_occurence[0])): # first, remove all occurrences of previous high word from original list
            word_list.remove(most_occurence[0])
            #print(word_list)
        most_occurence[0] = i                               # then save new highest occurrence word
        total_count = word_list.count(most_occurence[0])
        #print(most_occurence)
    elif word_list.count(i) < temp:
        for j in range(word_list.count(i)):                 # Remove all occurrences of previous high word from original list
            word_list.remove(i)
            #print(word_list)

print(word_list)
print(most_occurence)
# add additional words that have the same occurrences as the highest
while len(word_list) != 0:
    for i in most_occurence:
        if word_list[0] == i:
            word_list.remove(word_list[0])
            print("1", word_list)
        else:
            most_occurence.append(word_list[0])
            word_list.remove(word_list[0])
            print("2", most_occurence)

# print results
print("\nThe word(s) that appear the most in your sentence is/are:")
print(*most_occurence, sep = "\n")
print("They appear a total of", total_count, "times each.")