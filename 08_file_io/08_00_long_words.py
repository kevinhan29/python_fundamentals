'''
Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).
'''

with open("/Users/kevinhan/Documents/CodingNomads/labs/08_file_io/words.txt", "r") as fin:
    for line in fin.readlines():
        temp = line.strip()
        temp = temp.replace(" ", "")
        if len(temp) > 20:
            print(line.strip())