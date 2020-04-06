'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

# read in all the lines of words.txt
with open("/Users/kevinhan/Documents/CodingNomads/labs/08_file_io/words.txt", "r") as fin:
    words_reverse = []
    for line in fin.readlines():
        words_reverse.insert(0, line)   # insert words to beginning of words_reverse lise, which will reverse the order

with open("/Users/kevinhan/Documents/CodingNomads/labs/08_file_io/words_reverse.txt", "w") as fout:
    fout.writelines(words_reverse)