'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''

with open("/Users/kevinhan/Documents/CodingNomads/labs/08_file_io/words.txt", "r") as fin:
    longest = []
    shortest = []
    total = 0
    for line in fin.readlines():
        temp = line.strip()
        if len(longest) == 0:       # for the first item in the list, store it in both longest and shortest words list
            longest.append(temp)
            shortest.append(temp)
            continue
        if len(temp) == len(longest[0]):    # if long words are same length, add current word to long word list
            longest.append(temp)
        if len(temp) > len(longest[0]):     # if current is longer, clear previous longest word list and add current word
            longest = []
            longest.append(temp)
        if len(temp) == len(shortest[0]):   # if short words are same length, add current word to short word list
            shortest.append(temp)
        if len(temp) < len(shortest[0]):    # if current is shorter, clear previous shortest word list and add current word
            shortest = []
            shortest.append(temp)
        total += 1

# print the shortest words
newline = 0         # helps create a new line every 15th word to help with readability
print("\nThe shortest words in the list are:")
for words in shortest:
    print(f"{words:<4s} ", end="")
    newline += 1
    if newline == 15:
        print("")
        newline = 0

# print the longest words
print("\n\nThe longest words in the list are: ")
for words in longest:
    print(f"{words} ")

# print the total number of words
print(f"\nThere are {total} words in the file")